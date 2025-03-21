from typing import Optional

from src.eternity2_project.eternity2.game.color import Color
from src.eternity2_project.eternity2.game.constraints import Constraints
from src.eternity2_project.eternity2.game.rotation import Rotation


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

    def is_valid(self, constraints: Constraints) -> Optional[Rotation]:
        if self.is_valid_rotation_0(constraints):
            return Rotation.DEGREE_0
        if self.is_valid_rotation_90(constraints):
            return Rotation.DEGREE_90
        if self.is_valid_rotation_180(constraints):
            return Rotation.DEGREE_180
        if self.is_valid_rotation_270(constraints):
            return Rotation.DEGREE_270
        else:
            return None

    def is_valid_rotation_0(self, constraints: Constraints) -> bool:
        is_valid_up: bool = constraints.match_with_up(self.__up)
        is_valid_right: bool = constraints.match_with_right(self.__right)
        is_valid_down: bool = constraints.match_with_down(self.__down)
        is_valid_left: bool = constraints.match_with_left(self.__left)
        return is_valid_up and is_valid_right and is_valid_down and is_valid_left

    def is_valid_rotation_90(self, constraints: Constraints) -> bool:
        is_valid_up: bool = constraints.match_with_up(self.__left)
        is_valid_right: bool = constraints.match_with_right(self.__up)
        is_valid_down: bool = constraints.match_with_down(self.__right)
        is_valid_left: bool = constraints.match_with_left(self.__down)
        return is_valid_up and is_valid_right and is_valid_down and is_valid_left

    def is_valid_rotation_180(self, constraints: Constraints) -> bool:
        is_valid_up: bool = constraints.match_with_up(self.__down)
        is_valid_right: bool = constraints.match_with_right(self.__left)
        is_valid_down: bool = constraints.match_with_down(self.__up)
        is_valid_left: bool = constraints.match_with_left(self.__right)
        return is_valid_up and is_valid_right and is_valid_down and is_valid_left

    def is_valid_rotation_270(self, constraints: Constraints) -> bool:
        is_valid_up: bool = constraints.match_with_up(self.__right)
        is_valid_right: bool = constraints.match_with_right(self.__down)
        is_valid_down: bool = constraints.match_with_down(self.__left)
        is_valid_left: bool = constraints.match_with_left(self.__up)
        return is_valid_up and is_valid_right and is_valid_down and is_valid_left
