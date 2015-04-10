import numpy as np
import lda
from feature_vector import build_feature_vector
from preprocess import preprocess
from pos_tagging import pos_tag
from restaurant import restaurant
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
vocab=pos_tag(reviews)
print reviews
print vocab
X,vocab=build_feature_vector(reviews,vocab)    
X=np.asarray(X)    
#titles = lda.datasets.load_reuters_titles()
#X.shape
model = lda.LDA(n_topics=20, n_iter=1500, random_state=1)
model.fit(X)  # model.fit_transform(X) is also available
topic_word = model.topic_word_  # model.components_ also works
n_top_words = 8

for i, topic_dist in enumerate(topic_word):
    topic_words = np.array(vocab)[np.argsort(topic_dist)][:-n_top_words:-1]
    print('Topic {}: {}'.format(i, ' '.join(topic_words)))
doc_topic = model.doc_topic_
for i in range(10):
    print(" (top topic: {})".format(doc_topic[i].argmax()))