"""Module containing solutions for labb 5."""
from benchmarking import uppgift_4, DATA_FILES
from physics import uppgift_5, uppgift_6
from regression import (uppgift_a, uppgift_b, uppgift_c,
                        read_file, plot_regression)


def read_and_plot(file_name: str, regression_parameter_function) -> None:
    """Read the given file and plot the result given data with its regression line."""
    alpha, beta = regression_parameter_function(file_name)
    plot_regression(*read_file(file_name), alpha, beta)


def main():
    """Run the main program."""
    for uppgift in (uppgift_a, uppgift_b, uppgift_c):
        for file_name in DATA_FILES:
            read_and_plot(file_name, uppgift)
    uppgift_4()
    uppgift_5()
    uppgift_6()


if __name__ == "__main__":
    main()
