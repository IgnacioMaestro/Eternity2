from .board import Board
from .piece import Piece
from .piece_set import PieceSet
from .square import Square


class Game:
    def __init__(self):
        self.__piece_set = PieceSet()
        self.__board = Board()

    def get_square(self, column: int, row: int) -> Square:
        return self.__board.get_square(column, row)

    def get_piece(self, piece_number: int) -> Piece:
        return self.__piece_set.get_piece(piece_number)
