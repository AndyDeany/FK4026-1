"""Module containing solutions for labb 5."""
from matplotlib import pyplot as plt


plt.style.use("dark_background")


def uppgift_a(file_name):
    """Code for Uppgift 1."""
    x, y = read_file(file_name)
    plot_regression(x, y)


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


def calculate_regression_parameters(x: list[float], y: list[float]) -> tuple:
    """Take the given lists of x and y values and return the regression parameters."""
    n = len(x)
    s_x = sum(x)
    s_y = sum(y)
    s_xy = sum(x_value * y_value for x_value, y_value in zip(x, y))
    s_xx = sum(x_value ** 2 for x_value in x)

    beta = (n*s_xy - s_x*s_y)/(n*s_xx - s_x*s_x)
    alpha = (s_y - beta*s_x)/n

    return alpha, beta


def plot_regression(x, y):
    """Plot the given points together with their linear regression line."""
    alpha, beta = calculate_regression_parameters(x, y)
    plt.scatter(x, y, color="pink", marker="$♥$", s=50)
    plt.axline((0, alpha), slope=beta, color="#ffef5c")
    plt.show()


def main():
    """Run the main program."""
    uppgift_a("small.txt")


if __name__ == "__main__":
    main()

