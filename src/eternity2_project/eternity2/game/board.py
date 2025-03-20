from src.eternity2_project.eternity2.game.square import Square


class Board:
    def __init__(self):
        self.__squares: list[list[Square]] = [[]]
        for column in range(256):
            self.__squares.append([])
            for row in range(256):
                self.__squares[column].append(Square(column, row))

    def get_square(self, column: int, row: int) -> Square:
        return self.__squares[column][row]

