from typing import Self

from src.eternity2_project.eternity2.Itinerary.reference_path import ReferencePath
from src.eternity2_project.eternity2.Itinerary.step import Step
from src.eternity2_project.eternity2.game.square import Square
from src.eternity2_project.eternity2.situation.rotated_piece import RotatedPiece
from src.eternity2_project.eternity2.situation.situation import Situation


class Path(ReferencePath):
    def __init__(self, situation: Situation, steps: list[Step]):
        self.__situation: Situation = situation
        self.__steps: list[Step] = steps

    def get_first_step(self) -> Step:
        return self.__steps[0]

    def obtain_deepest_path(self) -> Self:
        if self.get_first_step().is_calculated_possibilities():
            return self.get_first_step().get_first_path()
        return self

    def get_situation(self) -> Situation:
        return self.__situation

    def generate_calculated_possibilities(self):
        square: Square = self.get_first_step().get_square()
        rotated_pieces: list[RotatedPiece] = self.__situation.calculate_possibilities(square)
        for rotated_piece in rotated_pieces:
            situation = Situation.create_from(self.__situation)
            situation.place_piece(rotated_piece.get_piece(), square, rotated_piece.get_rotation())
            path = Path(situation, self.__steps[1:])
            self.get_first_step().add_path(path)

