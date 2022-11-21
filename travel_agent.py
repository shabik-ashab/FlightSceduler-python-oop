
class TravelAgent:
    def __init__(self, name) -> None:
        self.name = name
        self.trips = None 

    def __repr__(self) -> str:
        return f"TravelAgent: {self.name} "