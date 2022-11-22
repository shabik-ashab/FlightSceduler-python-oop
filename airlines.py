import csv
from aircraft import Aircraft


class Airlines:
    def __init__(self) -> None:
        self.air_crafts = None
        self.load_aircraft_data('./data/aircraft.csv')

    def load_aircraft_data(self, csv_file):
        air_crafts = {}
        with open(csv_file, 'r') as file:
            lines = csv.reader(file)
            next(lines)
            for line in lines:
                air_crafts[line[0]] = Aircraft(line[3], line[0], line[1], line[4])
        file.close()
        self.air_crafts = air_crafts

    def get_aircraft(self, code):
        return self.air_crafts[code]

    def get_aircraft_by_distance(self, distance):
        for aircraft in self.air_crafts.items():
            if aircraft.fligt_range < distance:
                return aircraft


Airlines()