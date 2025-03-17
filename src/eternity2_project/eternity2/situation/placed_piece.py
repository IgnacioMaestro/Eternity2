from src.eternity2_project.eternity2.game.piece import Piece
from src.eternity2_project.eternity2.game.square import Square
from src.eternity2_project.eternity2.situation.rotation import Rotation


class PlacedPiece:
    def __init__(self, piece: Piece, square: Square, rotation: Rotation):
        self.__piece: Piece = piece
        self.__square: Square = square
        self.__rotation: Rotation = rotation
