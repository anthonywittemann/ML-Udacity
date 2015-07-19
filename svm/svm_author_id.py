#!/usr/bin/python

""" 
    this is the code to accompany the Lesson 2 (SVM) mini-project

    use an SVM to identify emails from the Enron corpus by their authors
    
    Sara has label 0
    Chris has label 1

"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################

#reduce the training set size
#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100] 

# make the prediction
from sklearn.svm import SVC
#classifier = SVC(kernel='linear')
# try different values of C - 10.0, 100., 1000., and 10000. (10000 best)
classifier = SVC(kernel='rbf', C=10000.) 
classifier.fit(features_train, labels_train)
prediction = classifier.predict(features_test)
print 'prediction', prediction
# predict the values of the 10th, 26th, 50th emails
#for i in [10,26,50]:
#	print i, ": ", prediction[i]

# count the number of emails by Chris (value of 1)
print 'number of Chris emails:', sum(prediction == 1)

# calculate the accuracy (no. of points classified correctly / all points in test set)
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(prediction, labels_test)
print 'accuracy', accuracy

#########################################################


