import data
from datetime import datetime
import sqlalchemy
from matplotlib import pyplot as plt
import numpy as np


SQLITE_URI = "sqlite:///data/flights.sqlite3"
IATA_LENGTH = 3


def percentage_delayed_flights_by_airline(data_manager: data.FlightData):
    # Get the data from the data.py class method
    airlines_data = data_manager.get_delayed_flights_percentage_by_airline()

    # Prepare data for plotting
    airlines = [row[0] for row in airlines_data]  # Airline names
    percentages = [
        (row[2] / row[1]) * 100 if row[1] > 0 else 0 for row in airlines_data
    ]  # Calculate percentage of delayed flights

    # Plot the data using matplotlib
    plt.figure(figsize=(10, 6))
    plt.bar(airlines, percentages)
    plt.xticks(rotation=45, ha="right")
    plt.xlabel("Airline")
    plt.ylabel("Percentage of Delayed Flights")
    plt.title("Percentage of Delayed Flights by Airline")
    plt.tight_layout()
    plt.show()


def percentage_delayed_flights_by_hour(data_manager: data.FlightData):
    # Get the data from the data.py class method
    hour_data = data_manager.get_delayed_flights_percentage_by_hour()

    # Prepare data for plotting, handling hours extracted from string
    hours = []
    percentages = []

    for row in hour_data:
        hour_str = row[0]  # The hour is a string in the format '00', '01', '12', etc.
        total_flights = row[1]
        delayed_flights = row[2]

        if (
            hour_str is not None and hour_str.isdigit()
        ):  # Only include valid hour strings
            hour = int(hour_str)  # Convert the hour string to an integer
            hours.append(hour)
            percentages.append(
                (delayed_flights / total_flights) * 100 if total_flights > 0 else 0
            )

    # Create a figure and axes for the plot
    fig, ax = plt.subplots(figsize=(10, 6))

    # Create a color map based on the percentage values
    cmap = plt.cm.viridis
    norm = plt.Normalize(
        vmin=min(percentages), vmax=max(percentages)
    )  # Normalize colors based on percentages
    colors = cmap(norm(percentages))

    # Create the bar chart
    bars = ax.bar(hours, percentages, color=colors)
    ax.set_xlabel("Hour of Day")
    ax.set_ylabel("Percentage of Delayed Flights")
    ax.set_title("Percentage of Delayed Flights by Hour of Day")

    # Add color bar on the side
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])  # Needed to avoid errors
    cbar = fig.colorbar(
        sm, ax=ax
    )  # Now explicitly link the colorbar to the figure/axes
    cbar.set_label("Percentage of Delayed Flights")

    plt.tight_layout()
    plt.show()
    # Get the data from the data.py class method
    hour_data = data_manager.get_delayed_flights_percentage_by_hour()

    # Prepare data for plotting, handling hours extracted from string
    hours = []
    percentages = []

    for row in hour_data:
        hour_str = row[0]  # The hour is a string in the format '00', '01', '12', etc.
        total_flights = row[1]
        delayed_flights = row[2]

        if (
            hour_str is not None and hour_str.isdigit()
        ):  # Only include valid hour strings
            hour = int(hour_str)  # Convert the hour string to an integer
            hours.append(hour)
            percentages.append(
                (delayed_flights / total_flights) * 100 if total_flights > 0 else 0
            )

    # Plot the data using matplotlib
    plt.figure(figsize=(10, 6))

    # Create a color map based on the percentage values
    cmap = plt.cm.viridis
    norm = plt.Normalize(
        vmin=min(percentages), vmax=max(percentages)
    )  # Normalize colors based on percentages
    colors = cmap(norm(percentages))

    # Create the bar chart
    bars = plt.bar(hours, percentages, color=colors)
    plt.xlabel("Hour of Day")
    plt.ylabel("Percentage of Delayed Flights")
    plt.title("Percentage of Delayed Flights by Hour of Day")

    # Add color bar on the side
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])  # Needed to avoid errors
    plt.colorbar(sm, label="Percentage of Delayed Flights")  # Add color bar to the plot

    plt.tight_layout()
    plt.show()
    # Get the data from the data.py class method
    hour_data = data_manager.get_delayed_flights_percentage_by_hour()

    # Prepare data for plotting, handling hours extracted from string
    hours = []
    percentages = []

    for row in hour_data:
        hour_str = row[0]  # The hour is a string in the format '00', '01', '12', etc.
        total_flights = row[1]
        delayed_flights = row[2]

        if (
            hour_str is not None and hour_str.isdigit()
        ):  # Only include valid hour strings
            hour = int(hour_str)  # Convert the hour string to an integer
            hours.append(hour)
            percentages.append(
                (delayed_flights / total_flights) * 100 if total_flights > 0 else 0
            )

    # Plot the data using matplotlib
    plt.figure(figsize=(10, 6))

    # Create a color map based on the percentage values
    colors = plt.cm.viridis(np.linspace(0, 1, len(hours)))

    plt.bar(hours, percentages, color=colors)
    plt.xlabel("Hour of Day")
    plt.ylabel("Percentage of Delayed Flights")
    plt.title("Percentage of Delayed Flights by Hour of Day")

    plt.tight_layout()
    plt.show()
    # Get the data from the data.py class method
    hour_data = data_manager.get_delayed_flights_percentage_by_hour()

    # Prepare data for plotting, handling hours extracted from string
    hours = []
    percentages = []

    for row in hour_data:
        hour_str = row[0]  # The hour is a string in the format '00', '01', '12', etc.
        total_flights = row[1]
        delayed_flights = row[2]

        if (
            hour_str is not None and hour_str.isdigit()
        ):  # Only include valid hour strings
            hour = int(hour_str)  # Convert the hour string to an integer
            hours.append(hour)
            percentages.append(
                (delayed_flights / total_flights) * 100 if total_flights > 0 else 0
            )

    # Plot the data using matplotlib
    plt.figure(figsize=(10, 6))

    # Create a color map based on the percentage values
    colors = plt.cm.viridis(np.linspace(0, 1, len(hours)))

    plt.bar(hours, percentages, color=colors)
    plt.xlabel("Hour of Day")
    plt.ylabel("Percentage of Delayed Flights")
    plt.title("Percentage of Delayed Flights by Hour of Day")

    # Add color bar for visual effect
    sm = plt.cm.ScalarMappable(
        cmap="viridis", norm=plt.Normalize(vmin=min(percentages), vmax=max(percentages))
    )
    sm.set_array([])  # Only needed for the color bar
    plt.colorbar(sm, label="Percentage of Delayed Flights")

    plt.tight_layout()
    plt.show()
    # Get the data from the data.py class method
    hour_data = data_manager.get_delayed_flights_percentage_by_hour()
    print(hour_data)
    # Prepare data for plotting
    hours = [int(row[0]) for row in hour_data]  # Convert hour string to int
    percentages = [
        (row[2] / row[1]) * 100 if row[1] > 0 else 0 for row in hour_data
    ]  # Calculate percentage of delayed flights

    # Plot the data using matplotlib
    plt.figure(figsize=(10, 6))

    # Create a color map based on the percentage values
    colors = plt.cm.viridis(np.linspace(0, 1, len(hours)))

    plt.bar(hours, percentages, color=colors)
    plt.xlabel("Hour of Day")
    plt.ylabel("Percentage of Delayed Flights")
    plt.title("Percentage of Delayed Flights by Hour of Day")

    # Add color bar for visual effect
    sm = plt.cm.ScalarMappable(
        cmap="viridis", norm=plt.Normalize(vmin=min(percentages), vmax=max(percentages))
    )
    sm.set_array([])  # Only needed for the color bar
    plt.colorbar(sm, label="Percentage of Delayed Flights")

    plt.tight_layout()
    plt.show()


