from src.eternity2_project.eternity2.game.color import Color


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