#%%
"""Lab 2

This laboration mainly concerns two thing:

1. Being able to look at functions that are already defined, and to be
able to use them effectively. Most of the time, you will not have to
write functions from scratch, but use already predefined function.
Being able to understand how a function is called, what the input
parameters are and what the expected output is, is important.
2. To define a couple of functions that calculate the average and moving
average of a list containing numerical values. This is mainly done by
using some builtin commands on lists, and some indexing of lists
together with iteration.

The two functions provided are ready to be used and are *not* meant to
be modified. However, many of the things that will come up in the next
lab are also used in these functions, so it is worth looking at them
(if you are interested).

The solar irradiance data is taken from:
https://ngdc.noaa.gov/stp/solar/solarirrad.html

"""

# ------------------- Predefined section
# You don't have to read this carefully

# this is the most widely used plotting library in python. you don't
# have to understand this statement right now
import matplotlib.pyplot as plt


plt.style.use('dark_background')


def get_irradiance_data(file_name='solar_irradiance.dat', set_nan_to_none=True):
    """Reads in and returns irradiance data.

    Reads in the time (day) at which the measuerment is taken and the
    value of the measurement and returns these as lists of numerical
    values.

    For this function to work, the data file:
    solar_irradiance.dat
    must be located in the same directory that this function is called
    from.

    The raw data can be found at:
    https://ngdc.noaa.gov/stp/solar/solarirrad.html
    in the Total Solar irradiance Composite Database. Taken from the file:
    ftp://ftp.ngdc.noaa.gov/STP/SOLAR_DATA/SOLAR_IRRADIANCE/composite_d25_07_0310a.dat


    Parameters
    ----------
    file_name : str, opt
        A string providing the full (relative) path to the file to be read in.
        Default is 'solar_irradiance.dat', which will try to read the
        data from a file in the same directory.
    set_nan_to_none : bool, opt
        If True (default) replaces the NaN values in the data
        (specified as -99) with None. If False, ignores the data
        points with NaN values, i.e., they are not read.

    Returns
    -------
    time: list
        The time at which the measurement is taken, given as  YYMMDD.
    time_epoch: list
        The time at which the measurement is taken, given as day of
        epoch 0 Jan 1980 (1 corresponds to 1-Jan-1980).
    solar_irradiance: list
        The measurements of daily solar irradiance, given as W/m^2.
    """
    # define lists to hold values
    time = []
    time_epoch = []
    solar_irradiance = []
    # open file and read row by row
    with open(file_name, 'r') as f:
        for line in f:
            row_values = line.split()
            # remove non measurements (NaN)
            si = float(row_values[2])  # solar irradiance value
            if si == -99 and not set_nan_to_none:
                continue
            elif si == -99:
                # assumes that set_nan_to_none == True
                si = None
            time.append(int(row_values[0]))
            time_epoch.append(float(row_values[1]))
            solar_irradiance.append(si)
    return time, time_epoch, solar_irradiance

print(get_irradiance_data('solar_irradiance.dat'))

