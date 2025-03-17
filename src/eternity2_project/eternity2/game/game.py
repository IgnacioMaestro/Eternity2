from .board import Board
from .piece_set import PieceSet


class Game:
    def __init__(self):
        self.__piece_set = PieceSet()
        self.__board = Board()
