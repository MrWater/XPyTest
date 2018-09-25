import numpy as np
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt

def dtr(maxdepth=2):
    import numpy as np
    from sklearn.tree import DecisionTreeRegressor
    import matplotlib.pyplot as plt

    # Create a random dataset
    rng = np.random.RandomState(100)
    X = np.sort(rng.rand(100, 1), axis=0)
    y = np.cos(X).ravel()
    y[::10] += (0.5 - rng.rand(10))
    # Fit regression model
    regr = DecisionTreeRegressor(max_depth=5)
    regr.fit(X, y)
    # Predict
    X_test = np.arange(0.0, 1.0, 0.01)[:, np.newaxis]
    y_predict = regr.predict(X_test)
    # Plot the results
    plt.scatter(X, y, s=20, edgecolor="black",
                c="darkorange", label="data")
    plt.plot(X_test, y_predict, color="blue", linewidth=2)
    plt.xlabel("data")
    plt.ylabel("target")
    plt.title("decision tree regression")
    plt.show()

dtr()