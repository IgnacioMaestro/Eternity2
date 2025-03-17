from src.eternity2_project.eternity2.game.square import Square
from src.eternity2_project.eternity2.situation.situation import Situation


class Step:
    def __init__(self, square: Square):
        self.__square: Square = square
        self.__generated_paths: list[Path] = []


class Path:
    def __init__(self, situation: Situation, steps: list[Step]):
        self.__situation: Situation = situation
        self.__steps: list[Step] = steps


class Itinerary:
    def __init__(self, name: str, situation: Situation, steps: list[Step]):
        self.__name: str = name
        self.__path: Path = Path(situation, steps)