from typing import Self

from src.eternity2_project.eternity2.game.square import Square
from src.eternity2_project.eternity2.piece.constraints import Constraints
from src.eternity2_project.eternity2.piece.rotated_piece import RotatedPiece
from src.eternity2_project.eternity2.situation.constraints_calculator import ConstraintsCalculator
from src.eternity2_project.eternity2.situation.piece_searcher import PieceSearcher
from src.eternity2_project.eternity2.situation.placed_piece import PlacedPiece


class Situation:
    def __init__(self, placed_pieces: list[PlacedPiece]):
        self.__placed_pieces: list[PlacedPiece] = placed_pieces

    @classmethod
    def create_from(cls, situation: Self) -> Self:
        return Situation(situation.__placed_pieces)

    def place_piece(self, square: Square, rotated_piece: RotatedPiece):
        self.__placed_pieces.append(PlacedPiece(square, rotated_piece))

    def calculate_possibilities(self, square: Square) -> list[RotatedPiece]:
        constraints: Constraints = ConstraintsCalculator(self.__placed_pieces, square).calculate()
        return PieceSearcher(self.__placed_pieces, constraints).search()
