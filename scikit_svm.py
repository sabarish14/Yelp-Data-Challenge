from sklearn import cross_validation
from sklearn import metrics
from sklearn import svm
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics import precision_recall_fscore_support

from compute_avg import compute_avg


#from feature_vector import feature_vectorizer
#from metric import find_precision_recall
feature_file=open("price.txt","r") 
fm=open("predicted_labels","w")
fc=open("actual_labels","w")
class_file=open("labels","r")
features=feature_file.readlines()
labels=class_file.readlines()
#features=features[0:9]
#labels=labels[0:9]
i=0
for str in labels:
    labels[i]=str.replace("\n", "")
    i=i+1
kf = cross_validation.StratifiedKFold(labels, n_folds=10,shuffle=False)
accuracy=0
precision=[0 for i in range(2)]
recall=[0 for i in range(2)]
fscore=[0 for i in range(2)]
for train_index, test_index in kf:
        
    train_features=list( features[i] for i in train_index ) 
    train_labels=list( labels[i] for i in train_index )
    test_features=list( features[i] for i in test_index )
    test_labels=list( labels[i] for i in test_index )
    #count_vect = CountVectorizer(ngram_range=(1, 3))
    #my_count_vect=feature_vectorizer()
    count_vect = CountVectorizer()   
    clf = svm.LinearSVC()
    #X_train_counts,vocab=my_count_vect.build_feature_vector(train_features,"train")
    X_train_counts = count_vect.fit_transform(train_features,train_labels)
    '''tfidf_transformer = TfidfTransformer()
    X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts,train_labels)'''
    
    X_new_counts=count_vect.transform(test_features)  
   
    clf.fit(X_train_counts, train_labels)
    #X_new_counts,vocab = my_count_vect.build_feature_vector(test_features,"test")
    #X_new_tfidf = tfidf_transformer.fit_transform(X_train_counts)
    predicted = clf.predict(X_new_counts)
    accuracy+= metrics.accuracy_score(test_labels, predicted, normalize=True, sample_weight=None)
    #print accuracy
    metric= precision_recall_fscore_support(test_labels, predicted)
    precision+=metric[0]
    recall+=metric[1]
    fscore+=metric[2]
    for doc, category,actual in zip(test_features, predicted,test_labels):
                #misclassified_count+=1
                fm.write(category+"\n")
                fc.write(actual+"\n")
    #find_precision_recall(predicted, test_labels)
        #for doc, category,actual in zip(test_features, predicted,test_labels):
            #print('%r => predicted: %s   actual:%s ' % (doc, category,actual))
    #print(metrics.classification_report(test_labels, predicted,target_names=['-1','0','1']))
precision=precision/10
recall=recall/10
fscore=fscore/10
print precision,"\n", recall,"\n",fscore,"\n"  
print accuracy/10 
compute_avg()
#print len(test_labels)       