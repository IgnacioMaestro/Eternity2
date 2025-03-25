from typing import Optional
from unittest import TestCase

from src.eternity2_project.eternity2.piece.constraints import Constraints
from src.eternity2_project.eternity2.piece.piece import Piece
from src.eternity2_project.eternity2.game.piece_set import PieceSet
from src.eternity2_project.eternity2.piece.rotation import Rotation


class TestPiece(TestCase):
    def setUp(self):
        self.matching_color = PieceSet.DARK_BLUE_YELLOW_FLOWER
        self.no_matching_color = PieceSet.BLUE_PINK_CASTLE
        self.piece_with_border: Piece = Piece(
            2, PieceSet.EDGE, self.matching_color, self.matching_color, self.matching_color)
        self.piece_without_border: Piece = Piece(
            3, self.matching_color, self.matching_color, self.matching_color, self.matching_color)

    def test_is_valid_no_constraints_piece_without_border(self):
        # Arrange
        constraints: Constraints = Constraints(None, None, None, None)

        # Act
        rotation: Optional[Rotation] = self.piece_without_border.is_valid(constraints)

        # Assert
        self.assertIsNotNone(rotation)
        self.assertEqual(rotation, Rotation.DEGREE_0)

    def test_is_valid_no_constraints_piece_with_border(self):
        # Arrange
        constraints: Constraints = Constraints(None, None, None, None)

        # Act
        rotation: Optional[Rotation] = self.piece_with_border.is_valid(constraints)

        # Assert
        self.assertIsNone(rotation)

    def test_is_valid_with_one_constraints_up_no_match_piece_without_border(self):
        # Arrange
        constraints: Constraints = Constraints(self.no_matching_color, None, None, None)

        # Act
        rotation: Optional[Rotation] = self.piece_without_border.is_valid(constraints)

        # Assert
        self.assertIsNone(rotation)

    def test_is_valid_with_one_constraints_up_no_match_piece_with_border(self):
        # Arrange
        constraints: Constraints = Constraints(self.no_matching_color, None, None, None)

        # Act
        rotation: Optional[Rotation] = self.piece_with_border.is_valid(constraints)

        # Assert
        self.assertIsNone(rotation)

    def test_is_valid_with_one_constraints_up_match_piece_without_border(self):
        # Arrange
        constraints: Constraints = Constraints(self.matching_color, None, None, None)

        # Act
        rotation: Optional[Rotation] = self.piece_without_border.is_valid(constraints)

        # Assert
        self.assertIsNotNone(rotation)
        self.assertEqual(rotation, Rotation.DEGREE_0)

    def test_is_valid_with_one_constraints_up_match_piece_with_border(self):
        # Arrange
        constraints: Constraints = Constraints(self.matching_color, None, None, None)

        # Act
        rotation: Optional[Rotation] = self.piece_with_border.is_valid(constraints)

        # Assert
        self.assertIsNone(rotation)

    def test_is_valid_with_one_constraints_right_no_match_piece_without_border(self):
        # Arrange
        constraints: Constraints = Constraints(None, self.no_matching_color, None, None)

        # Act
        rotation: Optional[Rotation] = self.piece_without_border.is_valid(constraints)

        # Assert
        self.assertIsNone(rotation)

    def test_is_valid_with_one_constraints_right_no_match_piece_with_border(self):
        # Arrange
        constraints: Constraints = Constraints(None, self.no_matching_color, None, None)

        # Act
        rotation: Optional[Rotation] = self.piece_with_border.is_valid(constraints)

        # Assert
        self.assertIsNone(rotation)

    def test_is_valid_with_one_constraints_right_match_piece_with_border(self):
        # Arrange
        constraints: Constraints = Constraints(None, self.matching_color, None, None)

        # Act
        rotation: Optional[Rotation] = self.piece_with_border.is_valid(constraints)

        # Assert
        self.assertIsNone(rotation)

    def test_is_valid_with_one_constraints_down_no_match_piece_with_border(self):
        # Arrange
        constraints: Constraints = Constraints(None, None, self.no_matching_color, None)

        # Act
        rotation: Optional[Rotation] = self.piece_with_border.is_valid(constraints)

        # Assert
        self.assertIsNone(rotation)

    def test_is_valid_with_one_constraints_down_match_piece_with_border(self):
        # Arrange
        constraints: Constraints = Constraints(None, None, self.matching_color, None)

        # Act
        rotation: Optional[Rotation] = self.piece_with_border.is_valid(constraints)

        # Assert
        self.assertIsNone(rotation)

    def test_is_valid_with_one_constraints_left_no_match_piece_with_border(self):
        # Arrange
        constraints: Constraints = Constraints(None, None, None, self.no_matching_color)

        # Act
        rotation: Optional[Rotation] = self.piece_with_border.is_valid(constraints)

        # Assert
        self.assertIsNone(rotation)

    def test_is_valid_with_one_constraints_left_match_piece_with_border(self):
        # Arrange
        constraints: Constraints = Constraints(None, None, None, self.matching_color)

        # Act
        rotation: Optional[Rotation] = self.piece_with_border.is_valid(constraints)

        # Assert
        self.assertIsNone(rotation)
