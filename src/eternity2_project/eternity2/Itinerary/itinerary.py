from typing import Self

from src.eternity2_project.eternity2.Itinerary.path import Path
from src.eternity2_project.eternity2.Itinerary.step import Step
from src.eternity2_project.eternity2.game.board import Board
from src.eternity2_project.eternity2.game.piece_set import PieceSet
from src.eternity2_project.eternity2.piece.rotated_piece import RotatedPiece
from src.eternity2_project.eternity2.situation.placed_piece import PlacedPiece
from src.eternity2_project.eternity2.piece.rotation import Rotation
from src.eternity2_project.eternity2.situation.situation import Situation


class Itinerary:
    def __init__(self, name: str, situation: Situation, steps: list[Step]):
        self.__name: str = name
        self.__path: Path = Path(situation, steps)

    @classmethod
    def create_with_first_5_pieces(cls) -> Self:
        board = Board()
        situation = Situation(
            [PlacedPiece(board.get_square(7, 8), RotatedPiece(PieceSet().get_piece(139), Rotation.DEGREE_180))])
        # TODO: add another 4 pieces
        steps: list[Step] = [
            Step(board.get_square(0, 0)),
            Step(board.get_square(1, 0)),
            Step(board.get_square(2, 0)),
            Step(board.get_square(2, 1))]
        return Itinerary("First 5 pieces", situation, steps)

    def obtain_deepest_path(self) -> Path:
        return self.__path.obtain_deepest_path()
