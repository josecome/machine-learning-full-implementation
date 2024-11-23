# Machine Learning Models
from sklearn.model_selection import train_test_split
from sklearn import datasets, svm
from sklearn.metrics import (
    mean_squared_error,
    mean_absolute_error,
    r2_score,
    accuracy_score,
)

#Models
class MLModels:
    X_test = None
    y_test = None

    def load_data():
        # SVM (with iris dataset)
        iris = datasets.load_iris()
        X = iris.data[:, :4]
        y = iris.target

        return train_test_split(X, y, test_size=0.33, random_state=42)


    @classmethod
    def train_models(cls):
        X_train, X_test, y_train, y_test = cls.load_data()
        cls.X_test = X_test
        cls.y_test = y_test

        C = 1.0  # SVM regularization parameter
        models = (
            svm.SVC(kernel="linear", C=C),
            svm.LinearSVC(C=C, max_iter=10000),
            svm.SVC(kernel="rbf", gamma=0.6, C=C),
            svm.SVC(kernel="poly", degree=3, gamma="auto", C=C),
        )
        return list(clf.fit(X_train, y_train) for clf in models)


    @classmethod
    def test_and_evaluate(cls):    
        clf1, clf2, clf3, clf4 = cls.train_models()

        y_pred1 = clf1.predict(cls.X_test)
        y_pred2 = clf2.predict(cls.X_test)
        y_pred3 = clf3.predict(cls.X_test)
        y_pred4 = clf4.predict(cls.X_test)

        # Evaluate the model
        # Model 1
        accuracy1 = accuracy_score(cls.y_test, y_pred1)
        mse1 = mean_squared_error(cls.y_test, y_pred1)
        mae1 = mean_absolute_error(cls.y_test, y_pred1)
        r21 = r2_score(cls.y_test, y_pred1)
        print(accuracy1, mse1, mae1, r21)

        # Model 2
        accuracy2 = accuracy_score(cls.y_test, y_pred2)
        mse2 = mean_squared_error(cls.y_test, y_pred2)
        mae2 = mean_absolute_error(cls.y_test, y_pred2)
        r22 = r2_score(cls.y_test, y_pred2)
        print(accuracy2, mse2, mae2, r22)

        # Model 3
        accuracy3 = accuracy_score(cls.y_test, y_pred3)
        mse3 = mean_squared_error(cls.y_test, y_pred3)
        mae3 = mean_absolute_error(cls.y_test, y_pred3)
        r23 = r2_score(cls.y_test, y_pred3)
        print(accuracy3, mse3, mae3, r23)

        # Model 4
        accuracy4 = accuracy_score(cls.y_test, y_pred4)
        mse4 = mean_squared_error(cls.y_test, y_pred4)
        mae4 = mean_absolute_error(cls.y_test, y_pred4)
        r24 = r2_score(cls.y_test, y_pred4)
        print(accuracy4, mse4, mae4, r24)


MLModels.test_and_evaluate()