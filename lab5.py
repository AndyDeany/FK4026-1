"""Module containing solutions for labb 5."""
from matplotlib import pyplot as plt
import numpy as np
import scipy.stats


plt.style.use("dark_background")


def uppgift_a(file_name: str) -> None:
    """Code for Uppgift 1."""
    x, y = read_file(file_name)
    return calculate_regression_parameters_pure(x, y)


def uppgift_b(file_name: str) -> None:
    """Code for Uppgift 2."""
    data = np.loadtxt(file_name)
    return calculate_regression_parameters_numpy(data[:, 0], data[:, 1])


def uppgift_c(file_name: str) -> None:
    """Code for Uppgift 3."""
    data = np.loadtxt(file_name)
    return calculate_regression_parameters_scipy(data[:, 0], data[:, 1])


def read_file(file_name: str) -> Tuple[list[float], list[float]]:
    """Read the data file with the given name and return lists of the included x and y values."""
    x = []
    y = []
    with open(file_name) as file:
        for line in file:
            x_value, y_value = line.split()
            x.append(float(x_value))
            y.append(float(y_value))

    return x, y


def calculate_regression_parameters_pure(x: list[float], y: list[float]) -> tuple:
    """Take the given lists of x and y values and return the regression parameters.

    The parameters are calculated using pure Python (no external libraries).
    """
    n = len(x)
    s_x = sum(x)
    s_y = sum(y)
    s_xy = sum(x_value * y_value for x_value, y_value in zip(x, y))
    s_xx = sum(x_value ** 2 for x_value in x)

    beta = (n*s_xy - s_x*s_y)/(n*s_xx - s_x*s_x)
    alpha = (s_y - beta*s_x)/n

    return alpha, beta


def calculate_regression_parameters_numpy(x: np.ndarray[float], y: np.ndarray[float]) -> tuple:
    """Take the given lists of x and y values and return the regression parameters.

    These parameters are calculated using numpy (as opposed to pure Python).
    """
    n = len(x)
    s_x = np.sum(x)
    s_y = np.sum(y)
    s_xy = np.dot(x, y)
    s_xx = np.dot(x, x)

    beta = (n*s_xy - s_x*s_y)/(n*s_xx - s_x*s_x)
    alpha = (s_y - beta*s_x)/n

    return alpha, beta


def calculate_regression_parameters_scipy(x: list[float], y: list[float]) -> tuple:
    """Take the given lists of x and y values and return the regression parameters.

    These parameters are calculated using scipy.
    """
    regression = scipy.stats.linregress(x, y)
    return regression.intercept, regression.slope


def plot_regression(x: ndarray[float], y: ndarray[float], alpha: float, beta: float) -> None:
    """Plot the given points together with their linear regression line."""
    # plt.scatter(x, y, color="pink", marker="$♥$", s=50)
    # plt.axline((0, alpha), slope=beta, color="#ffef5c")
    plt.scatter(x, y, color="#34d6eb", marker="$♪$", s=50)
    plt.axline((0, alpha), slope=beta, color="#eba134")
    # plt.scatter(x, y, color="yellow", marker="$☼$", s=50)
    # plt.axline((0, alpha), slope=beta, color="green")
    plt.show()


def read_and_plot(file_name: str, regression_parameter_function: function) -> None:
    """Read the given file and plot the result given data with its regression line."""
    alpha, beta = regression_parameter_function(file_name)
    plot_regression(*read_file(file_name), alpha, beta)


def main():
    """Run the main program."""
    read_and_plot("small.txt", uppgift_a)
    read_and_plot("medium.txt", uppgift_a)
    read_and_plot("large.txt", uppgift_a)
    read_and_plot("small.txt", uppgift_b)
    read_and_plot("medium.txt", uppgift_b)
    read_and_plot("large.txt", uppgift_b)
    read_and_plot("small.txt", uppgift_c)
    read_and_plot("medium.txt", uppgift_c)
    read_and_plot("large.txt", uppgift_c)


if __name__ == "__main__":
    main()

