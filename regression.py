__author__ = 'Sabarish'

#from sklearn import metrics
from sklearn.svm import SVR
import xlrd
from matplotlib import pyplot as pl
#from mpl_toolkits.mplot3d import Axes3D
import numpy as np
#import pylab as pl


def open_file(path):
    book = xlrd.open_workbook(path)
    sheet = book.sheet_by_name("Sheet1")
    rows = sheet.nrows
    for i in range(1,rows):
        col = sheet.row_values(i)
        features = []
        features.append(col[2])         #location
        features.append(col[5])         #service
        features.append(col[8])         #price
        training_features.append(features)
        training_rating.append(round(col[1],2))

def regression(features,rating):
    train_data = features[1:155]
    train_label = rating[1:155]

    X = np.array(train_data)
    Y = np.array(train_label)
    svr_rbf = SVR(kernel='rbf')
    clf = svr_rbf.fit(X,Y)

    test_data = features[156:]
    test_label = rating[156:]


    x_test = np.array(test_data)
    y_test = np.array(test_label)
    y_rbf = clf.predict(x_test)
    params = clf.get_params(deep = True)
    print(params)
    score = clf.score(x_test,y_test)
    print(score)
    #print x_test[:,0]
    #print x_test[:,1]
    print x_test.shape
    print y_test.shape
    
    '''pl.scatter(x_test,y_test,c='k',label='data')
    pl.hold('on')
    #pl.plot(X,y_test,c='g',label = 'RBF Model')
    pl.xlabel('data')
    pl.ylabel('target')
    pl.title('Support Vector Regression')
    pl.legend()
    pl.show()'''

    y_true = []
    y_pred = []

    accuracy=0
    for i in range(len(x_test)):
        label = clf.predict(x_test[i])
        y_true.append(round(y_test[i]))
        y_pred.append (round(label[0],2))
        if abs(y_pred[i]-y_true[i])<0.3:
            accuracy+=1
    #accuracy=float(accuracy)/len(y_pred)
            
    '''fig = pl.figure()
    
    ax = fig.add_subplot(2,1,1, projection='3d')
    ax1 = fig.add_subplot(2,1,2, projection='3d')
    ax.scatter(x_test[:,0], x_test[:,1], y_test, c='r')
    ax.set_xlabel('service')
    ax.set_ylabel('price')
    ax.set_zlabel('rating')
    ax1.set_xlabel('service')
    ax1.set_ylabel('price')
    ax1.set_zlabel('rating')
    
    
    #pl.hold('on')
    ax1.scatter(x_test[:,0], x_test[:,1], y_pred, c='b')  
    pl.show()''
    
    print "real accuracy:",accuracy
    print(y_test)
    print(y_pred)'''



path = "data.xlsx"
training_features = []
training_rating = []
open_file(path)
regression(training_features,training_rating)
