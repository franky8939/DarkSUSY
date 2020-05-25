from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures
from modules.maquine_learning.Paq_ML import *

def regresion(X_train, Y_train, X_test=None, Y_test=None, ax=None, degree=5):
    poly_features = PolynomialFeatures(degree=degree)
    # transforms the existing features to higher degree features.
    X_train_poly = poly_features.fit_transform(X_train)
    # fit the transformed features to Linear Regression
    poly_model = LinearRegression()
    poly_model.fit(X_train_poly, Y_train)
    # predicting on training data-set
    y_train_predicted = poly_model.predict(X_train_poly)
    # predicting on test data-set
    y_test_predict = poly_model.predict(poly_features.fit_transform(X_test))

    # evaluating the model on training dataset
    rmse_train = np.sqrt(mean_squared_error(Y_train, y_train_predicted))
    r2_train = r2_score(Y_train, y_train_predicted)
    print("The model performance for the training set")
    print("RMSE of training set is {}".format(rmse_train))
    print("R2 score of training set is {}".format(r2_train))
    if X_test is not None and Y_test is not None:
        # evaluating the model on test dataset
        rmse_test = np.sqrt(mean_squared_error(Y_test, y_test_predict))
        r2_test = r2_score(Y_test, y_test_predict)
        print("\n")
        print("The model performance for the test set")
        print("RMSE of test set is {}".format(rmse_test))
        print("R2 score of test set is {}".format(r2_test))
        if ax is None:
            plt.plot(np.exp(Y_test), np.exp(y_test_predict), '.')
        else:
            ax.plot(np.exp(Y_test), np.exp(y_test_predict), '.')
        return poly_model, rmse_train, r2_train, rmse_test, r2_test, ax
    return poly_model, rmse_train, r2_train