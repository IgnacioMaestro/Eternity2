from typing import Self

from src.eternity2_project.eternity2.Itinerary.reference_path import ReferencePath
from src.eternity2_project.eternity2.Itinerary.step import Step
from src.eternity2_project.eternity2.game.square import Square
from src.eternity2_project.eternity2.piece.rotated_piece import RotatedPiece
from src.eternity2_project.eternity2.situation.situation import Situation


class Path(ReferencePath):
    def __init__(self, situation: Situation, steps: list[Step]):
        self.__situation: Situation = situation
        self.__steps: list[Step] = steps

    def __str__(self) -> str:
        return "Placed pieces: " + str(self.__situation) + ", Steps: " + str(len(self.__steps))

    def print(self):
        print('Placed pieces:')
        self.__situation.print()
        print('Steps:')
        for step in self.__steps:
            print(str(step))

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
            path = self.create_new_path(rotated_piece, square)
            self.get_first_step().add_path(path)

    def create_new_path(self, rotated_piece, square):
        situation = Situation.create_from(self.__situation)
        situation.place_piece(square, rotated_piece)
        path = Path(situation, self.__steps[1:])
        return path
