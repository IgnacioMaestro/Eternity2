from unittest import TestCase, skip

from src.eternity2_project.eternity2.game.board import Board
from src.eternity2_project.eternity2.game.piece_set import PieceSet
from src.eternity2_project.eternity2.situation.rotated_piece import RotatedPiece
from src.eternity2_project.eternity2.situation.rotation import Rotation
from src.eternity2_project.eternity2.situation.situation import Situation


class TestSituation(TestCase):
    def test_calculate_possibilities_corner_no_placed(self):
        # Arrange
        situation: Situation = Situation([])
        corner_square = Board().get_square(0, 0)

        # Act
        rotated_pieces: list[RotatedPiece] = situation.calculate_possibilities(corner_square)

        # Assert
        self.assertEqual(len(rotated_pieces), 4)
        expected_rotated_piece_1: RotatedPiece = RotatedPiece(PieceSet().get_piece(1), Rotation.DEGREE_90)
        expected_rotated_piece_2: RotatedPiece = RotatedPiece(PieceSet().get_piece(2), Rotation.DEGREE_90)
        expected_rotated_piece_3: RotatedPiece = RotatedPiece(PieceSet().get_piece(3), Rotation.DEGREE_90)
        expected_rotated_piece_4: RotatedPiece = RotatedPiece(PieceSet().get_piece(4), Rotation.DEGREE_90)
        self.assertIn(expected_rotated_piece_1, rotated_pieces)
        self.assertIn(expected_rotated_piece_2, rotated_pieces)
        self.assertIn(expected_rotated_piece_3, rotated_pieces)
        self.assertIn(expected_rotated_piece_4, rotated_pieces)

    @skip('TODO: implement')
    def test_calculate_possibilities_top_border(self):
        # Arrange
        situation: Situation = Situation([])

        # Act
        rotated_pieces: list[RotatedPiece] = situation.calculate_possibilities(Board().get_square(0, 1))

        # Assert
        self.assertEqual(len(rotated_pieces), 60)


