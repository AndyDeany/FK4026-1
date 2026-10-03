"""Module containing solutions for labb 5."""
from matplotlib import pyplot as plt
import numpy as np
import numpy.typing as npt
import scipy.stats
import timeit

from helmholtz_fd import solve_helmholtz
from regression import (uppgift_a, uppgift_b, uppgift_c,
                        read_file, calculate_regression_parameters_scipy, plot_regression)


plt.style.use("dark_background")


DATA_FILES = ("small.txt", "medium.txt", "large.txt")


def uppgift_4() -> None:
    """Code for Uppgift 4.

    A typical execution prints the following:
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

    This shows that pure python is about 3x slower than NumPy/SciPy.
    NumPy and SciPy are roughly equally fast, likely because SciPy
    uses NumPy internally for calculations.
    """
    benchmark_function(uppgift_a)
    benchmark_function(uppgift_b)
    benchmark_function(uppgift_c)


def uppgift_5() -> None:
    """Code for Uppgift 5."""
    for k in (1, 5, 10):
        x, u, norm = solve_helmholtz(k)
        print("Number of grid points:", len(x), "Solution norm:", norm)
        print("Independently calculated norm:", calculate_norm(x, u))

        plt.plot(x, np.real(u), label=f"k={k}")
        plt.xlabel("x")
        plt.ylabel("Re(u)")
        plt.title("Helmholtz solutions for different values of k")

    plt.legend()
    plt.show()


def uppgift_6() -> None:
    """Code for Uppgift 6."""
    ks = np.linspace(0, 8, 100)
    norms = []
    for k in ks:
        x, u, norm = solve_helmholtz(k)
        norms.append(norm)

    plt.xlabel("k")
    plt.ylabel("norm")
    plt.title("Plot of scaled L2 norm as a function of wavenumber k")
    plot_regression(ks, norms, *calculate_regression_parameters_scipy(ks, norms))


def read_and_plot(file_name: str, regression_parameter_function: function) -> None:
    """Read the given file and plot the result given data with its regression line."""
    alpha, beta = regression_parameter_function(file_name)
    plot_regression(*read_file(file_name), alpha, beta)


def benchmark_function(regression_parameter_function: function) -> None:
    print(regression_parameter_function)
    for file_name in DATA_FILES:
        benchmark_function_on_file(file_name, regression_parameter_function)


def benchmark_function_on_file(file_name: str, regression_parameter_function: function) -> None:
    """Benchmark the given regression parameter function on the given file. Returns average execution time in seconds."""
    print(file_name, timeit.timeit(lambda: regression_parameter_function(file_name), number=1000))


def calculate_norm(x: npt.NDArray[np.float64], u: npt.NDArray[np.float64]) -> np.float64:
    """Calculate the norm of the given array."""
    h = x[1] - x[0]
    return np.sqrt(h) * np.linalg.norm(u)


def main():
    """Run the main program."""
    # for uppgift in (uppgift_a, uppgift_b, uppgift_c):
    #     for file_name in DATA_FILES:
    #         read_and_plot(file_name, uppgift)
    # uppgift_4()
    # uppgift_5()
    uppgift_6()


if __name__ == "__main__":
    main()

