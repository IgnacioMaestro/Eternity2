from unittest import TestCase

from src.eternity2_project.eternity2.game.board import Board
from src.eternity2_project.eternity2.situation.situation import Situation
from .itinerary import Itinerary
from .path import Path
from .step import Step


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
