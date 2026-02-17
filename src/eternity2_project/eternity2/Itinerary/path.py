from typing import Self, Optional

from src.eternity2_project.eternity2.Itinerary.reference_path import ReferencePath
from src.eternity2_project.eternity2.Itinerary.step import Step
from src.eternity2_project.eternity2.game.square import Square
from src.eternity2_project.eternity2.rotated_piece.rotated_piece import RotatedPiece
from src.eternity2_project.eternity2.situation.situation import Situation


class Path(ReferencePath):
    def __init__(self, situation: Situation, steps: list[Step]):
        self.__situation: Situation = situation
        self.__next_step: Optional[Step] = None
        self.__rest_steps: list[Step] = []
        if steps:
            self.__next_step = steps[0]
            self.__rest_steps: list[Step] = steps[1:]

    def __str__(self) -> str:
        str_situation = "Placed pieces: " + str(self.__situation)
        str_next_step = ", Next step: " + str(self.__next_step)
        str_rest_of_steps = ", Rest of the steps: " + str(len(self.__rest_steps))
        return str_situation + str_next_step + str_rest_of_steps

    def print(self):
        print('Placed pieces:')
        self.__situation.print()
        print('Steps:')
        for step in self.__steps:
            print(str(step))

    def get_first_step(self) -> Step:
        return self.__next_step

    def obtain_deepest_path(self) -> Self:
        if self.get_first_step().is_calculated_possibilities():
            return self.get_first_step().get_first_path()
        return self

    def get_situation(self) -> Situation:
        return self.__situation

    def generate_calculated_possibilities(self):
        square: Square = self.__next_step.get_square()
        rotated_pieces: list[RotatedPiece] = self.__situation.calculate_possibilities(square)
        for rotated_piece in rotated_pieces:
            path = self.create_new_path(rotated_piece, square)
            self.get_first_step().add_path(path)

    def create_new_path(self, rotated_piece, square):
        situation = Situation.create_from(self.__situation)
        situation.place_piece(square, rotated_piece)
        path = Path(situation, self.__rest_steps)
        return path
