from unittest import TestCase

from src.eternity2_project.eternity2.game.board import Board
from src.eternity2_project.eternity2.game.piece_set import PieceSet
from src.eternity2_project.eternity2.rotated_piece.rotated_piece import RotatedPiece
from src.eternity2_project.eternity2.rotated_piece.rotation import Rotation
from src.eternity2_project.eternity2.situation.situation import Situation


class TestSituation(TestCase):
    def test_calculate_possibilities_corner_no_placed(self):
        # Arrange
        situation: Situation = Situation([])
        up_left_corner_square = Board().get_up_left_corner()

        # Act
        rotated_pieces: list[RotatedPiece] = situation.calculate_possibilities(up_left_corner_square)

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

    def test_calculate_possibilities_corner_placed_3_corners_placed_no_near(self):
        # Arrange
        situation: Situation = Situation([])
        situation.place_piece(Board().get_square(0, 2), RotatedPiece(PieceSet().get_piece(1), Rotation.DEGREE_90))
        situation.place_piece(Board().get_square(0, 3), RotatedPiece(PieceSet().get_piece(2), Rotation.DEGREE_90))
        situation.place_piece(Board().get_square(0, 4), RotatedPiece(PieceSet().get_piece(3), Rotation.DEGREE_90))
        up_left_corner_square = Board().get_up_left_corner()

        # Act
        rotated_pieces: list[RotatedPiece] = situation.calculate_possibilities(up_left_corner_square)

        # Assert
        self.assertEqual(len(rotated_pieces), 1)
        expected_rotated_piece_4: RotatedPiece = RotatedPiece(PieceSet().get_piece(4), Rotation.DEGREE_90)
        self.assertIn(expected_rotated_piece_4, rotated_pieces)

    def test_calculate_possibilities_top_border_no_placed(self):
        # Arrange
        situation: Situation = Situation([])

        # Act
        rotated_pieces: list[RotatedPiece] = situation.calculate_possibilities(Board().get_square(1, 0))

        # Assert
        self.assertEqual(len(rotated_pieces), 56)

    def test_calculate_possibilities_top_border_one_placed(self):
        # Arrange
        situation: Situation = Situation([])
        situation.place_piece(Board().get_square(3, 0), RotatedPiece(PieceSet().get_piece(5), Rotation.DEGREE_180))

        # Act
        rotated_pieces: list[RotatedPiece] = situation.calculate_possibilities(Board().get_square(1, 0))

        # Assert
        self.assertEqual(len(rotated_pieces), 55)

    def test_calculate_possibilities_top_border_one_placed_next_to(self):
        # Arrange
        situation: Situation = Situation([])
        situation.place_piece(Board().get_square(2, 0), RotatedPiece(PieceSet().get_piece(5), Rotation.DEGREE_180))

        # Act
        rotated_pieces: list[RotatedPiece] = situation.calculate_possibilities(Board().get_square(1, 0))

        # Assert
        self.assertEqual(len(rotated_pieces), 9)
