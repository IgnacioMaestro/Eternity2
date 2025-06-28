from unittest import TestCase

from src.eternity2_project.eternity2.game.board import Board
from src.eternity2_project.eternity2.game.piece_set import PieceSet
from src.eternity2_project.eternity2.game.constraints import Constraints
from src.eternity2_project.eternity2.rotated_piece.rotated_piece import RotatedPiece
from src.eternity2_project.eternity2.rotated_piece.rotation import Rotation
from src.eternity2_project.eternity2.situation.constraints_calculator import ConstraintsCalculator
from src.eternity2_project.eternity2.situation.placed_piece import PlacedPiece


class TestConstraintsCalculator(TestCase):
    def setUp(self):
        self.top_left_corner = Board().get_square(0, 0)
        self.top_right_corner = Board().get_square(15, 0)
        self.bottom_right_corner = Board().get_square(15, 15)

    def test_calculate_corners_no_placed(self):
        # Act
        constraints: Constraints = ConstraintsCalculator([], self.top_left_corner).calculate()

        # Assert
        self.assertEqual(constraints, Constraints(PieceSet.EDGE, None, None, PieceSet.EDGE))

        # Act
        constraints: Constraints = ConstraintsCalculator([], self.top_right_corner).calculate()

        # Assert
        self.assertEqual(constraints, Constraints(PieceSet.EDGE, PieceSet.EDGE, None, None))
        # Act
        constraints: Constraints = ConstraintsCalculator([], Board().get_square(0, 15)).calculate()

        # Assert
        self.assertEqual(constraints, Constraints(None, None, PieceSet.EDGE, PieceSet.EDGE))
        # Act
        constraints: Constraints = ConstraintsCalculator([], Board().get_square(15, 15)).calculate()

        # Assert
        self.assertEqual(constraints, Constraints(None, PieceSet.EDGE, PieceSet.EDGE, None, ))

    def test_calculate_top_left_corner_one_next_to_placed(self):
        # Arrange
        placed_piece: PlacedPiece = PlacedPiece(
            Board().get_square(1, 0), RotatedPiece(PieceSet().get_piece(6), Rotation.DEGREE_180))

        # Act
        constraints: Constraints = ConstraintsCalculator([placed_piece], self.top_left_corner).calculate()

        # Assert
        expected_constraints = Constraints(PieceSet.EDGE, PieceSet.DARK_BLUE_YELLOW_FLOWER, None, PieceSet.EDGE)
        self.assertEqual(constraints, expected_constraints)

    def test_calculate_top_left_corner_two_next_to_placed(self):
        # Arrange
        right_placed_piece: PlacedPiece = PlacedPiece(
            Board().get_square(1, 0), RotatedPiece(PieceSet().get_piece(6), Rotation.DEGREE_180))
        down_placed_piece: PlacedPiece = PlacedPiece(
            Board().get_square(0, 1), RotatedPiece(PieceSet().get_piece(7), Rotation.DEGREE_90))

        # Act
        constraints: Constraints = ConstraintsCalculator(
            [right_placed_piece, down_placed_piece], self.top_left_corner).calculate()

        # Assert
        expected_constraints = Constraints(
            PieceSet.EDGE, PieceSet.DARK_BLUE_YELLOW_FLOWER, PieceSet.ORANGE_BLUE_CROSS, PieceSet.EDGE)
        self.assertEqual(constraints, expected_constraints)

    def test_calculate_bottom_right_corner_two_next_to_placed(self):
        # Arrange
        left_placed_piece: PlacedPiece = PlacedPiece(
            Board().get_square(14, 15), RotatedPiece(PieceSet().get_piece(6), Rotation.DEGREE_0))
        top_placed_piece: PlacedPiece = PlacedPiece(
            Board().get_square(15, 14), RotatedPiece(PieceSet().get_piece(7), Rotation.DEGREE_270))

        # Act
        constraints: Constraints = ConstraintsCalculator(
            [left_placed_piece, top_placed_piece], self.bottom_right_corner).calculate()

        # Assert
        expected_constraints = Constraints(
            PieceSet.ORANGE_BLUE_CROSS, PieceSet.EDGE, PieceSet.EDGE, PieceSet.DARK_BLUE_YELLOW_FLOWER)
        self.assertEqual(constraints, expected_constraints)

    def test_calculate_normal_piece_no_placed(self):
        # Act
        constraints: Constraints = ConstraintsCalculator(
            [], Board().get_square(7, 7)).calculate()

        # Assert
        expected_constraints = Constraints(None, None, None, None)
        self.assertEqual(constraints, expected_constraints)

    def test_calculate_normal_piece_all_placed(self):
        # Arrange
        left_placed_piece: PlacedPiece = PlacedPiece(
            Board().get_square(6, 7), RotatedPiece(PieceSet().get_piece(128), Rotation.DEGREE_0))
        up_placed_piece: PlacedPiece = PlacedPiece(
            Board().get_square(7, 6), RotatedPiece(PieceSet().get_piece(128), Rotation.DEGREE_0))
        right_placed_piece: PlacedPiece = PlacedPiece(
            Board().get_square(8, 7), RotatedPiece(PieceSet().get_piece(128), Rotation.DEGREE_0))
        down_placed_piece: PlacedPiece = PlacedPiece(
            Board().get_square(7, 8), RotatedPiece(PieceSet().get_piece(128), Rotation.DEGREE_0))

        # Act
        constraints: Constraints = ConstraintsCalculator(
            [left_placed_piece, up_placed_piece, right_placed_piece, down_placed_piece],
            Board().get_square(7, 7)).calculate()

        # Assert
        expected_constraints = Constraints(PieceSet.PURPLE_BLUE_SPADE, PieceSet.DARK_BLUE_BLUE_SQUARE,
                                           PieceSet.MAROON_YELLOW_STAR, PieceSet.PINK_YELLOW_CASTLE)
        self.assertEqual(constraints, expected_constraints)
