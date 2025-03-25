from src.eternity2_project.eternity2.piece.piece import Piece
from src.eternity2_project.eternity2.piece.rotation import Rotation


class RotatedPiece:
    def __init__(self, piece: Piece, rotation: Rotation):
        self.__piece: Piece = piece
        self.__rotation: Rotation = rotation

    def __eq__(self, other):
        return self.__piece == other.__piece and self.__rotation == other.__rotation

    def get_piece(self) -> Piece:
        return self.__piece

    def get_rotation(self) -> Rotation:
        return self.__rotation
