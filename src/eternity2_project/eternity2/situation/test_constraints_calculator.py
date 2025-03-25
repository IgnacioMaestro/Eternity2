from unittest import TestCase

from src.eternity2_project.eternity2.game.board import Board
from src.eternity2_project.eternity2.piece.constraints import Constraints
from src.eternity2_project.eternity2.game.piece_set import PieceSet
from src.eternity2_project.eternity2.piece.rotation import Rotation
from src.eternity2_project.eternity2.situation.constraints_calculator import ConstraintsCalculator
from src.eternity2_project.eternity2.situation.placed_piece import PlacedPiece


class TestConstraintsCalculator(TestCase):
    def test_calculate_corners_no_placed(self):
        # Act
        constraints: Constraints = ConstraintsCalculator([], Board().get_square(0, 0)).calculate()

        # Assert
        self.assertEqual(constraints, Constraints(PieceSet.BORDER, None, None, PieceSet.BORDER))

        # Act
        constraints: Constraints = ConstraintsCalculator([], Board().get_square(15, 0)).calculate()

        # Assert
        self.assertEqual(constraints, Constraints(PieceSet.BORDER, PieceSet.BORDER, None, None))
        # Act
        constraints: Constraints = ConstraintsCalculator([], Board().get_square(0, 15)).calculate()

        # Assert
        self.assertEqual(constraints, Constraints(None, None, PieceSet.BORDER, PieceSet.BORDER))
        # Act
        constraints: Constraints = ConstraintsCalculator([], Board().get_square(15, 15)).calculate()

        # Assert
        self.assertEqual(constraints, Constraints(None, PieceSet.BORDER, PieceSet.BORDER, None, ))

    def test_calculate_corner_one_next_to_placed(self):
        # Arrange
        placed_piece: PlacedPiece = PlacedPiece(PieceSet().get_piece(6), Board().get_square(0, 1), Rotation.DEGREE_180)

        # Act
        constraints: Constraints = ConstraintsCalculator([placed_piece], Board().get_square(0, 0)).calculate()

        # Assert
        expected_constraints = Constraints(PieceSet.BORDER, PieceSet.DARK_BLUE_YELLOW_FLOWER, None, PieceSet.BORDER)
        self.assertEqual(constraints, expected_constraints)
