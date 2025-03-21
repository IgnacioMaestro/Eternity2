from typing import Self


class Square:
    def __init__(self, column: int, row: int):
        self.__column = column
        self.__row = row

    def is_corner(self) -> bool:
        is_top_left_corner: bool = self.__column == 0 and self.__row == 0
        is_top_right_corner: bool = self.__column == 15 and self.__row == 0
        is_bottom_left_corner: bool = self.__column == 0 and self.__row == 15
        is_bottom_right_corner: bool = self.__column == 15 and self.__row == 15
        return is_top_left_corner or is_top_right_corner or is_bottom_left_corner or is_bottom_right_corner

    def is_up_to(self, square: Self) -> bool:
        return self.__row == square.get_row() + 1 and self.__column == square.get_column

    def is_right_to(self, square: Self) -> bool:
        return self.__row == square.get_row and self.__column == square.get_column + 1

    def is_down_to(self, square: Self) -> bool:
        return self.__row == square.get_row - 1 and self.__column == square.get_column

    def is_left_to(self, square: Self) -> bool:
        return self.__row == square.get_row and self.__column == square.get_column - 1
