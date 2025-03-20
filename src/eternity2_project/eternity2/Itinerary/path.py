from typing import Self

from src.eternity2_project.eternity2.Itinerary.reference_path import ReferencePath
from src.eternity2_project.eternity2.Itinerary.step import Step
from src.eternity2_project.eternity2.situation.situation import Situation


class Path(ReferencePath):
    def __init__(self, situation: Situation, steps: list[Step]):
        self.__situation: Situation = situation
        self.__steps: list[Step] = steps

    def get_first_step(self) -> Step:
        return self.__steps[0]

    def create_path(self):
        self.__steps[0].add_path(Path(self.__situation, self.__steps[1:]))

    def obtain_deepest_path(self) -> Self:
        if self.get_first_step().is_calculated_possibilities():
            return self.get_first_step().get_first_path()
        return self

    def get_situation(self) -> Situation:
        return self.__situation