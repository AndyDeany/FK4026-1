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
    return input("Which data file? ")


def read_data_from_sample_file(file_name: str) -> dict[int, DataPoint]:
    """Read and return the data from the sample file with the given name."""
    data = {}

    with open(file_name, "r") as file:
        for line in file:
            line_data = list(map(lambda d: d.strip(), line.split(",")))
            batch_number = int(line_data[0])
            data_point = DataPoint(float(line_data[1]), float(line_data[2]), float(line_data[3]))
            data.setdefault(batch_number, []).append(data_point)

    return data


def calculate_average(batch: list[DataPoint]) -> float:
    """Calculate the average of the valid data points in given batch."""
    valid_values = [data_point.value for data_point in batch if data_point.is_valid]
    return sum(valid_values) / len(valid_values)


def print_batch_averages(data) -> None:
    """Print averages of all batches in the given data."""
    for batch_number, batch in data.items():
        print(f"{batch_number} \t {calculate_average(batch)}")


def main():
    """Run the main program."""
    file_name = get_file_name_from_user()
    data = read_data_from_sample_file(file_name)
    print_batch_averages(data)


if __name__ == "__main__":
    main()
