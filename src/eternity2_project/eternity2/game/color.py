from src.eternity2_project.eternity2.game.css_color_code import CSSColorCode


class Color:
    def __init__(self, color_id: int, code: CSSColorCode, name: str):
        self.__id: int = color_id
        self.__code: CSSColorCode = code
        self.__name: str = name

    @property
    def code(self):
        return self.__code

    @property
    def name(self):
        return self.__name
