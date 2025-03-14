from src.eternity2_project.eternity2.game.color import Color


class Piece:
    __up: Color
    __down: Color
    __left: Color
    __right: Color

    def __init__(self, up: Color, down: Color, left: Color, right: Color):
        self.__up = up
        self.__down = down
        self.__left = left
        self.__right = right