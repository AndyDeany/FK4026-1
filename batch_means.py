# Sample data: 
# 1, 0.1, 0.2, 73
# 1, 0.11, 0.1, 101
# 2, 0.23, 0.01, 17
# 2, 0.12, 0.15, 23
#
# Pretend this is taken from two (or more) different experiments: batch 1 and batch 2.
import numpy as np


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

            
def old_main():
    '''
    This is the main body of the program.
    '''
    
    filename = input('Which data file? ')

    data = dict()               # Or data = {}
    with open(filename, 'r') as h:
        for line in h:
            four_vals = line.split(',')
            batch = four_vals[0]
            if not batch in data:
                data[batch] = []
            data[batch] += [(float(four_vals[1]), float(four_vals[2]), float(four_vals[3]))] # Collect data from an experiment

    for batch, sample in data.items(): 
        if len(sample) > 0:
            n = 0
            x_sum = 0
            for (x, y, val) in sample:
                if x**2 + y**2 <= 1:
                    x_sum += val
                    n += 1
            average = x_sum/n
            print(batch, "\t", average)
        else:
            print(batch, "\tNo data")

        

# Start the main program: This is idiomatic python
if __name__ == "__main__":
    main()

# The idea with this idiom is that if this code is loaded as a module,
# then the __name__ variable (internal to Python) is not __main__ and
# the body of the program is not executed. Consider what would happen
# if the main function was not in a function: an import statement (for
# example "import o4") would load the functions and then executed
# "filename = input(...)" and that is probably not what you want. The
# idiom is simply an easy way of ensuring that some code is only
# executed when run as an actual program.
#
# Try it out by importing this file into another project!
    
