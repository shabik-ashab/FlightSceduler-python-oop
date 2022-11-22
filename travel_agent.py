from all_airport import AllAirports
from airlines import Airlines


class TravelAgent:
    def __init__(self, name) -> None:
        self.name = name
        self.trips = None 
        self.all_airports = AllAirports()
        self.airlines = Airlines()

    def trip_one_city_one_way(self, start, end, start_date):
        price = self.all_airports.ticket_price(start, end)
        distance = self.all_airports.distance_between_two_airports(start, end)
        aircraft = self.airlines.get_aircraft_by_distance(distance)
        return [aircraft, price]

    def trip_one_city_two_way(self):
        pass

    def trip_two_city_one_way(self):
        pass

    def trip_two_city_two_way(self):
        pass

    def trip_multi_city_round(self):
        pass


    def __repr__(self) -> str:
        return f"TravelAgent: {self.name} "