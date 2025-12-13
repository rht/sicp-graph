import re
import os
import json

from dotenv import load_dotenv

load_dotenv()

import numpy as np
import nltk
import tiktoken
from openai import OpenAI
from sklearn.metrics.pairwise import cosine_similarity
import networkx
from networkx.readwrite import json_graph

# Download NLTK data if not present
try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")

# Configuration
prefix = ["sicp", "dirac", "dirac_sections", "sicm", "som"][2]
metadata = open("texts/" + prefix + "/metadata.txt", "r").read().split("\n")[:-1]
if prefix == "dirac_sections":
    book, labels = zip(*[i.split("|") for i in metadata])
else:
    wordcount, book, labels = zip(*[i.split("|") for i in metadata])

# OpenAI client (uses OPENAI_API_KEY env var)
client = OpenAI()
MODEL = "text-embedding-3-small"
MAX_TOKENS = 8191  # OpenAI's limit for this model

# Tokenizer for accurate token counting
encoding = tiktoken.encoding_for_model(MODEL)


def count_tokens(text):
    """Count tokens using tiktoken for accurate measurement."""
    return len(encoding.encode(text))


def chunk_document(text, max_tokens=8000):
    """Split document into chunks that fit within token limit.

    OpenAI's text-embedding-3-small has an 8191 token limit.
    Uses tiktoken for accurate token counting.
    """
    if count_tokens(text) <= max_tokens:
        return [text]

    sentences = nltk.sent_tokenize(text)
    chunks = []
    current_chunk = []
    current_tokens = 0

    for sentence in sentences:
        sentence_tokens = count_tokens(sentence)

        # Handle case where a single sentence exceeds limit
        if sentence_tokens > max_tokens:
            # Save current chunk if any
            if current_chunk:
                chunks.append(" ".join(current_chunk))
                current_chunk = []
                current_tokens = 0
            # Split long sentence by encoding and chunking tokens directly
            encoded = encoding.encode(sentence)
            for i in range(0, len(encoded), max_tokens):
                chunk_tokens = encoded[i : i + max_tokens]
                chunks.append(encoding.decode(chunk_tokens))
            continue

        # Check if adding this sentence would exceed limit
        test_tokens = (
            current_tokens + sentence_tokens + (1 if current_chunk else 0)
        )  # +1 for space

        if test_tokens > max_tokens:
            # Save current chunk and start new one
            chunks.append(" ".join(current_chunk))
            current_chunk = [sentence]
            current_tokens = sentence_tokens
        else:
            current_chunk.append(sentence)
            current_tokens = test_tokens

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks if chunks else [text]


def embed_texts(texts):
    """Embed multiple texts using OpenAI API one at a time."""
    embeddings = []

    for text in texts:
        tokens = count_tokens(text)
        if tokens > MAX_TOKENS:
            print(f"Warning: text has {tokens} tokens, truncating to {MAX_TOKENS}")
            # Truncate to fit
            encoded = encoding.encode(text)[:MAX_TOKENS]
            text = encoding.decode(encoded)

        response = client.embeddings.create(model=MODEL, input=text)
        embeddings.append(response.data[0].embedding)

    return np.array(embeddings)


def embed_document(text):
    """Embed a document, chunking if necessary and averaging."""
    chunks = chunk_document(text)

    if len(chunks) == 1:
        response = client.embeddings.create(model=MODEL, input=chunks[0])
        return np.array(response.data[0].embedding)

    # Multiple chunks: embed and average
    chunk_embeddings = embed_texts(chunks)
    return np.mean(chunk_embeddings, axis=0)


def get_embeddings(documents, prefix, force_recompute=False):
    """Load cached embeddings or compute and cache them."""
    cache_path = f"texts/{prefix}/embeddings_openai.npy"

    if os.path.exists(cache_path) and not force_recompute:
        print(f"Loading cached embeddings from {cache_path}")
        return np.load(cache_path)

    print(f"Computing embeddings for {len(documents)} documents using OpenAI API...")
    embeddings = np.array([embed_document(doc) for doc in documents])

    np.save(cache_path, embeddings)
    print(f"Saved embeddings to {cache_path}")

    return embeddings


# Process labels based on book type
if (prefix == "sicp") or (prefix == "sicm"):
    # Strip unreadable characters
    labels = [re.sub("\xc2|\xa0|\xe2|\x80|\x94", " ", i) for i in labels]
    groups = [(l[0].isdigit() and l[0]) or 0 for l in labels]

elif prefix == "dirac":
    groups = [l.split(".")[0] for l in labels]

elif prefix == "dirac_sections":
    labels = [l.split(".")[0] for l in labels if l[0].isdigit()]
    groupdic = {
        d[0]: d[1]
        for d in [
            i.split(" ")
            for i in open("texts/" + prefix + "/metadata_extra.txt", "r")
            .read()
            .strip()
            .split("\n")
        ]
    }
    groups = [groupdic[i] for i in labels]

else:
    groups = [l.split(".")[0] for l in labels]

# Step 1: Load documents
print("Loading documents...")
documents = [open("texts/" + section, "r").read() for section in book]

# Step 2: Compute embeddings via OpenAI API
embeddings = get_embeddings(documents, prefix)

# Step 3: Compute similarity matrix
print("Computing similarity matrix...")
sims = cosine_similarity(embeddings)

# Step 4: Apply percentile threshold
percentile = {"sicp": 90, "sicm": 95, "dirac": 60, "dirac_sections": 95, "som": 98}[
    prefix
]
sims[sims < np.percentile(sims, percentile)] = 0

# Step 5: Convert to NetworkX Graph
print("Converting similarity matrix to networkx Graph")
sims = networkx.Graph(sims, node_list=list(range(len(book))))
networkx.set_node_attributes(sims, {x: y for x, y in enumerate(labels)}, "name")
networkx.set_node_attributes(sims, {x: y for x, y in enumerate(groups)}, "group")
wordcount_normalize = {"sicp": 1000, "sicm": 500}.get(prefix, 1000)
if prefix != "dirac_sections":
    networkx.set_node_attributes(
        sims,
        {x: float(y) / wordcount_normalize for x, y in enumerate(wordcount)},
        "wordcount",
    )

# Step 6: Export JSON for D3.js visualization
json_data = json_graph.node_link_data(sims)
json.dump(json_data, open("docs/json/" + prefix + ".json", "w"), indent=4)
print(f"Saved graph to docs/json/{prefix}.json")
