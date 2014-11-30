import re
import string
from time import time
import json

import nltk
from collections import Counter
from gensim import utils, corpora, models, similarities
from gensim.parsing import preprocessing
import networkx
from networkx.readwrite import json_graph
import pylab

bookname = 'sicp'

def prepare_corpus(documents):
    tic = time()
    # lower, strip tags, strip punctuation, strip multiple whitespaces,
    # strip numeric, remove stopwords, strip short, stem text
    texts = preprocessing.preprocess_documents(documents)

    #texts = [nltk.word_tokenize(document) for document in documents]

    #filter out hapax legomena
    all_tokens = sum(texts, [])
    tokens_once = set(word for word in set(all_tokens) if all_tokens.count(word)==1)
    texts = [[word for word in text if word not in tokens_once]
             for text in texts]
    print time() - tic

    dictionary = corpora.Dictionary(texts)
    dictionary.save('sicp.dict')
    raw_corpus = [dictionary.doc2bow(text) for text in texts]
    corpora.MmCorpus.serialize(bookname+".mm", raw_corpus)

book = [
"markdown/book-Z-H-10.html.md",
"markdown/book-Z-H-11.html.md",
"markdown/book-Z-H-12.html.md",
"markdown/book-Z-H-13.html.md",
"markdown/book-Z-H-14.html.md",
"markdown/book-Z-H-15.html.md",
"markdown/book-Z-H-16.html.md",
"markdown/book-Z-H-17.html.md",
"markdown/book-Z-H-18.html.md",
"markdown/book-Z-H-19.html.md",
"markdown/book-Z-H-1.html.md",
"markdown/book-Z-H-20.html.md",
"markdown/book-Z-H-21.html.md",
"markdown/book-Z-H-22.html.md",
"markdown/book-Z-H-23.html.md",
"markdown/book-Z-H-24.html.md",
"markdown/book-Z-H-25.html.md",
"markdown/book-Z-H-26.html.md",
"markdown/book-Z-H-27.html.md",
"markdown/book-Z-H-28.html.md",
"markdown/book-Z-H-29.html.md",
"markdown/book-Z-H-2.html.md",
"markdown/book-Z-H-30.html.md",
"markdown/book-Z-H-31.html.md",
"markdown/book-Z-H-32.html.md",
"markdown/book-Z-H-33.html.md",
"markdown/book-Z-H-34.html.md",
"markdown/book-Z-H-35.html.md",
"markdown/book-Z-H-36.html.md",
"markdown/book-Z-H-37.html.md",
"markdown/book-Z-H-38.html.md",
"markdown/book-Z-H-3.html.md",
"markdown/book-Z-H-4.html.md",
"markdown/book-Z-H-5.html.md",
"markdown/book-Z-H-6.html.md",
"markdown/book-Z-H-7.html.md",
"markdown/book-Z-H-8.html.md",
"markdown/book-Z-H-9.html.md"]

try:
    labels = open('titles.txt','r').read().split('\n')[:-1]

    #strip unreadable characters
    labels = [re.sub('\xc2|\xa0|\xe2|\x80|\x94',' ',i) for i in labels]

    # remove section name from labels
    labels = [ ((l[0].isdigit() and l[2].isdigit()) and l.split(' ')[0]) or l for l in labels]

    groups = [(l[0].isdigit() and l[0]) or 0 for l in labels]
except:
    labels = {i:i+1 for i in range(len(book))}

#step 1 prepare corpus
#prepare_corpus([open(section,'r').read().decode('utf-8') for section in book])
dictionary = corpora.Dictionary.load('sicp.dict')
corpus = corpora.MmCorpus(bookname+".mm")

#step 2 create tf-idf model
tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]  # convert vector space to tfidf space

#step 2.1 create LDA model
numTopics = 50
lda = models.ldamodel.LdaModel(corpus_tfidf, id2word=dictionary, num_topics=numTopics)
topics = lda.show_topics(num_topics=numTopics)
#print topics
for text in corpus:
    for id,freq in lda[text]:
        print dictionary[id], freq
    print

#step 3 create similarity matrix
index = similarities.Similarity('/tmp/tst', corpus_tfidf.corpus, num_features=corpus.num_terms+1)
sims = index[corpus_tfidf]
#step 3.1
sims[sims < pylab.percentile(sims, 90)] = 0

#step 4 convert datatype to networkx Graph
print "converting similarity matrix to networkx Graph"
sims = networkx.Graph(sims, node_list=range(len(book)))
networkx.set_node_attributes(sims, 'name', {x:y for x,y in enumerate(labels)})
networkx.set_node_attributes(sims, 'group', {x:y for x,y in enumerate(groups)})

#step 5: dump json for visualization in d3.js
json_data = json_graph.node_link_data(sims)
json.dump(json_data, open('visualize/graph_'+bookname+'.json', 'w'), indent=4)
#networkx.draw(sims)
#savefig('graph.png')
