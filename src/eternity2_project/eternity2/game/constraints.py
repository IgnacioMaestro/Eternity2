from typing import Optional

from src.eternity2_project.eternity2.game.color import Color


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

    def get_up(self) -> Optional[Color]:
        return self.__up

    def get_right(self) -> Optional[Color]:
        return self.__right

    def get_down(self) -> Optional[Color]:
        return self.__down

    def get_left(self) -> Optional[Color]:
        return self.__left

    def is_up_none(self) -> bool:
        return self.__up is None

    def is_right_none(self) -> bool:
        return self.__right is None

    def is_down_none(self) -> bool:
        return self.__down is None

    def is_left_none(self) -> bool:
        return self.__left is None

    def match_with_up(self, color: Color) -> bool:
        return self.is_up_none() or self.__up == color

    def match_with_right(self, color: Color) -> bool:
        return self.is_right_none() or self.__right == color

    def match_with_down(self, color: Color) -> bool:
        return self.is_down_none() or self.__down == color

    def match_with_left(self, color: Color) -> bool:
        return self.is_left_none() or self.__left == color
