from src.eternity2_project.eternity2.piece.color import Color
from src.eternity2_project.eternity2.piece.piece import Piece
from src.eternity2_project.eternity2.game.square import Square
from src.eternity2_project.eternity2.piece.rotation import Rotation


class PlacedPiece:
    def __init__(self, piece: Piece, square: Square, rotation: Rotation):
        self.__piece: Piece = piece
        self.__square: Square = square
        self.__rotation: Rotation = rotation

    def get_piece(self) -> Piece:
        return self.__piece

    def is_up(self, square: Square) -> bool:
        return self.__square.is_up_to(square)

    def is_right(self, square: Square) -> bool:
        return self.__square.is_right_to(square)

    def is_down(self, square: Square) -> bool:
        return self.__square.is_down_to(square)

    def is_left(self, square: Square) -> bool:
        return self.__square.is_left_to(square)

    def get_down_color(self) -> Color:
        return self.__piece.get_down_color()

    def get_left_color(self) -> Color:
        return self.__piece.get_left_color()

    def get_up_color(self) -> Color:
        return self.__piece.get_up_color()

    def get_right_color(self) -> Color:
        return self.__piece.get_right_color()
