# SICP-Graph

This project began from a question "can machines understand the text within SICP?".


A graph visualization of the interconnectedness between the sections in SICP.

## Method

Similarity is computed using a hybrid approach combining semantic and lexical methods:

1. **Semantic similarity**: OpenAI's `text-embedding-3-small` embeddings with cosine similarity
2. **Lexical similarity**: BM25 (Okapi BM25) for keyword-based matching

The final similarity score combines both: `0.7 * semantic + 0.3 * lexical`. This captures both conceptual relationships (via embeddings) and shared terminology (via BM25).

A k-NN threshold is applied to keep only the top-k most similar neighbors per chapter, resulting in a sparse similarity graph visualized with D3.js force-directed layout.

## Directory structure

- `docs` contains all the data and the static pages rendered on gh-pages
- `texts` contains the cleaned html and markdown version of each texts
- `connectome.py` computes semantic similarity using OpenAI embeddings
- `connectome_tfidf.py` legacy TF-IDF approach (preserved for comparison)

The graph visualization has since been extended to other texts:
- [Structure and Interpretation of Computer Programs](https://rht.github.io/sicp-graph)
- [Structure and Interpretation of Classical Mechanics](https://rht.github.io/sicp-graph/index.html?type=sicm)
   * Lagrangian mechanics is more related to rigid bodies than Hamiltonian mechanics.
- The Principles of Quantum Mechanics: [chapters](https://rht.github.io/sicp-graph/index.html?type=dirac),
  [sections](https://rht.github.io/sicp-graph/index.html?type=dirac_sections)
- [The Society of Mind](https://rht.github.io/sicp-graph/index.html?type=som). Sourced From http://www.aurellem.org/minsky/
  * Each sections are highly correlated with each other
