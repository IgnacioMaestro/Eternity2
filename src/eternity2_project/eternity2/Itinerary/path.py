from src.eternity2_project.eternity2.Itinerary.step import Step
from src.eternity2_project.eternity2.situation.situation import Situation


class Path:
    def __init__(self, situation: Situation, steps: list[Step]):
        self.__situation: Situation = situation
        self.__steps: list[Step] = steps
