"""Module containing code for calculating Helmholtz solutions.

Includes code for uppgifter 5-6.
"""
from matplotlib import pyplot as plt
import numpy as np
import numpy.typing as npt

from helmholtz_fd import solve_helmholtz
from regression import calculate_regression_parameters_scipy, plot_regression


plt.style.use("dark_background")


def uppgift_5() -> None:
    """Code for Uppgift 5.

    Iterates through different wave number values and plots the real part of
    the Helmholtz solution against the corresponding x value.
    """
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
        _x, _u, norm = solve_helmholtz(k)
        norms.append(norm)

    plt.title("Plot of scaled L2 norm as a function of wavenumber k")
    plot_regression(ks, norms, *calculate_regression_parameters_scipy(ks, norms), xlabel="k", ylabel="norm")


def calculate_norm(x: npt.NDArray[np.float64], u: npt.NDArray[np.float64]) -> np.float64:
    """Calculate the scaled L2 norm of the given helmholtz solution data.

    The parameters x, u should be numpy arrays from the helmholtz_fd.solve_helmholtz function.
    """
    h = x[1] - x[0]
    return np.sqrt(h) * np.linalg.norm(u)
