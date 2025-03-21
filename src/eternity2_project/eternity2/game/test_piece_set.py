from unittest import TestCase

from src.eternity2_project.eternity2.game.board import Board
from src.eternity2_project.eternity2.game.piece import Piece
from src.eternity2_project.eternity2.game.piece_set import PieceSet
from src.eternity2_project.eternity2.situation.placed_piece import PlacedPiece
from src.eternity2_project.eternity2.situation.rotation import Rotation


class TestPieceSet(TestCase):
    def test_get_no_placed_pieces_no_placed_pieces(self):
        # Act
        pieces: list[Piece] = PieceSet().get_no_placed_pieces([])

        # Assert
        self.assertEqual(len(pieces), 208)

    def test_get_no_placed_pieces_one_placed_piece(self):
        # Arrange
        piece: Piece = Piece(1, PieceSet.ORANGE_BLUE_CROSS, PieceSet.PINK_BLUE_CROSS, PieceSet.BORDER, PieceSet.BORDER)
        placed_piece: PlacedPiece =PlacedPiece(piece, Board().get_square(0, 0), Rotation.DEGREE_0)

        # Act
        pieces: list[Piece] = PieceSet().get_no_placed_pieces([placed_piece])

        # Assert
        self.assertEqual(len(pieces), 207)

