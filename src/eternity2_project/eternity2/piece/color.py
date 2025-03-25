from src.eternity2_project.eternity2.piece.css_color_code import CSSColorCode


class Color:
    def __init__(self, color_id: int, main_color: CSSColorCode, secondary_code: CSSColorCode, name: str):
        self.__id: int = color_id
        self.__main_color: CSSColorCode = main_color
        self.__secondary_color: CSSColorCode = secondary_code
        self.__name: str = name

    def __str__(self) -> str:
        return self.__name