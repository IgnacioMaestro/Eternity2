from typing import Self

from src.eternity2_project.eternity2.Itinerary.path import Path
from src.eternity2_project.eternity2.Itinerary.step import Step
from src.eternity2_project.eternity2.game.game import Game
from src.eternity2_project.eternity2.situation.rotation import Rotation
from src.eternity2_project.eternity2.situation.situation import Situation


class Itinerary:
    def __init__(self, name: str, situation: Situation, steps: list[Step]):
        self.__name: str = name
        self.__path: Path = Path(situation, steps)

    @classmethod
    def create_with_first_5_pieces(cls) -> Self:
        game = Game()
        situation = Situation()
        situation.place_piece(game.get_piece(139), game.get_square(7, 8), Rotation.DEGREE_180)
        # TODO: add another 4 pieces
        steps: list[Step] = [
            Step(game.get_square(0, 0)),
            Step(game.get_square(1, 0)),
            Step(game.get_square(2, 0)),
            Step(game.get_square(2, 1))]
        return Itinerary("First 5 pieces", situation, steps)
