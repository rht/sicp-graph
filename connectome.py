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

prefix = 'dirac_sections'
metadata = open(prefix+'/metadata.txt','r').read().split('\n')[:-1]
book, labels = zip(*[i.split('|') for i in metadata])

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
    dictionary.save(prefix+'/dictionary.dict')
    raw_corpus = [dictionary.doc2bow(text) for text in texts]
    corpora.MmCorpus.serialize(prefix+"/corpus.mm", raw_corpus)


if prefix == 'sicp':
    #strip unreadable characters
    labels = [re.sub('\xc2|\xa0|\xe2|\x80|\x94',' ',i) for i in labels]

    # remove section name from labels
    labels = [ ((l[0].isdigit() and l[2].isdigit()) and l.split(' ')[0]) or l for l in labels]

    groups = [(l[0].isdigit() and l[0]) or 0 for l in labels]
elif prefix == 'dirac':
    labels = [ ((l[0].isdigit() and l[1].isdigit()) and l.split(' ')[0]) or l for l in labels]
    labels = [ (l[0].isdigit() and l.split(' ')[0]) or l for l in labels]
    groups = [((l[0].isdigit() and not l[1].isdigit()) and l[0]) or ((l[0].isdigit() and l[1].isdigit()) and l[:2]) or 0 for l in labels]
else:
    labels = [ ((l[0].isdigit() and l[1].isdigit()) and l.split(' ')[0]) or l for l in labels]
    labels = [ (l[0].isdigit() and l.split(' ')[0]) or l for l in labels]
    groups = [(l[0].isdigit() and l[0]) or 0 for l in labels]

#step 1 prepare corpus
prepare_corpus([open(section,'r').read().decode('utf-8') for section in book])
dictionary = corpora.Dictionary.load(prefix+'/dictionary.dict')
corpus = corpora.MmCorpus(prefix+"/corpus.mm")

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
#sims[sims < pylab.percentile(sims, 60)] = 0
#sims[sims < pylab.percentile(sims, 90)] = 0
sims[sims < pylab.percentile(sims, 95)] = 0

#step 4 convert datatype to networkx Graph
print "converting similarity matrix to networkx Graph"
sims = networkx.Graph(sims, node_list=range(len(book)))
networkx.set_node_attributes(sims, 'name', {x:y for x,y in enumerate(labels)})
networkx.set_node_attributes(sims, 'group', {x:y for x,y in enumerate(groups)})

#step 5: dump json for visualization in d3.js
json_data = json_graph.node_link_data(sims)
json.dump(json_data, open('visualize/graph_'+prefix+'.json', 'w'), indent=4)
#networkx.draw(sims)
#savefig('graph.png')
