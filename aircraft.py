
class Aircraft:
    def __init__(self, brand, code, type, flight_range) -> None:
        self.brand = brand
        self.code = code
        self.type = type
        self.flight_range = flight_range

    def get_brand(self):
        return self.brand

    def __repr__(self) -> str:
        return f"Aircraft made by: {self.brand} code: {self.code} type: {self.type} range: {self.flight_range}"



    