from src.core.city_generator import CityData


class City:
    def __init__(self, city_data: CityData, research_station: bool = False):
        self.city_name = city_data.city_name

        self.virus = city_data.virus

        self.blue_cube_count = 0
        self.black_cube_count = 0
        self.red_cube_count = 0
        self.yellow_cube_count = 0
        self.research_station = research_station
