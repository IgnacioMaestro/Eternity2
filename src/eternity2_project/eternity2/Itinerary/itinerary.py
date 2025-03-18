from src.eternity2_project.eternity2.Itinerary.path import Path
from src.eternity2_project.eternity2.Itinerary.step import Step
from src.eternity2_project.eternity2.situation.situation import Situation


class Itinerary:
    def __init__(self, name: str, situation: Situation, steps: list[Step]):
        self.__name: str = name
        self.__path: Path = Path(situation, steps)
