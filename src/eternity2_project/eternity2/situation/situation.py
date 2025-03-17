from src.eternity2_project.eternity2.game.piece import Piece
from src.eternity2_project.eternity2.game.square import Square
from src.eternity2_project.eternity2.situation.placed_piece import PlacedPiece
from src.eternity2_project.eternity2.situation.rotation import Rotation


class Situation:
    def __init__(self):
        self.__placed_pieces: list[PlacedPiece] = []

    def place_piece(self, piece: Piece, square: Square, rotation: Rotation):
        self.__placed_pieces.append(PlacedPiece(piece, square, rotation))