def delayed_flights_by_airline(data_manager):
    """
    Asks the user for a textual airline name (any string will work here).
    Then runs the query using the data object method "get_delayed_flights_by_airline".
    When results are back, calls "print_results" to show them to on the screen.
    """
    airline_input = input("Enter airline name: ")
    results = data_manager.get_delayed_flights_by_airline(airline_input)
    print_results(results)


def delayed_flights_by_airport(data_manager: data.FlightData):
    """
    Asks the user for a textual IATA 3-letter airport code (loops until input is valid).
    Then runs the query using the data object method "get_delayed_flights_by_airport".
    When results are back, calls "print_results" to show them to on the screen.
    """
    valid = False
    while not valid:
        airport_input = input("Enter origin airport IATA code: ")
        # Valide input
        if airport_input.isalpha() and len(airport_input) == IATA_LENGTH:
            valid = True
    results = data_manager.get_delayed_flights_by_airport(airport_input)
    print_results(results)


def flight_by_id(data_manager: data.FlightData):
    """
    Asks the user for a numeric flight ID,
    Then runs the query using the data object method "get_flight_by_id".
    When results are back, calls "print_results" to show them to on the screen.
    """
    valid = False
    while not valid:
        try:
            id_input = int(input("Enter flight ID: "))
        except Exception as e:
            print("Try again...")
        else:
            valid = True
    results = data_manager.get_flight_by_id(id_input)
    print_results(results)


