from unittest import TestCase, skip

from src.eternity2_project.eternity2.game.board import Board
from src.eternity2_project.eternity2.situation.situation import Situation
from .itinerary import Itinerary
from .path import Path
from .step import Step
from ..game.piece_set import PieceSet
from ..game.square import Square
from ..rotated_piece.rotated_piece import RotatedPiece
from ..rotated_piece.rotation import Rotation
from ..situation.placed_piece import PlacedPiece


class TestItinerary(TestCase):
    def test_obtain_deepest_path_no_calculated_possibilities(self):
        # Arrange
        board = Board()
        initial_situation = Situation([])
        step_1_level_1 = Step.create_no_evaluated_step(board.get_square(0, 0))
        step_2_level_1 = Step.create_no_evaluated_step(board.get_square(1, 0))

        itinerary = Itinerary("First 5 pieces", initial_situation, [step_1_level_1, step_2_level_1])

        # Act
        path: Path = itinerary.obtain_deepest_path()

        # Assert
        self.assertEqual(path.get_first_step(), step_1_level_1)
        self.assertEqual(path.get_situation(), initial_situation)

    def test_generate_next_step_in_deep_no_steps_in_deep(self):
        initial_situation = Situation([])
        itinerary = Itinerary("First 5 pieces", initial_situation, [])

        # Act
        generated: bool = itinerary.generate_next_step_in_deep()

        # Assert
        self.assertFalse(generated)
        expected_itinerary = Itinerary("First 5 pieces", initial_situation, [])
        self.assertEqual(itinerary, expected_itinerary)

    def test_generate_next_step_in_deep_one_no_evaluated_step_no_possibilities(self):
        one_zero_placed_piece = PlacedPiece(Square(1, 0), RotatedPiece(PieceSet().get_piece(1), Rotation.DEGREE_0))
        initial_situation = Situation([one_zero_placed_piece])
        step = Step.create_no_evaluated_step(Square(0, 0))
        itinerary = Itinerary("First 5 pieces", initial_situation, [step])

        # Act
        generated: bool = itinerary.generate_next_step_in_deep()

        # Assert
        self.assertFalse(generated)
        evaluated_step = Step.create_evaluated_step(Square(0, 0))
        expected_itinerary = Itinerary("First 5 pieces", initial_situation, [evaluated_step])
        self.assertEqual(itinerary, expected_itinerary)
