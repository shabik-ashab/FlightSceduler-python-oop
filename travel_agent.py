from all_airport import AllAirports
from airlines import Airlines
from trip import Trip


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
        trip = Trip([start,end], aircraft, price, start_date)
        return trip

    def trip_one_city_two_way(self):
        pass

    def trip_two_city_one_way(self, trip_info, start_date1, start_date):
        trip1 = self.trip_one_city_one_way(trip_info[0], trip_info[1], start_date)
        trip2 = self.trip_one_city_one_way(trip_info[1], trip_info[2], start_date)
        return [trip1, trip2]


    def trip_two_city_two_way(self):
        pass

    def trip_multi_city_one_way_fix_round(self, trip_info, start_date):
        trips = []
        for i in range(0, len(trip_info) - 1):
            trip = self.trip_one_city_one_way(trip_info[i], trip_info[i+1], start_date)
            trips.append(trip)
        return trips


    def __repr__(self) -> str:
        return f"TravelAgent: {self.name} "