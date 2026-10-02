"""Module containing solutions for labb 5."""
from matplotlib import pyplot as plt
import numpy as np
import scipy.stats
import timeit


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


def benchmark_function(regression_parameter_function: function) -> None:
    print(regression_parameter_function)
    for file_name in ("small.txt", "medium.txt", "large.txt"):
        benchmark_function_on_file(file_name, regression_parameter_function)


def benchmark_function_on_file(file_name: str, regression_parameter_function: function) -> float:
    """Benchmark the given regression parameter function on the given file. Returns average execution time in seconds."""
    print(file_name, timeit.timeit(lambda: regression_parameter_function(file_name), number=1000))


def main():
    """Run the main program."""
    # read_and_plot("small.txt", uppgift_a)
    # read_and_plot("medium.txt", uppgift_a)
    # read_and_plot("large.txt", uppgift_a)
    # read_and_plot("small.txt", uppgift_b)
    # read_and_plot("medium.txt", uppgift_b)
    # read_and_plot("large.txt", uppgift_b)
    # read_and_plot("small.txt", uppgift_c)
    # read_and_plot("medium.txt", uppgift_c)
    # read_and_plot("large.txt", uppgift_c)
    benchmark_function(uppgift_a)
    benchmark_function(uppgift_b)
    benchmark_function(uppgift_c)
    """
    <function uppgift_a at 0x0000023CDB536C40>
    small.txt 1.7332542000804096
    medium.txt 15.545606799889356
    large.txt 158.95802869996987
    <function uppgift_b at 0x0000023CEE6D5900>
    small.txt 0.9451810999307781
    medium.txt 5.78290730016306
    large.txt 57.73936649993993
    <function uppgift_c at 0x0000023CEE6D7270>
    small.txt 1.7974177000578493
    medium.txt 6.684295400045812
    large.txt 59.77635780000128
    """


if __name__ == "__main__":
    main()

