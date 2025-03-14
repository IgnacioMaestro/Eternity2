from .color import Color
from .css_color_code import CSSColorCode
from .piece import Piece


class PieceSet:
    BORDER_COLOR = Color(1, CSSColorCode('808080'), "Border")
    WHITE_COLOR = Color(1, CSSColorCode('FFFFFF'), "White")
    __color_list: list[Color]
    __piece_list: list[Piece]

    def __init__(self):
        self.__color_list = [PieceSet.BORDER_COLOR, PieceSet.WHITE_COLOR]
        self.__piece_list = [
            Piece(PieceSet.BORDER_COLOR, PieceSet.WHITE_COLOR, PieceSet.WHITE_COLOR, PieceSet.WHITE_COLOR)]
