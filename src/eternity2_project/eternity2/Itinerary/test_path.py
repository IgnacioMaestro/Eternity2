from unittest import TestCase
from unittest.mock import patch, MagicMock

from src.eternity2_project.eternity2.Itinerary.path import Path
from src.eternity2_project.eternity2.Itinerary.step import Step
from src.eternity2_project.eternity2.game.board import Board
from src.eternity2_project.eternity2.game.piece_set import PieceSet
from src.eternity2_project.eternity2.game.square import Square
from src.eternity2_project.eternity2.rotated_piece.rotated_piece import RotatedPiece
from src.eternity2_project.eternity2.rotated_piece.rotation import Rotation
from src.eternity2_project.eternity2.situation.placed_piece import PlacedPiece
from src.eternity2_project.eternity2.situation.situation import Situation


class TestPath(TestCase):
    def test_str_no_steps(self):
        # Arrange
        situation: Situation = Situation([])
        path: Path = Path(situation, [])

        # Act
        str_path: str = str(path)

        # Assert
        self.assertEqual(str_path, "Placed pieces: " + str(situation) + ", Next step: None, Rest of the steps: 0")

    def test_str_one_steps(self):
        # Arrange
        situation: Situation = Situation([])
        step: Step = Step(Square(1, 0))
        path: Path = Path(situation, [step])

        # Act
        str_path: str = str(path)

        # Assert
        self.assertEqual(
            str_path,
            "Placed pieces: " + str(situation) + ", Next step: " + str(step) + ", Rest of the steps: 0")

    def test_str_two_steps(self):
        # Arrange
        situation: Situation = Situation([])
        first_step: Step = Step(Square(1, 0))
        second_step: Step = Step(Square(1, 1))
        path: Path = Path(situation, [first_step, second_step])

        # Act
        str_path: str = str(path)

        # Assert
        self.assertEqual(
            str_path,
            "Placed pieces: " + str(situation) + ", Next step: " + str(first_step) + ", Rest of the steps: 1")

    @patch.object(Situation, "calculate_possibilities")
    def test_genera_calculate_possibilities(self, mock_calculate_possibilities: MagicMock):
        # Arrange
        rotated_piece: RotatedPiece = RotatedPiece(PieceSet().get_piece(1), Rotation.DEGREE_90)
        mock_calculate_possibilities.return_value = [rotated_piece, rotated_piece, rotated_piece, rotated_piece]
        board = Board()
        step: Step = Step(board.get_square(0, 0))
        path: Path = Path(Situation([]), [step])

        # Act
        path.generate_calculated_possibilities()

        # Assert
        self.assertEqual(step.count_paths(), 4)
        self.assertTrue(step.is_calculated_possibilities())
        deepest_path = path.obtain_deepest_path()
        expected_situation = Situation([PlacedPiece(board.get_square(0, 0), rotated_piece)])
        self.assertEqual(deepest_path.get_situation(), expected_situation)
