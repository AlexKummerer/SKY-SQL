from sqlalchemy import create_engine, text

QUERY_FLIGHT_BY_ID = "SELECT flights.*, airlines.airline, flights.ID as FLIGHT_ID, flights.DEPARTURE_DELAY as DELAY FROM flights JOIN airlines ON flights.airline = airlines.id WHERE flights.ID = :id"


class FlightData:
    """
    The FlightData class is a Data Access Layer (DAL) object that provides an
    interface to the flight data in the SQLITE database. When the object is created,
    the class forms connection to the sqlite database file, which remains active
    until the object is destroyed.
    """

    def __init__(self, db_uri):
        """
        Initialize a new engine using the given database URI
        """
        self._engine = create_engine(db_uri)

    def _execute_query(self, query, params=()):
        """
        Executes a query and returns the result using SQLAlchemy.
        :param query: The SQL query to be executed.
        :param params: The parameters to be used in the query.
        :return: Query result as a list of dictionaries.
        """
        with self._engine.connect() as connection:
            result = connection.execute(text(query), params)
            # print(result.fetchall())
            return result.fetchall()

    def get_flight_by_id(self, flight_id):
        QUERY_FLIGHT_BY_ID = """
        SELECT f.id, f.year, f.month, f.day, f.origin_airport, f.destination_airport, f.departure_delay AS DELAY, a.airline
        FROM flights f
        JOIN airlines a ON f.airline = a.id
        WHERE f.id = :flight_id
        """
        params = {"flight_id": flight_id}
        return self._execute_query(QUERY_FLIGHT_BY_ID, params)

    def get_flights_by_date(self, day, month, year):
        """
        Retrieves flights for a given date.
        """
        query = """
        SELECT f.id, f.year, f.month, f.day, f.origin_airport, f.destination_airport, f.departure_delay AS DELAY, a.airline
        FROM flights f
        JOIN airlines a ON f.airline = a.id
        WHERE f.day = :day AND f.month = :month AND f.year = :year
        """
        params = {"day": day, "month": month, "year": year}
        return self._execute_query(query, params)

    def get_delayed_flights_by_airport(self, airport):
        """
        Retrieves delayed flights for a given airport.
        """
        query = """
        SELECT f.id, f.year, f.month, f.day, f.origin_airport, f.destination_airport, f.departure_delay AS DELAY, a.airline
        FROM flights f
        JOIN airlines a ON f.airline = a.id
        WHERE f.origin_airport = :airport AND f.departure_delay > 0
        """
        params = {"airport": airport}
        return self._execute_query(query, params)

    def get_delayed_flights_by_airline(self, airline):
        """
        Retrieves delayed flights for a given airline.
        """
        query = """
        SELECT f.id, f.year, f.month, f.day, f.origin_airport, f.destination_airport, f.departure_delay AS DELAY, a.airline
        FROM flights f
        JOIN airlines a ON f.airline = a.id
        WHERE a.airline = :airline AND f.departure_delay > 0
        """
        params = {"airline": airline}
        return self._execute_query(query, params)

    def get_delayed_flights_percentage_by_airline(self):
        """
        Retrieves the percentage of delayed flights for each airline.
        :return: A list of dictionaries with airline names and percentage of delayed flights.
        """
        query = """
        SELECT a.airline, 
               COUNT(f.id) AS total_flights, 
               SUM(CASE WHEN f.departure_delay > 0 THEN 1 ELSE 0 END) AS delayed_flights
        FROM flights f
        JOIN airlines a ON f.airline = a.id
        GROUP BY a.airline
        """

        results = self._execute_query(query)

        return results

    def get_delayed_flights_percentage_by_hour(self):
        """
        Retrieves the percentage of delayed flights for each hour of the day.
        :return: A list of tuples (hour, total_flights, delayed_flights)
        """
        query = """
        SELECT SUBSTR(f.departure_time, 1, 2) AS hour_of_day,
               COUNT(f.id) AS total_flights,
               SUM(CASE WHEN f.departure_delay > 0 THEN 1 ELSE 0 END) AS delayed_flights
        FROM flights f
        WHERE f.departure_time IS NOT NULL  -- Filter out NULL departure_time
        GROUP BY hour_of_day
        ORDER BY hour_of_day
        """

        # Execute the query and return the raw results as tuples
        results = self._execute_query(query)
        print(results)
        return results  # Return the list of tuples

    def __del__(self):
        """
        Closes the connection to the databse when the object is about to be destroyed
        """
        self._engine.dispose()
