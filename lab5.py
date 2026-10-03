"""Module containing solutions for labb 5."""
from benchmarking import uppgift_4, DATA_FILES
from physics import uppgift_5, uppgift_6
from regression import (uppgift_a, uppgift_b, uppgift_c,
                        read_file, plot_regression)


def read_and_plot(data_file: str, regression_parameter_function) -> None:
    """Plot the data from the given file along with its linear regression line.

    data_file:
        Name of the file to read data points from.
        Each line of the file should contain two values separated by a tab.
    regression_parameter_function:
        Function to use for calculating linear regression coefficients.
        It should have the signature regression_parameter_function(file_name) -> alpha, beta.
    """
    alpha, beta = regression_parameter_function(data_file)
    plot_regression(*read_file(data_file), alpha, beta)


def main():
    """Run the main program.

    This runs all the code for every uppgift in turn.
    """
    for uppgift in (uppgift_a, uppgift_b, uppgift_c):
        for file_name in DATA_FILES:
            read_and_plot(file_name, uppgift)
    uppgift_4()
    uppgift_5()
    uppgift_6()


if __name__ == "__main__":
    main()
