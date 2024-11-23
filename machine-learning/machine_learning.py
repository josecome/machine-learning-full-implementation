# Machine Learning Models
from sklearn.model_selection import train_test_split
from sklearn import datasets, svm
#Models

# SVM (with iris dataset)
iris = datasets.load_iris()

X = iris.data[:, :4]
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=42)



C = 1.0  # SVM regularization parameter
models = (
    svm.SVC(kernel="linear", C=C),
    svm.LinearSVC(C=C, max_iter=10000),
    svm.SVC(kernel="rbf", gamma=0.6, C=C),
    svm.SVC(kernel="poly", degree=3, gamma="auto", C=C),
)

models = list(clf.fit(X_train, y_train) for clf in models)

clf1, clf2, clf3, clf4 = models

clf1.predict(X_test)
clf2.predict(X_test)
clf3.predict(X_test)
clf4.predict(X_test)


