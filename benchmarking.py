"""Module containing code for benchmarking linear regression functions.

Includes the code for uppgift 4.
"""
import timeit


DATA_FILES = ("small.txt", "medium.txt", "large.txt")


def _benchmark_function(regression_parameter_function) -> None:
    print(regression_parameter_function)
    for file_name in DATA_FILES:
        benchmark_function_on_file(file_name, regression_parameter_function)


def benchmark_function_on_file(file_name: str, regression_parameter_function) -> None:
    """Benchmark the given regression parameter function on the given file. Returns average execution time in seconds."""
    print(file_name, timeit.timeit(lambda: regression_parameter_function(file_name), number=1000))
