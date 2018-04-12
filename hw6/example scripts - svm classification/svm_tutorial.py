import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn import svm
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV

iris = datasets.load_iris()
print iris.data.shape, iris.target.shape

X_train, X_test, y_train, y_test, = train_test_split(iris.data, iris.target, test_size=0.1, random_state = 0)
print X_train.shape, y_train.shape
print X_test.shape, y_test.shape

clf = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)
print clf.score(X_test, y_test)

clf = svm.SVC(kernel='linear', C=1)
scores = cross_val_score(clf, iris.data, iris.target, cv=10)
print scores

print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std()*2 ))

tuned_parameters = [{'kernel': ['rbf'], 'gamma': [1e-3, 1e-4],'C': [1, 10, 100, 1000]},{'kernel': ['linear'], 'C': [1, 10, 100, 1000]}]
scores = ['precision', 'recall']
svr = svm.SVC(C=1)
for score in scores:
    print("# Tuning hyper-parameters for %s"% score)
    clf =GridSearchCV(svr, tuned_parameters, cv=10,scoring='%s_macro'% score)
    clf.fit(X_train, y_train)
    print("best parameters %s" % clf.best_params_)
    means = clf.cv_results_['mean_test_score']
    stds = clf.cv_results_['std_test_score']
    for mean, std, params in zip(means, stds, clf.cv_results_['params']):
        print("%0.3f (+/-%0.03f) for %r"% (mean, std *2, params))
    y_true, y_pred = y_test, clf.predict(X_test)
