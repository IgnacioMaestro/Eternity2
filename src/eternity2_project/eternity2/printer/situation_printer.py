from typing import List, Optional, Self, Final

from src.eternity2_project.eternity2.piece.rotated_piece import RotatedPiece
from src.eternity2_project.eternity2.printer.line_printer import LinePrinter


class SituationPrinter:
    ROW_COUNT: Final[int] = 16
    ROW_WIDTH: Final[int] = 16

    def __init__(self, pieces: List[Optional[RotatedPiece]]):
        self.__pieces = pieces

    @classmethod
    def create(cls, pieces: List[Optional[RotatedPiece]]) -> Self:
        if len(pieces) != 16 * 16:
            raise ValueError("LinePrinter requires exactly 256 pieces")
        return cls(pieces)

    def print(self) -> str:
        result = ""
        for row_index in range(self.ROW_COUNT):
            result += self.print_row(row_index) + ("-" * (LinePrinter.PIECE_WIDTH + 1) * self.ROW_WIDTH + "\n")
        return result

    def print_row(self, row_index: int):
        first_piece_index = row_index * self.ROW_WIDTH
        last_piece_index = first_piece_index + self.ROW_WIDTH
        line_printer = LinePrinter.create(self.__pieces[first_piece_index:last_piece_index])
        return line_printer.print_row_in_3_lines()
