from typing import Optional

from src.eternity2_project.eternity2.game.color import Color


class Constraints:
    def __init__(self, up: Optional[Color], right: Optional[Color], down: Optional[Color], left: Optional[Color]):
        self.__up: Optional[Color] = up
        self.__right: Optional[Color] = right
        self.__down: Optional[Color] = down
        self.__left: Optional[Color] = left
