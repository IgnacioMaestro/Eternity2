from src.eternity2_project.eternity2.Itinerary.reference_path import ReferencePath
from src.eternity2_project.eternity2.game.square import Square


class Step:
    def __init__(self, square: Square):
        self.__square: Square = square
        self.__generated_paths: list[ReferencePath] = []

    def __str__(self):
        return str(self.__square)

    def __eq__(self, other):
        if isinstance(other, Step):
            is_equal_square = self.__square == other.get_square()
            is_equal_generated_paths = self.__generated_paths == other.__generated_paths
            return is_equal_square and is_equal_generated_paths
        return False

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
