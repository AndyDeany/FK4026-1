"""Lösningen för labb 3."""
import matplotlib.pyplot as plt


plt.style.use("dark_background")


WEATHER_DATA_FILE_NAME = "stockholm_daily_mean_temp.txt"


def read_weather_data() -> dict:
    """Read in the weather data and return a dictionary containing its data."""
    year = []
    month = []
    day = []
    temp = []
    with open(WEATHER_DATA_FILE_NAME, "r") as file:
        for line in file.readlines():
            items = line.split()
            year.append(int(items[0]))
            month.append(int(items[1]))
            day.append(int(items[2]))
            if items[3] == "-999.0":
                temp.append(None)
            else:
                temp.append(float(items[3]))

    return {
        "year": year,
        "month": month,
        "day": day,
        "temp": temp,
    }


def plot_temp_vs_days() -> None:
    """Plot the temperature against the number of days since first measurement."""
    temps = read_weather_data()["temp"]
    label = "Data for average daily temperature in Stockholm"
    plt.plot(range(len(temps)), temps, label=label)
    plt.xlabel("Number of days from Jan 1st, 1756")
    plt.ylabel("Temperature (Celcius)")
    plt.title(label)
    plt.show()


plot_temp_vs_days()


def get_period_indices(start: str, end: str, data: dict) -> tuple[int | None, int | None]:
    """Return the start and end indices encapsulating data belonging to the given date range."""
    start_year, start_month, start_day = map(int, start.split("-"))
    end_year, end_month, end_day = map(int, end.split("-"))

    for index in range(len(data["temp"])):
        year, month, day = data["year"][index], data["month"][index], data["day"][index]
        if year < start_year:
            continue
        if year > start_year:
            start_index = index
            break

        if month < start_month:
            continue
        if month > start_month:
            start_index = index
            break

        if day < start_day:
            continue

        start_index = index
        break
    else:
        return None, None   # No valid range

    for index in reversed(range(len(data["temp"]))):
        year, month, day = data["year"][index], data["month"][index], data["day"][index]
        if year > end_year:
            continue
        if year < end_year:
            end_index = index
            break

        if month > end_month:
            continue
        if month < end_month:
            end_index = index
            break

        if day > end_day:
            continue

        end_index = index
        break
    else:
        return None, None   # No valid range

    return start_index, end_index


def make_temp_hist(data):
    occurrences = {}
    for temp in data["temp"]:
        occurrences[temp] = occurrences.get(temp, 0) + 1

    return occurrences


def plot_temp_histogram():
    """Plot a histogram of the frequencies of different temperature values."""
    occurrences = make_temp_hist(read_weather_data())
    plt.plot(occurrences.keys(), occurrences.values(), "bo")
    plt.xlabel("Temperature (0.1°C bins)")
    plt.ylabel("Number of measurements")
    plt.title("Temperature distribution/histogram in Stockholm")
    plt.show()


plot_temp_histogram()
