from unittest import TestCase

from .itinerary import Itinerary
from .path import Path
from .step import Step
from src.eternity2_project.eternity2.game.board import Board
from src.eternity2_project.eternity2.game.piece_set import PieceSet
from src.eternity2_project.eternity2.situation.placed_piece import PlacedPiece
from src.eternity2_project.eternity2.situation.situation import Situation
from src.eternity2_project.eternity2.piece.rotation import Rotation
from src.eternity2_project.eternity2.piece.rotated_piece import RotatedPiece


class TestItinerary(TestCase):
    def test_obtain_deepest_path_no_calculated_possibilities(self):
        # Arrange
        board = Board()
        initial_situation = Situation([])
        step_1_level_1 = Step(board.get_square(0, 0))
        step_2_level_1 = Step(board.get_square(1, 0))

        itinerary = Itinerary("First 5 pieces", initial_situation, [step_1_level_1, step_2_level_1])

        # Act
        path: Path = itinerary.obtain_deepest_path()

        # Assert
        self.assertEqual(path.get_first_step(), step_1_level_1)
        self.assertEqual(path.get_situation(), initial_situation)

    def test_obtain_deepest_path_one_level(self):
        # Arrange
        board = Board()
        initial_situation = Situation([])
        step_1_level_1 = Step(board.get_square(0, 0))
        step_2_level_1 = Step(board.get_square(1, 0))
        initial_situation_plus_one_piece = Situation(
            [PlacedPiece(board.get_square(7, 8), RotatedPiece(PieceSet().get_piece(1), Rotation.DEGREE_180))])
        step_1_level_2 = Step(board.get_square(1, 0))
        step_2_level_2 = Step(board.get_square(2, 0))
        path_1_level_2 = Path(initial_situation_plus_one_piece, [step_1_level_2, step_2_level_2])
        step_1_level_1.add_path(path_1_level_2)
        itinerary = Itinerary("First 5 pieces", initial_situation, [step_1_level_1, step_2_level_1])

        # Act
        path: Path = itinerary.obtain_deepest_path()

        # Assert
        self.assertEqual(path.get_first_step(), step_1_level_2)
        self.assertEqual(path.get_situation(), initial_situation_plus_one_piece)
