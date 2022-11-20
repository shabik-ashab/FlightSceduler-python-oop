
class Airport:
    def __init__(self, code, name, country, city, lat, long, rate) -> None:
        self.name = name
        self.country = country
        self.lat = float(lat)
        self.long = float(long)
        self.rate = float(rate)
        self.code = code 
        self.city = city

    def __repr__(self) -> str:
        return f"Airport: {self.name} in: {self.country} lattitude {self.lat} longitude: {self.long} rate: {self.rate} "


