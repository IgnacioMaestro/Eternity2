from typing import Self, Optional

from src.eternity2_project.eternity2.game.color import Color
from src.eternity2_project.eternity2.game.constraints import Constraints
from src.eternity2_project.eternity2.game.piece import Piece
from src.eternity2_project.eternity2.game.piece_set import PieceSet
from src.eternity2_project.eternity2.game.square import Square
from src.eternity2_project.eternity2.situation.placed_piece import PlacedPiece
from src.eternity2_project.eternity2.situation.rotated_piece import RotatedPiece
from src.eternity2_project.eternity2.situation.rotation import Rotation


class PieceSearcher:
    def __init__(self, placed_pieces: list[PlacedPiece], constraints: Constraints):
        self.__placed_pieces: list[PlacedPiece] = placed_pieces
        self.__constraints: Constraints = constraints

    def search(self) -> list[RotatedPiece]:
        pieces: list[Piece] = PieceSet().search(self.__constraints)
        rotated_pieces: list[RotatedPiece] = []
        for piece in pieces:
            rotated_pieces.append(RotatedPiece(piece, Rotation.DEGREE_0))
        return rotated_pieces


class Situation:
    def __init__(self, placed_pieces: list[PlacedPiece]):
        self.__placed_pieces: list[PlacedPiece] = placed_pieces

    @classmethod
    def create_from(cls, situation: Self) -> Self:
        return Situation(situation.__placed_pieces)

    def place_piece(self, piece: Piece, square: Square, rotation: Rotation):
        self.__placed_pieces.append(PlacedPiece(piece, square, rotation))

    def calculate_possibilities(self, square: Square) -> list[RotatedPiece]:
        constraints: Constraints = self.__get_constraints(square)
        rotated_pieces: list[RotatedPiece] = self.__search(constraints)
        return rotated_pieces

    def __get_constraints(self, square: Square) -> Constraints:
        up_constraint: Optional[Color] = self.__get_up_constraint(square)
        right_constraint: Optional[Color] = self.__get_right_constraint(square)
        down_constraint: Optional[Color] = self.__get_down_constraint(square)
        left_constraint: Optional[Color] = self.__get_left_constraint(square)
        return Constraints(up_constraint, right_constraint, down_constraint, left_constraint)

    def __get_up_constraint(self, square: Square) -> Optional[Color]:
        up_placed_piece: Optional[PlacedPiece] = self.__get_up_placed_piece(square)
        if up_placed_piece is None:
            return None
        return up_placed_piece.get_down_color()

    def __get_right_constraint(self, square: Square) -> Optional[Color]:
        right_placed_piece: Optional[PlacedPiece] = self.__get_right_placed_piece(square)
        if right_placed_piece is None:
            return None
        return right_placed_piece.get_left_color()

    def __get_down_constraint(self, square: Square) -> Optional[Color]:
        down_placed_piece: Optional[PlacedPiece] = self.__get_down_placed_piece(square)
        if down_placed_piece is None:
            return None
        return down_placed_piece.get_up_color()

    def __get_left_constraint(self, square: Square) -> Optional[Color]:
        left_placed_piece: Optional[PlacedPiece] = self.__get_left_placed_piece(square)
        if left_placed_piece is None:
            return None
        return left_placed_piece.get_right_color()

    def __get_up_placed_piece(self, square: Square) -> Optional[PlacedPiece]:
        for placed_piece in self.__placed_pieces:
            if placed_piece.is_up(square):
                return placed_piece

    def __get_right_placed_piece(self, square: Square) -> Optional[PlacedPiece]:
        for placed_piece in self.__placed_pieces:
            if placed_piece.is_right(square):
                return placed_piece

    def __get_down_placed_piece(self, square: Square) -> Optional[PlacedPiece]:
        for placed_piece in self.__placed_pieces:
            if placed_piece.is_down(square):
                return placed_piece

    def __get_left_placed_piece(self, square: Square) -> Optional[PlacedPiece]:
        for placed_piece in self.__placed_pieces:
            if placed_piece.is_left(square):
                return placed_piece

    def __search(self, constraints: Constraints) -> list[RotatedPiece]:
        return PieceSearcher(self.__placed_pieces, constraints).search()
