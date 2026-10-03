"""Module containing code for benchmarking linear regression functions.

Includes the code for uppgift 4.
"""
import timeit

from regression import uppgift_a, uppgift_b, uppgift_c


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

    SciPy was certainly easiest to write.
    """
    _benchmark_function(uppgift_a)
    _benchmark_function(uppgift_b)
    _benchmark_function(uppgift_c)


def _benchmark_function(regression_parameter_function) -> None:
    print(regression_parameter_function)
    for file_name in DATA_FILES:
        _benchmark_function_on_file(file_name, regression_parameter_function)


def _benchmark_function_on_file(file_name: str, regression_parameter_function) -> None:
    """Benchmark the given regression parameter function on the given file. Returns average execution time in seconds."""
    print(file_name, timeit.timeit(lambda: regression_parameter_function(file_name), number=1000))
