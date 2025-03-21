from src.eternity2_project.eternity2.game.color import Color
from src.eternity2_project.eternity2.game.constraints import Constraints


class Piece:
    __number: int
    __up: Color
    __down: Color
    __left: Color
    __right: Color

    def __init__(self, piece_number: int, up: Color, right: Color, down: Color, left: Color):
        self.__number = piece_number
        self.__up = up
        self.__down = down
        self.__left = left
        self.__right = right

    def __eq__(self, other):
        return self.__number == other.__number

    def get_down_color(self) -> Color:
        return self.__down

    def get_left_color(self) -> Color:
        return self.__left

    def get_up_color(self) -> Color:
        return self.__up

    def get_right_color(self) -> Color:
        return self.__right

    def is_valid(self, constraints: Constraints) -> bool:
        return True

