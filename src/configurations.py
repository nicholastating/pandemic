from src.enums.difficulty import Difficulty


class Configurations:
    INFECTION_RATE = [2, 2, 2, 3, 3, 4, 4]
    OUTBREAK_LIMIT = 8
    RESEARCH_STATION_LIMIT = 6
    CUBES_PER_DISEASE = 24
    CARDS_PER_PLAYER_BY_NUM_PLAYERS = {
        2: 4,
        3: 3,
        4: 2,
    }
    NUM_EPIDEMIC_CARDS_BY_DIFFICULTY = {
        Difficulty.INTRODUCTORY:    4,
        Difficulty.STANDARD:        5,
        Difficulty.HEROIC:          6,
    }

    @staticmethod
    def get_infection_rate(index: int) -> int:
        return Configurations.INFECTION_RATE[index]

    @staticmethod
    def get_starting_cards_per_player(num_players: int) -> int:
        return Configurations.CARDS_PER_PLAYER_BY_NUM_PLAYERS[num_players]

    @staticmethod
    def get_number_of_epidemics(difficulty: Difficulty) -> int:
        return Configurations.NUM_EPIDEMIC_CARDS_BY_DIFFICULTY[difficulty]
