from src.eternity2_project.eternity2.piece.color import Color
from src.eternity2_project.eternity2.piece.piece import Piece
from src.eternity2_project.eternity2.piece.rotation import Rotation


class RotatedPiece:
    def __init__(self, piece: Piece, rotation: Rotation):
        self.__piece: Piece = piece
        self.__rotation: Rotation = rotation

    def __eq__(self, other):
        return self.__piece == other.__piece and self.__rotation == other.__rotation

    def __str__(self) -> str:
        return str(self.__piece) + str(self.__rotation)

    def get_piece(self) -> Piece:
        return self.__piece

    def get_rotation(self) -> Rotation:
        return self.__rotation

    def get_down_color(self) -> Color:
        if self.__rotation == Rotation.DEGREE_0:
            return self.__piece.get_down_color()
        if self.__rotation == Rotation.DEGREE_90:
            return self.__piece.get_right_color()
        if self.__rotation == Rotation.DEGREE_180:
            return self.__piece.get_up_color()
        if self.__rotation == Rotation.DEGREE_270:
            return self.__piece.get_left_color()
        return self.__piece.get_left_color()

    def get_left_color(self) -> Color:
        if self.__rotation == Rotation.DEGREE_0:
            return self.__piece.get_left_color()
        if self.__rotation == Rotation.DEGREE_90:
            return self.__piece.get_down_color()
        if self.__rotation == Rotation.DEGREE_180:
            return self.__piece.get_right_color()
        if self.__rotation == Rotation.DEGREE_270:
            return self.__piece.get_up_color()
        return self.__piece.get_up_color()

    def get_up_color(self) -> Color:
        if self.__rotation == Rotation.DEGREE_0:
            return self.__piece.get_up_color()
        if self.__rotation == Rotation.DEGREE_90:
            return self.__piece.get_left_color()
        if self.__rotation == Rotation.DEGREE_180:
            return self.__piece.get_down_color()
        if self.__rotation == Rotation.DEGREE_270:
            return self.__piece.get_right_color()
        return self.__piece.get_right_color()

    def get_right_color(self) -> Color:
        if self.__rotation == Rotation.DEGREE_0:
            return self.__piece.get_right_color()
        if self.__rotation == Rotation.DEGREE_90:
            return self.__piece.get_up_color()
        if self.__rotation == Rotation.DEGREE_180:
            return self.__piece.get_left_color()
        if self.__rotation == Rotation.DEGREE_270:
            return self.__piece.get_down_color()
        return self.__piece.get_down_color()
