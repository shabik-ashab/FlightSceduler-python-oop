from travel_agent import TravelAgent


def main():
    travel_agent = TravelAgent('Go jaan')
    trip_info1 = travel_agent.trip_one_city_one_way('DAC', 'PRA', '05/07/2022')
    # print(trip_info1.aircraft)

    trip_cities = ['DUB', 'LHR', 'SYD', 'JFK']
    trip_info2  = travel_agent.trip_multi_city_one_way_flexible(trip_cities, '20/2/22')

    for trip in trip_info2[0]:
        print(trip)

if __name__ == '__main__':
    main()