def plot_irradiance(time_epoch, solar_irradiance,
                    marker_style='bo', label=None):
    """Plots the irradiance series over time, with x-axis labels as
    years.

    Parameters
    ----------
    time_epoch: list
        Time series given in epoch 0 standard.
    solar_irradiance: list
        Solar irradiance measurements corresponding to `time_epoch`.
    marker_style: str, optional
        String that specifies the marker and color to be plotted.
        Default format string is 'bo'. For the available choices of
        the format strings, see the documentation for
        matplotlib.pyplot.plot or alternatively the notes below.
    label: str, optional
        String that specifies the label of the series, see documentation for
        matplotlib.pyplot.plot. Default is None.

    ... notes::
        The following documetion is taken from matplotlib.pyplot.plot:

        **Format Strings**

        A format string consists of a part for color, marker and line::

            fmt = '[marker][line][color]'

        Each of them is optional. If not provided, the value from the style
        cycle is used. Exception: If ``line`` is given, but no ``marker``,
        the data will be a line without markers.

        Other combinations such as ``[color][marker][line]`` are also
        supported, but note that their parsing may be ambiguous.

        **Markers**

        =============    ===============================
        character        description
        =============    ===============================
        ``'.'``          point marker
        ``','``          pixel marker
        ``'o'``          circle marker
        ``'v'``          triangle_down marker
        ``'^'``          triangle_up marker
        ``'<'``          triangle_left marker
        ``'>'``          triangle_right marker
        ``'1'``          tri_down marker
        ``'2'``          tri_up marker
        ``'3'``          tri_left marker
        ``'4'``          tri_right marker
        ``'s'``          square marker
        ``'p'``          pentagon marker
        ``'*'``          star marker
        ``'h'``          hexagon1 marker
        ``'H'``          hexagon2 marker
        ``'+'``          plus marker
        ``'x'``          x marker
        ``'D'``          diamond marker
        ``'d'``          thin_diamond marker
        ``'|'``          vline marker
        ``'_'``          hline marker
        =============    ===============================

        **Line Styles**

        =============    ===============================
        character        description
        =============    ===============================
        ``'-'``          solid line style
        ``'--'``         dashed line style
        ``'-.'``         dash-dot line style
        ``':'``          dotted line style
        =============    ===============================

        Example format strings::

            'b'    # blue markers with default shape
            'or'   # red circles
            '-g'   # green solid line
            '--'   # dashed line with default color
            '^k:'  # black triangle_up markers connected by a dotted line

        **Colors**

        The supported color abbreviations are the single letter codes

        =============    ===============================
        character        color
        =============    ===============================
        ``'b'``          blue
        ``'g'``          green
        ``'r'``          red
        ``'c'``          cyan
        ``'m'``          magenta
        ``'y'``          yellow
        ``'k'``          black
        ``'w'``          white
        =============    ===============================
    """
    plt.plot(time_epoch, solar_irradiance, marker_style, label=label)
    # make better ticks on x-axis, corresponding to year.
    # Note: this does *not* take into account leap years, and is
    # therefore a bit ad-hoc/approximate. Ok for visual purposes.
    # start from the minimum year of the time series, and
    # end at the maxi year of the time series
    span_years = range(int(min(time_epoch)//365),
                       int(max(time_epoch)//365) + 1)
    tick_values = [i*365 for i in span_years]
    tick_labels = [str(1980 + i) for i in span_years]
    plt.xticks(tick_values, tick_labels)
    plt.xlabel('Year')
    plt.ylabel('$W/m^2$')
    if label:
        plt.legend()
    plt.title('Solar irradiance ({}-{})'.format(
        tick_labels[0], tick_labels[-1]))
    plt.xticks(rotation=45)

# ----------- Lab 2 starts here for students ----------------

#
# 1. Solve Uppgift 1 according to the PDF instructions.
#
def myfraction(x, y):
    if y == 0:
        return None

    return x/y

#
# 2. Solve Uppgift 2 according to the PDF instructions.
#
def list_remove_none(input_list):
    """Return a copy of the given list with `None` values removed."""
    return list(filter(lambda x: x is not None, input_list))

# 3. Use the provided functions to read in the data into variables (of
# your choice), and plot the data.
# After calling `plot_irradiance`, you must call plt.show() to see the plot.
def read_and_show_data():
    """Read in the solar irradiance data from the file and show it in a plot."""
    time, time_epoch, solar_irradiance = get_irradiance_data()
    plot_irradiance(time_epoch, solar_irradiance, marker_style="x", label="Daily")
    plt.show()


read_and_show_data()


# 4.
# Define a function that calculates the average of a list of numerical
# values with possible Nones included
def average(input_list):
    """Return the mean average of the given list.

    `None` values are ignored.
    """
    input_list = list_remove_none(input_list)

    if not input_list:
        return None

    return sum(input_list)/len(input_list)

# 5.
# Define a function that calculates the moving average of a list of
# numerical values (with possible Nones included). The moving average
# should be able to be calculated with a specified `window_size`
# parameter, where `window_size = 0` specifies that no average is
# taken, only the point considered. A larger window size > n (integer)
# should calculate the average of the list of size 2*n + 1 centered
# around the considered point.
# BEWARE OF THE END POINTS!
# if a window size is such that it extends beyond the end points of
# the list, only take into account the point that actually are in the
# list.
# Example:
# > d = [0, 2, 3, 4, 6, 8, 12]
# > moving_average(d, window_size=3)
# > [2.25, 3.0, 3.8333333333333335, 5.0, 5.833333333333333, 6.6, 7.5]
# This is calculated by:
# [average(d[0:4]), average(d[0:5]), average(d[0:6]), average(d[0:7]),
#  average(d[1:7]), average(d[2:7]), average(d[3:7])]
def moving_average(input_list, window_size=0):
    """Return the moving average of the given input_list with the given window_size."""
    moving_averages = []
    for i in range(len(input_list)):
        start_index = max(i - window_size, 0)
        end_index = min(i + window_size + 1, len(input_list))
        moving_averages.append(average(input_list[start_index:end_index]))
    return moving_averages

# 6.
# Using `moving_average`, calculate the smoothed solar irradiance series for:
# - a window size of 15 (average of the series that is 15 days before to 15
#   days after the measurement, a "monthly average")
# - a window size of 45 (a "quarterly-year average").
def calculate_monthly_and_quarterly_solar_irradiance(solar_irradiance):
    """Calculate a moving average solar irradiance data month-wise and quarter-wise."""
    monthly_solar_irradiance = moving_average(solar_irradiance, 15)
    quarterly_solar_irradiance = moving_average(solar_irradiance, 45)
    return solar_irradiance, monthly_solar_irradiance, quarterly_solar_irradiance


def print_solar_irradiance():
    """Print the daily, monthly, and quarterly solar irradiance data."""
    daily, monthly, quarterly = calculate_monthly_and_quarterly_solar_irradiance(get_irradiance_data()[2])
    print(f"SERIES STATISTICS\n"
          f"Series      Mean irradiance\n"
          f"Daily       {average(daily):.8f}\n"
          f"Monthly     {average(monthly):.8f}\n"
          f"Quarterly   {average(quarterly):.8f}\n")


print_solar_irradiance()


def plot_solar_irradiance():
    """Plot the daily, monthly, and quarterly solar irradiance data."""
    _, time_epoch, solar_irradiance = get_irradiance_data()
    daily, monthly, quarterly = calculate_monthly_and_quarterly_solar_irradiance(solar_irradiance)
    plot_irradiance(time_epoch, daily, label="Daily")
    plot_irradiance(time_epoch, monthly, label="Monthly", marker_style="-r")
    plot_irradiance(time_epoch, quarterly, label="Quarterly", marker_style="-g")
    plt.show()


plot_solar_irradiance()

# 7.
# plot the data using `plot_irradiance`. Plot both daily values and
# the values calculated in 4. Use appropriate labels for the moving
# average by specifying the keyword parameter `labels`, and use unique
# symbol markers (e.g. blue dots, red line, green line) for the
# different data sets.
# after calling the function for each data set, show the plot with plt.show()
# plotting
