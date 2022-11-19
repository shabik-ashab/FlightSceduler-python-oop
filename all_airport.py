import csv
from airport import Airport


class AllAirports:
    def __init__(self) -> None:
        self.load_airport_data('./data/airport.csv')
        self.airports = None

    def load_airport_data(self, file_path):
        airports = {}
        with open(file_path, 'r' ,encoding="utf8") as file:
            lines = csv.reader(file)

            for line in lines:
                airports[line[4]] = Airport(line[4], line[1], line[3], line[2], line[6], line[7], 0)

            self.airports = airports
            for airport in airports.items():
                print(airport)


AllAirports()