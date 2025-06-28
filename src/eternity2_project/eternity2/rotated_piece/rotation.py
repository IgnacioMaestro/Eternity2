from enum import Enum
from typing import Self


class Rotation(Enum):
    DEGREE_0 = 0
    DEGREE_90 = 1
    DEGREE_180 = 2
    DEGREE_270 = 3

    def rotate_90_degrees(self) -> Self:
        return Rotation((self.value + 1) % 4)
