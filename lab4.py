"""Module for calculating the averages of valid data points in multiple batches of data."""


class DataPoint:
    """Class for representing a single data point."""

    def __init__(self, x: float, y: float, value: float) -> None:
        self.x = x
        self.y = y
        self.value = value

    @property
    def is_valid(self) -> bool:
        return self.x**2 + self.y**2 <= 1


def get_file_name_from_user() -> str:
    """Ask the user for a file name and then return it."""
    while True:
        file_name = input("Which data file? ")
        try:    # Handle invalid file names by checking that a file with the given name exists
            open(file_name).close()
        except FileNotFoundError:
            print(f"A file with name {file_name} could not be found. Please try again.")
        else:
            break

    return file_name



def read_data_from_sample_file(file_name: str) -> dict[int, DataPoint]:
    """Read and return the data from the sample file with the given name."""
    data = {}

    with open(file_name, "r") as file:
        for line in file:
            try:    # Handle invalid lines in sample files by catching Exceptions
                batch_number, data_point = read_line(line)
            except Exception:
                print(f"\n[Warning] The following line could not be parsed:\n    {line}")
                continue

            data.setdefault(batch_number, []).append(data_point)

    return data


def read_line(line: str) -> tuple[int, DataPoint]:
    """Read and return the data from the given line string."""
    line_data = list(map(lambda d: d.strip(), line.split(",")))
    batch_number = int(line_data[0])
    data_point = DataPoint(float(line_data[1]), float(line_data[2]), float(line_data[3]))
    return batch_number, data_point


def calculate_average(batch: list[DataPoint]) -> float | None:
    """Calculate the average of the valid data points in given batch.

    Returns `None` if there are no valid data points.
    """
    valid_values = [data_point.value for data_point in batch if data_point.is_valid]
    if not valid_values:    # Avoid ZeroDivisionError when there are no valid data points
        return None
    return sum(valid_values) / len(valid_values)


def print_batch_averages(data) -> None:
    """Print averages of all batches in the given data."""
    for batch_number, batch in sorted(data.items()):
        average = calculate_average(batch)
        if average is None:     # Handle case where no data points in a batch are valid
            print(f"{batch_number} \t No valid data points")
        else:
            print(f"{batch_number} \t {average}")


def main():
    """Run the main program."""
    file_name = get_file_name_from_user()
    data = read_data_from_sample_file(file_name)
    print_batch_averages(data)


if __name__ == "__main__":
    main()
