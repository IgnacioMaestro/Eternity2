from src.eternity2_project.eternity2.game.piece import Piece
from src.eternity2_project.eternity2.situation.rotation import Rotation


class RotatedPiece:
    def __init__(self, piece: Piece, rotation: Rotation):
        self.__piece: Piece = piece
        self.__rotation: Rotation = rotation

    def get_piece(self) -> Piece:
        return self.__piece

    def get_rotation(self) -> Rotation:
        return self.__rotation
