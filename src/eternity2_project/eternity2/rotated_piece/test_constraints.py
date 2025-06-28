from unittest import TestCase

from src.eternity2_project.eternity2.game.piece_set import PieceSet
from src.eternity2_project.eternity2.rotated_piece.constraints import Constraints


class TestConstraints(TestCase):
    def test_match_with_up_none_with_normal_color(self):
        # Arrange
        constraints: Constraints = Constraints(None, None, None, None)

        # Act
        does_match: bool = constraints.match_with_up(PieceSet.BLUE_PINK_CASTLE)

        # Assert
        self.assertTrue(does_match)

    def test_match_with_up_none_with_border_color(self):
        # Arrange
        constraints: Constraints = Constraints(None, None, None, None)

        # Act
        does_match: bool = constraints.match_with_up(PieceSet.EDGE)

        # Assert
        self.assertFalse(does_match)

    def test_match_with_up_normal_color_with_normal_color_match(self):
        # Arrange
        constraints: Constraints = Constraints(PieceSet.BLUE_PINK_CASTLE, None, None, None)

        # Act
        does_match: bool = constraints.match_with_up(PieceSet.BLUE_PINK_CASTLE)

        # Assert
        self.assertTrue(does_match)

    def test_match_with_up_normal_color_with_normal_color_no_match(self):
        # Arrange
        constraints: Constraints = Constraints(PieceSet.BLUE_PINK_CASTLE, None, None, None)

        # Act
        does_match: bool = constraints.match_with_up(PieceSet.BLUE_PINK_SPADE)

        # Assert
        self.assertFalse(does_match)

    def test_match_with_up_normal_color_with_border_color(self):
        # Arrange
        constraints: Constraints = Constraints(PieceSet.BLUE_PINK_CASTLE, None, None, None)

        # Act
        does_match: bool = constraints.match_with_up(PieceSet.EDGE)

        # Assert
        self.assertFalse(does_match)
