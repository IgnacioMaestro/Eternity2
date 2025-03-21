from unittest import TestCase
from unittest.mock import patch, MagicMock

from src.eternity2_project.eternity2.Itinerary.path import Path
from src.eternity2_project.eternity2.Itinerary.step import Step
from src.eternity2_project.eternity2.game.board import Board
from src.eternity2_project.eternity2.game.piece_set import PieceSet
from src.eternity2_project.eternity2.situation.rotated_piece import RotatedPiece
from src.eternity2_project.eternity2.situation.rotation import Rotation
from src.eternity2_project.eternity2.situation.situation import Situation


class TestPath(TestCase):
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