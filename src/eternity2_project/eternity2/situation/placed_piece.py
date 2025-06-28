from src.eternity2_project.eternity2.game.square import Square
from src.eternity2_project.eternity2.game.color import Color
from src.eternity2_project.eternity2.game.piece import Piece
from src.eternity2_project.eternity2.rotated_piece.rotated_piece import RotatedPiece


class PlacedPiece:
    def __init__(self, square: Square, rotated_piece: RotatedPiece):
        self.__square: Square = square
        self.__rotated_piece: RotatedPiece = rotated_piece

    def __str__(self) -> str:
        return str(self.__rotated_piece) + ', ' + str(self.__square)

    def get_piece(self) -> Piece:
        return self.__rotated_piece.get_piece()

    def is_up(self, square: Square) -> bool:
        return self.__square.is_up_to(square)

    def is_right(self, square: Square) -> bool:
        return self.__square.is_right_to(square)

    def is_down(self, square: Square) -> bool:
        return self.__square.is_down_to(square)

    def is_left(self, square: Square) -> bool:
        return self.__square.is_left_to(square)

    def get_down_color(self) -> Color:
        return self.__rotated_piece.get_down_color()

    def get_left_color(self) -> Color:
        return self.__rotated_piece.get_left_color()

    def get_up_color(self) -> Color:
        return self.__rotated_piece.get_up_color()

    def get_right_color(self) -> Color:
        return self.__rotated_piece.get_right_color()
