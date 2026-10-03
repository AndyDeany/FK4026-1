"""Module containing code for calculating and plotting linear regressions on datasets.

Includes the code for uppgifter 1-3.
"""
from matplotlib import pyplot as plt
import numpy as np
import numpy.typing as npt
import scipy.stats


plt.style.use("dark_background")


def uppgift_a(data_file: str) -> tuple[float, float]:
    """Code for Uppgift 1."""
    x, y = read_file(data_file)
    return calculate_regression_parameters_pure(x, y)


def uppgift_b(data_file: str) -> tuple[float, float]:
    """Code for Uppgift 2."""
    data = np.loadtxt(data_file)
    return calculate_regression_parameters_numpy(data[:, 0], data[:, 1])


def uppgift_c(data_file: str) -> tuple[float, float]:
    """Code for Uppgift 3."""
    data = np.loadtxt(data_file)
    return calculate_regression_parameters_scipy(data[:, 0], data[:, 1])


def read_file(data_file: str) -> tuple[list[float], list[float]]:
    """Read the data from the given file return lists of the x and y values contained therein."""
    x = []
    y = []
    with open(data_file, encoding="utf-8") as file:
        for line in file:
            x_value, y_value = line.split()
            x.append(float(x_value))
            y.append(float(y_value))

    return x, y


def calculate_regression_parameters_pure(x: list[float], y: list[float]) -> tuple[float, float]:
    """Take the given lists of x and y values and return the linear regression parameters (α, β).

    These parameters are calculated using pure Python (no external libraries).
    """
    n = len(x)
    s_x = sum(x)
    s_y = sum(y)
    s_xy = sum(x_value * y_value for x_value, y_value in zip(x, y))
    s_xx = sum(x_value ** 2 for x_value in x)

    beta = (n*s_xy - s_x*s_y)/(n*s_xx - s_x*s_x)
    alpha = (s_y - beta*s_x)/n

    return alpha, beta


def calculate_regression_parameters_numpy(x: npt.NDArray[np.float64],
                                          y: npt.NDArray[np.float64]) -> tuple[float, float]:
    """Take the given lists of x and y values and return the linear regression parameters (α, β).

    These parameters are calculated using NumPy.
    """
    n = len(x)
    s_x = np.sum(x)
    s_y = np.sum(y)
    s_xy = np.dot(x, y)
    s_xx = np.dot(x, x)

    beta = (n*s_xy - s_x*s_y)/(n*s_xx - s_x*s_x)
    alpha = (s_y - beta*s_x)/n

    return alpha, beta


def calculate_regression_parameters_scipy(x: npt.NDArray[np.float64],
                                          y: npt.NDArray[np.float64]) -> tuple[float, float]:
    """Take the given lists of x and y values and return the linear regression parameters (α, β).

    These parameters are calculated using scipy.
    """
    regression = scipy.stats.linregress(x, y)
    return regression.intercept, regression.slope


def plot_regression(x: np.ndarray[float], y: np.ndarray[float], alpha: float, beta: float) -> None:
    """Plot the given points together with their linear regression line.

    x, y: The values to plot on the graph.
    alpha, beta: The linear regression parameters to use for plotting the line of best fit.
    """
    # plt.scatter(x, y, color="pink", marker="$♥$", s=50)
    # plt.axline((0, alpha), slope=beta, color="#ffef5c")
    # plt.scatter(x, y, color="#34d6eb", marker="$♪$", s=50)
    # plt.axline((0, alpha), slope=beta, color="#eba134")
    plt.scatter(x, y, color="yellow", marker="$☼$", s=50)
    plt.axline((0, alpha), slope=beta, color="green")
    plt.show()
