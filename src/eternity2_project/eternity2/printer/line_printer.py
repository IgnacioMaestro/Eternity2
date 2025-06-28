from typing import Optional, List, Self

from src.eternity2_project.eternity2.rotated_piece.rotated_piece import RotatedPiece


class LinePrinter:
    PIECE_WIDTH = 52

    def __init__(self, pieces: List[Optional[RotatedPiece]]):
        self.__pieces = pieces

    @classmethod
    def create(cls, pieces: List[Optional[RotatedPiece]]) -> Self:
        if len(pieces) != 16:
            raise ValueError("LinePrinter requires exactly 16 pieces")
        return cls(pieces)

    def __print_center_text(self, text: str) -> str:
        return text.center(self.PIECE_WIDTH)

    def __print_two_texts(self, piece: RotatedPiece) -> str:
        left_color = str(piece.get_left_color())
        right_color = str(piece.get_right_color())
        return left_color.ljust(self.PIECE_WIDTH - len(right_color)) + right_color

    def print_row_in_3_lines(self) -> str:
        up_line = self.print_row_up_line()
        center_line = self.print_row_center_line()
        down_line = self.print_row_down_line()
        return up_line + center_line + down_line

    def print_row_up_line(self) -> str:
        up_line = ""
        for piece in self.__pieces:
            up_line += self.print_up_piece(piece) + "|"
        return up_line[:-1] + "\n"

    def print_up_piece(self, piece: Optional[RotatedPiece]) -> str:
        if piece is None:
            return " " * LinePrinter.PIECE_WIDTH
        else:
            return self.__print_center_text(str(piece.get_up_color()))

    def print_row_center_line(self) -> str:
        center_line = ""
        for piece in self.__pieces:
            center_line += self.print_center_piece(piece) + "|"
        return center_line[:-1] + "\n"

    def print_center_piece(self, piece: Optional[RotatedPiece]) -> str:
        if piece is None:
            return " " * LinePrinter.PIECE_WIDTH
        else:
            return self.__print_two_texts(piece)

    def print_row_down_line(self) -> str:
        down_line = ""
        for piece in self.__pieces:
            down_line += self.print_down_piece(piece) + "|"
        return down_line[:-1] + "\n"

    def print_down_piece(self, piece: Optional[RotatedPiece]) -> str:
        if piece is None:
            return " " * LinePrinter.PIECE_WIDTH
        else:
            return self.__print_center_text(str(piece.get_down_color()))

