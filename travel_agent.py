from itertools import permutations

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

    def trip_one_city_round(self, start, end, start_date):
        trip1 = self.trip_one_city_one_way(start, end, start_date)
        trip2 = self.trip_one_city_one_way(end, start, start_date)
        return [trip1, trip2]

    def trip_two_city_one_way(self, trip_cities, start_date):
        trip1 = self.trip_one_city_one_way(trip_cities[0], trip_cities[1], start_date)
        trip2 = self.trip_one_city_one_way(trip_cities[1], trip_cities[2], start_date)
        return [trip1, trip2]

    def trip_two_city_two_way(self):
        pass

    def trip_multi_city_one_way_fix(self, trip_cities, start_date):
        trips = []
        for i in range(0, len(trip_cities) - 1):
            trip = self.trip_one_city_one_way(trip_cities[i], trip_cities[i+1], start_date)
            trips.append(trip)
        return trips

    def trip_multi_city_one_way_flexible(self, trip_cities, start_date):
        start_city = trip_cities[0]
        flexible_cities = trip_cities[1:]

        min_price = float('inf')
        selected_trips = None
        for sequence in permutations(flexible_cities):
            fixed_routes = [start_city] + list(sequence)
            fixed_routes_trips = self.trip_multi_city_one_way_fix(fixed_routes, start_date)
            price = 0
            for trip in fixed_routes_trips:
                price += trip.price
            if price < min_price:
                min_price = price
                selected_trips = fixed_routes_trips
        
        return selected_trips, min_price



    def __repr__(self) -> str:
        return f"TravelAgent: {self.name} "