from src.eternity2_project.eternity2.Itinerary.path import Path
from src.eternity2_project.eternity2.game.square import Square


class Step:
    def __init__(self, square: Square):
        self.__square: Square = square
        self.__generated_paths: list[Path] = []
