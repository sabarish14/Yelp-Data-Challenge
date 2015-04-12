import numpy as np
import lda
from sklearn.feature_extraction.text import CountVectorizer
from feature_vector import build_feature_vector
from preprocess import preprocess
from pos_tagging import pos_tag
from restaurant import restaurant
import operator


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
'''vocab=pos_tag(reviews)
#print reviews
#print vocab
X,vocab=build_feature_vector(reviews,vocab)    
X=np.asarray(X)    
#titles = lda.datasets.load_reuters_titles()'''
reviews=pos_tag(reviews)
vec = CountVectorizer()
X = vec.fit_transform(reviews)
vocab = vec.get_feature_names()
X.shape
model = lda.LDA(n_topics=200, n_iter=1500, random_state=1)
model.fit(X)  # model.fit_transform(X) is also available
topic_word = model.topic_word_  # model.components_ also works
n_top_words = 8
topic_words=[]
for i, topic_dist in enumerate(topic_word):
    topic_words.append(np.array(vocab)[np.argsort(topic_dist)][:-n_top_words:-1])
    print len(topic_words)
    #print('Topic {}: {}'.format(i, ' '.join(topic_words)))
doc_topic = model.doc_topic_
top_topics=[]
for i in range(len(r.id)):
    top_topics.append(doc_topic[i].argmax())
    print("(top topic: {})".format( doc_topic[i].argmax()))
top_topic_words=[]
for i in range(len(top_topics)):
    top_topic_words.append(topic_words[top_topics[i]])
word_hash={}
for lines in top_topic_words:
    for words in lines:
        try:
            word_hash[words]+=1
        except KeyError:
            word_hash[words]=1

sorted_x = sorted(word_hash.items(), key=operator.itemgetter(1),reverse=True)  
print sorted_x[1:10]     
        
    
    
    #print("{} (top topic: {})".format(titles[i], doc_topic[i].argmax()))