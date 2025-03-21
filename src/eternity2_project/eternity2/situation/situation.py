from typing import Self

from src.eternity2_project.eternity2.game.piece import Piece
from src.eternity2_project.eternity2.game.square import Square
from src.eternity2_project.eternity2.situation.placed_piece import PlacedPiece
from src.eternity2_project.eternity2.situation.rotated_piece import RotatedPiece
from src.eternity2_project.eternity2.situation.rotation import Rotation


class Situation:
    def __init__(self, placed_pieces: list[PlacedPiece]):
        self.__placed_pieces: list[PlacedPiece] = placed_pieces

    @classmethod
    def create_from(cls, situation: Self) -> Self:
        return Situation(situation.__placed_pieces)


    def place_piece(self, piece: Piece, square: Square, rotation: Rotation):
        self.__placed_pieces.append(PlacedPiece(piece, square, rotation))

    def calculate_possibilities(self) -> list[RotatedPiece]:
        return []