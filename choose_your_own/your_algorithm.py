#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow" points mixed
### in together--separate them so we can give them different colors in the scatterplot,
### and visually identify them
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
#################################################################################

print 'starting training'

### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

# KNN Classifier
from sklearn.neighbors import KNeighborsClassifier 
clf = KNeighborsClassifier(n_neighbors=4)	#accuracy with nn=3: .936, nn=4: .94, nn=5: .92

# Ensemble Methods: Adaboost, Random Forest
#from sklearn.ensemble import AdaBoostClassifier	# accuracy n_est=2: .804
#clf = AdaBoostClassifier(n_estimators=2)

#from sklearn.ensemble import RandomForestClassifier		# accuracy n_est=20, max_depth=5: .92
#clf = RandomForestClassifier(n_estimators=20, max_depth=5)


clf.fit(features_train, labels_train)
prediction = clf.predict(features_test)

from sklearn.metrics import accuracy_score
acc = accuracy_score(prediction, labels_test)
print 'accuracy:', acc


try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
