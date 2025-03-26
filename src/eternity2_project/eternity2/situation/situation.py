from typing import Self

from src.eternity2_project.eternity2.game.board import Board
from src.eternity2_project.eternity2.game.piece_set import PieceSet
from src.eternity2_project.eternity2.game.square import Square
from src.eternity2_project.eternity2.piece.constraints import Constraints
from src.eternity2_project.eternity2.piece.rotated_piece import RotatedPiece
from src.eternity2_project.eternity2.piece.rotation import Rotation
from src.eternity2_project.eternity2.situation.constraints_calculator import ConstraintsCalculator
from src.eternity2_project.eternity2.situation.piece_searcher import PieceSearcher
from src.eternity2_project.eternity2.situation.placed_piece import PlacedPiece


class Situation:
    def __init__(self, placed_pieces: list[PlacedPiece]):
        self.__placed_pieces: list[PlacedPiece] = placed_pieces

    @classmethod
    def create_initial_situation(cls) -> Self:
        board = Board()
        situation = Situation(
            [PlacedPiece(board.get_square(7, 8), RotatedPiece(PieceSet().get_piece(139), Rotation.DEGREE_180)),
             PlacedPiece(board.get_square(2, 2), RotatedPiece(PieceSet().get_piece(208), Rotation.DEGREE_270)),
             PlacedPiece(board.get_square(13, 2), RotatedPiece(PieceSet().get_piece(255), Rotation.DEGREE_270)),
             PlacedPiece(board.get_square(2, 13), RotatedPiece(PieceSet().get_piece(181), Rotation.DEGREE_270)),
             PlacedPiece(board.get_square(13, 13), RotatedPiece(PieceSet().get_piece(249), Rotation.DEGREE_0))])
        return situation

    @classmethod
    def create_from(cls, situation: Self) -> Self:
        return Situation(situation.__placed_pieces)

    def place_piece(self, square: Square, rotated_piece: RotatedPiece):
        self.__placed_pieces.append(PlacedPiece(square, rotated_piece))

    def calculate_possibilities(self, square: Square) -> list[RotatedPiece]:
        constraints: Constraints = ConstraintsCalculator(self.__placed_pieces, square).calculate()
        return PieceSearcher(self.__placed_pieces, constraints).search()
