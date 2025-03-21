from src.eternity2_project.eternity2.Itinerary.reference_path import ReferencePath
from src.eternity2_project.eternity2.game.square import Square


class Step:
    def __init__(self, square: Square):
        self.__square: Square = square
        self.__generated_paths: list[ReferencePath] = []

    def add_path(self, path: ReferencePath):
        self.__generated_paths.append(path)

    def is_calculated_possibilities(self) -> bool:
        return len(self.__generated_paths) > 0

    def get_first_path(self) -> ReferencePath:
        return self.__generated_paths[0]

    def count_paths(self) -> int:
        return len(self.__generated_paths)

    def get_square(self) -> Square:
        return self.__square
