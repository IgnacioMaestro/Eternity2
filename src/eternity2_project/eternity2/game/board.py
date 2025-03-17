from src.eternity2_project.eternity2.game.square import Square


class Board:
    def __init__(self):
        self.__squares: list[list[Square]] = [[]]
        for column in range(256):
            for row in range(256):
                self.__squares[column].append(Square(column, row))
