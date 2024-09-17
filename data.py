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

    def get_delayed_flights(self):
        """
        Retrieves flights delayed by 20 minutes or more.
        """
        query = """
        SELECT id, year, month, day, origin_airport, destination_airport, departure_delay
        FROM flights
        WHERE departure_delay >= 20
        """
        return self._execute_query(query)

    def __del__(self):
        """
        Closes the connection to the databse when the object is about to be destroyed
        """
        self._engine.dispose()
