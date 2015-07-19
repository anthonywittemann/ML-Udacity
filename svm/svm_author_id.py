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
# make the prediction
from sklearn.svm import SVC
classifier = SVC(kernel='linear')
classifier.fit(features_train, labels_train)
prediction = classifier.predict(features_test)
print "prediction", prediction


# calculate the accuracy (no. of points classified correctly / all points in test set)
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(prediction, labels_test)
print "accuracy", accuracy

#########################################################


