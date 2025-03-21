from typing import Optional
from unittest import TestCase

from src.eternity2_project.eternity2.game.constraints import Constraints
from src.eternity2_project.eternity2.game.piece import Piece
from src.eternity2_project.eternity2.game.piece_set import PieceSet
from src.eternity2_project.eternity2.game.rotation import Rotation


class TestPiece(TestCase):
    def setUp(self):
        self.piece: Piece = PieceSet().get_piece(6)

    def test_is_valid_no_constraints(self):
        # Arrange
        constraints: Constraints = Constraints(None, None, None, None)

        # Act
        rotation: Optional[Rotation] = self.piece.is_valid(constraints)

        # Assert
        self.assertIsNotNone(rotation)
        self.assertEqual(rotation, Rotation.DEGREE_0)

    def test_is_valid_with_one_constraints_up_no_match(self):
        # Arrange
        constraints: Constraints = Constraints(PieceSet.BLUE_PINK_CASTLE, None, None, None)

        # Act
        rotation: Optional[Rotation] = self.piece.is_valid(constraints)

        # Assert
        self.assertIsNone(rotation)

    def test_is_valid_with_one_constraints_up_match(self):
        # Arrange
        constraints: Constraints = Constraints(PieceSet.PURPLE_BLUE_SPADE, None, None, None)

        # Act
        rotation: Optional[Rotation] = self.piece.is_valid(constraints)

        # Assert
        self.assertIsNotNone(rotation)
        self.assertEqual(rotation, Rotation.DEGREE_0)

    def test_is_valid_with_one_constraints_right_no_match(self):
        # Arrange
        constraints: Constraints = Constraints(None, PieceSet.BLUE_PINK_CASTLE, None, None)

        # Act
        rotation: Optional[Rotation] = self.piece.is_valid(constraints)

        # Assert
        self.assertIsNone(rotation)


    def test_is_valid_with_one_constraints_right_match(self):
        # Arrange
        constraints: Constraints = Constraints(None, PieceSet.PURPLE_BLUE_SPADE, None, None)

        # Act
        rotation: Optional[Rotation] = self.piece.is_valid(constraints)

        # Assert
        self.assertIsNotNone(rotation)
        self.assertEqual(rotation, Rotation.DEGREE_90)

    def test_is_valid_with_one_constraints_down_no_match(self):
        # Arrange
        constraints: Constraints = Constraints(None, None, PieceSet.BLUE_PINK_CASTLE, None)

        # Act
        rotation: Optional[Rotation] = self.piece.is_valid(constraints)

        # Assert
        self.assertIsNone(rotation)


    def test_is_valid_with_one_constraints_down_match(self):
        # Arrange
        constraints: Constraints = Constraints(None, None, PieceSet.PURPLE_BLUE_SPADE, None)

        # Act
        rotation: Optional[Rotation] = self.piece.is_valid(constraints)

        # Assert
        self.assertIsNotNone(rotation)
        self.assertEqual(rotation, Rotation.DEGREE_180)

    def test_is_valid_with_one_constraints_left_no_match(self):
        # Arrange
        constraints: Constraints = Constraints(None,None, None, PieceSet.BLUE_PINK_CASTLE)

        # Act
        rotation: Optional[Rotation] = self.piece.is_valid(constraints)

        # Assert
        self.assertIsNone(rotation)


    def test_is_valid_with_one_constraints_left_match(self):
        # Arrange
        constraints: Constraints = Constraints(None,None, None, PieceSet.PURPLE_BLUE_SPADE)

        # Act
        rotation: Optional[Rotation] = self.piece.is_valid(constraints)

        # Assert
        self.assertIsNotNone(rotation)
        self.assertEqual(rotation, Rotation.DEGREE_270)