def flights_by_date(data_manager: data.FlightData):
    """
    Asks the user for date input (and loops until it's valid),
    Then runs the query using the data object method "get_flights_by_date".
    When results are back, calls "print_results" to show them to on the screen.
    """
    valid = False
    while not valid:
        try:
            date_input = input("Enter date in DD/MM/YYYY format: ")
            date = datetime.strptime(date_input, "%d/%m/%Y")
        except ValueError as e:
            print("Try again...", e)
        else:
            valid = True
    results = data_manager.get_flights_by_date(date.day, date.month, date.year)
    print_results(results)


def print_results(results):
    """
    Get a list of flight results (List of dictionary-like objects from SQLAachemy).
    Even if there is one result, it should be provided in a list.
    Each object *has* to contain the columns:
    FLIGHT_ID, ORIGIN_AIRPORT, DESTINATION_AIRPORT, AIRLINE, and DELAY.
    """
    print(f"Got {len(results)} results.")
    for result in results:
        # turn result into dictionary
        result = result._mapping

        # Check that all required columns are in place
        try:
            delay = (
                int(result["DELAY"]) if result["DELAY"] else 0
            )  # If delay columns is NULL, set it to 0
            origin = result["ORIGIN_AIRPORT"]
            dest = result["DESTINATION_AIRPORT"]
            airline = result["AIRLINE"]
        except (ValueError, sqlalchemy.exc.SQLAlchemyError) as e:
            print("Error showing results: ", e)
            return

        # Different prints for delayed and non-delayed flights
        if delay and delay > 0:
            print(
                f"{result['ID']}. {origin} -> {dest} by {airline}, Delay: {delay} Minutes"
            )
        else:
            print(f"{result['ID']}. {origin} -> {dest} by {airline}")


def show_menu_and_get_input():
    """
    Show the menu and get user input.
    If it's a valid option, return a pointer to the function to execute.
    Otherwise, keep asking the user for input.
    """
    print("Menu:")
    for key, value in FUNCTIONS.items():
        print(f"{key}. {value[1]}")

    # Input loop
    while True:
        try:
            choice = int(input())
            if choice in FUNCTIONS:
                return FUNCTIONS[choice][0]
        except ValueError as e:
            pass
        print("Try again...")


"""
Function Dispatch Dictionary
"""
FUNCTIONS = {
    1: (flight_by_id, "Show flight by ID"),
    2: (flights_by_date, "Show flights by date"),
    3: (delayed_flights_by_airline, "Delayed flights by airline"),
    4: (delayed_flights_by_airport, "Delayed flights by origin airport"),
    5: (
        percentage_delayed_flights_by_airline,
        "Percentage of delayed flights by airline",
    ),
    6: (
        percentage_delayed_flights_by_hour,
        "Percentage of delayed flights by hour of day",
    ),  # Add this line
    7: (quit, "Exit"),
}


def main():
    # Create an instance of the Data Object using our SQLite URI
    data_manager = data.FlightData(SQLITE_URI)

    # The Main Menu loop
    while True:
        choice_func = show_menu_and_get_input()
        choice_func(data_manager)


if __name__ == "__main__":
    main()
