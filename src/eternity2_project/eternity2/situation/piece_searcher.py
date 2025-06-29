from src.eternity2_project.eternity2.game.piece_set import PieceSet
from src.eternity2_project.eternity2.game.constraints import Constraints
from src.eternity2_project.eternity2.rotated_piece.rotated_piece import RotatedPiece
from src.eternity2_project.eternity2.situation.placed_piece import PlacedPiece


class PieceSearcher:
    def __init__(self, placed_pieces: list[PlacedPiece], constraints: Constraints):
        self.__placed_pieces: list[PlacedPiece] = placed_pieces
        self.__constraints: Constraints = constraints

    def search(self) -> list[RotatedPiece]:
        rotated_pieces: list[RotatedPiece] = PieceSet().search(self.__constraints)
        rotated_pieces_not_in_placed_pieces: list[RotatedPiece] = self.remove_placed_pieces(rotated_pieces)
        return rotated_pieces_not_in_placed_pieces

    def remove_placed_pieces(self, rotated_pieces: list[RotatedPiece]) -> list[RotatedPiece]:
        rotated_pieces_not_in_placed_pieces = []
        for rotated_piece in rotated_pieces:
            if self.is_rotated_piece_not_in_placed_pieces(rotated_piece):
                rotated_pieces_not_in_placed_pieces.append(rotated_piece)
        return rotated_pieces_not_in_placed_pieces

    def is_rotated_piece_not_in_placed_pieces(self, rotated_piece: RotatedPiece) -> bool:
        return rotated_piece.get_piece() not in [placed_piece.get_piece() for placed_piece in self.__placed_pieces]
