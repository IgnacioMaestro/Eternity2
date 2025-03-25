from typing import Optional

from src.eternity2_project.eternity2.piece.color import Color


class Constraints:
    def __init__(self, up: Optional[Color], right: Optional[Color], down: Optional[Color], left: Optional[Color]):
        self.__up: Optional[Color] = up
        self.__right: Optional[Color] = right
        self.__down: Optional[Color] = down
        self.__left: Optional[Color] = left

    def __eq__(self, other):
        equal_up = self.__up == other.__up
        equal_right = self.__right == other.__right
        equal_down = self.__down == other.__down
        equal_left = self.__left == other.__left
        return equal_up and equal_right and equal_down and equal_left

    def match_with_up(self, color: Color) -> bool:
        if self.__up is None:
            return not color.is_edge()
        else:
            return self.__up == color

    def match_with_right(self, color: Color) -> bool:
        if self.__right is None:
            return not color.is_edge()
        else:
            return self.__right == color

    def match_with_down(self, color: Color) -> bool:
        if self.__down is None:
            return not color.is_edge()
        else:
            return self.__down == color

    def match_with_left(self, color: Color) -> bool:
        if self.__left is None:
            return not color.is_edge()
        else:
            return self.__left == color
