from typing import Self

from src.eternity2_project.eternity2.Itinerary.path import Path
from src.eternity2_project.eternity2.Itinerary.step import Step
from src.eternity2_project.eternity2.game.board import Board
from src.eternity2_project.eternity2.situation.situation import Situation


class Itinerary:
    def __init__(self, name: str, situation: Situation, steps: list[Step]):
        self.__name: str = name
        self.__path: Path = Path(situation, steps)

    def __eq__(self, other) -> bool:
        if not isinstance(other, Itinerary):
            return False
        return self.__name == other.__name and self.__path == other.__path

    @classmethod
    def create_with_first_5_pieces(cls) -> Self:
        situation = Situation.create_initial_situation()
        board = Board()
        steps: list[Step] = [
            Step.create_no_evaluated_step(board.get_square(0, 0)),
            Step.create_no_evaluated_step(board.get_square(1, 0)),
            Step.create_no_evaluated_step(board.get_square(2, 0)),
            Step.create_no_evaluated_step(board.get_square(2, 1))]
        return Itinerary("First 5 pieces", situation, steps)

    def obtain_deepest_path(self) -> Path:
        return self.__path.obtain_deepest_path()

    def print(self) -> None:
        print(self.__name)
        self.__path.print()

    def generate_next_step_in_deep(self) -> bool:
        # If path has no steps False
        if not self.__path.has_steps():
            return False

        # If first step is not evaluated
            # If step has no possibilities False


            # Else expand step and mark evaluated

        # If first step is evaluated change path


        if not self.__path.get_first_step().is_evaluated():
            return False

        return True

