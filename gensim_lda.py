from gensim import matutils
from gensim.models.ldamodel import LdaModel
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from feature_vector import build_feature_vector
from preprocess import preprocess
from pos_tagging import pos_tag
from restaurant import restaurant
#import lda.datasets
filename="az_fast_food_w_elite.csv"
r=restaurant(filename)
r.group_review()
#print r.reviews
reviews=preprocess(r.reviews)
#pos_tag(reviews)
#X=reviews
#vocab=[]
#X = lda.datasets.load_reuters()
#vocab = lda.datasets.load_reuters_vocab()
reviews=pos_tag(reviews)
#print reviews
#print vocab
#X,vocab=build_feature_vector(reviews,vocab)    
vec = CountVectorizer()
X = vec.fit_transform(reviews)
vocab = vec.get_feature_names()
#X=np.asarray(X)  
print "X created"
lda=LdaModel(matutils.Sparse2Corpus(X), num_topics=20,
                    passes=100,
                    id2word=dict([(i, s) for i, s in enumerate(vocab)]))
topics = lda.show_topics(num_topics=20, formatted=False)
for ti, topic in enumerate(topics):
        print 'topic %d: %s' % (ti, ' '.join('%s/%.2f' % (t[1], t[0]) for t in topic))