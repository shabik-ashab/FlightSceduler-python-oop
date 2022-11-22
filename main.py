from travel_agent import TravelAgent


def main():
    travel_agent = TravelAgent('Go jaan')
    trip_info1 = travel_agent.trip_one_city_one_way('DAC', 'PRA', '05/07/2022')
    print(trip_info1.aircraft)

if __name__ == '__main__':
    main()