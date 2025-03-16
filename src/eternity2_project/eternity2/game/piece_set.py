from .color import Color
from .css_color_code import CSSColorCode
from .piece import Piece


class PieceSet:
    BORDER = Color(1, CSSColorCode('808080'), CSSColorCode('808080'), "Border")
    ORANGE_BLUE = Color(2, CSSColorCode('FFA500'), CSSColorCode('0000FF'), "OrangeBlueCross")
    PINK_BLUE = Color(3, CSSColorCode('FFC0CB'), CSSColorCode('0000FF'), "PinkBlueCross")
    GREEN_DARK_BLUE = Color(4, CSSColorCode('00FF00'), CSSColorCode('00008B'), "GreenDarkBlueHexagon")
    DARK_BLUE_YELLOW = Color(5, CSSColorCode('00008B'), CSSColorCode('FFFF00'), "DarkBlueYellowFlower")
    PINK_YELLOW_CROSS_CIRCLE = Color(6, CSSColorCode('FFC0CB'), CSSColorCode('FFFF00'), "PinkYellowCrossCircle")
    PURPLE_BLUE = Color(7, CSSColorCode('800080'), CSSColorCode('0000FF'), "PurpleBlueSpade")
    PURPLE_YELLOW = Color(8, CSSColorCode('800080'), CSSColorCode('FFFF00'), "PurpleYellowCrossCircle")
    BROWN_ORANGE = Color(9, CSSColorCode('A52A2A'), CSSColorCode('FFA500'), "BrownOrange")
    GREEN_ORANGE = Color(10, CSSColorCode('00FF00'), CSSColorCode('FFA500'), "GreenOrangeSpade")
    BLUE_PINK_CASTLE = Color(11, CSSColorCode('0000FF'), CSSColorCode('FFC0CB'), "BluePinkCastle")
    YELLOW_GREEN = Color(12, CSSColorCode('FFFF00'), CSSColorCode('00FF00'), "YellowGreenSquare")
    DARK_BLUE_ORANGE = Color(13, CSSColorCode('00008B'), CSSColorCode('FFA500'), "DarkBlueOrangeCrossCircle")
    PINK_YELLOW_CASTLE = Color(14, CSSColorCode('FFC0CB'), CSSColorCode('FFFF00'), "PinkYellowCastle")
    YELLOW_BLUE = Color(15, CSSColorCode('FFFF00'), CSSColorCode('0000FF'), "YellowBlueStar")
    GREEN_PINK = Color(16, CSSColorCode('00FF00'), CSSColorCode('FFC0CB'), "GreenPinkCrossCircle")
    MAROON_YELLOW = Color(17, CSSColorCode('800000'), CSSColorCode('FFFF00'), "MaroonYellowStar")
    BLUE_PINK_SPADE = Color(18, CSSColorCode('0000FF'), CSSColorCode('FFC0CB'), "BluePinkSpade")
    YELLOW_DARK_BLUE = Color(19, CSSColorCode('FFFF00'), CSSColorCode('00008B'), "YellowDarkBlueCastle")
    ORANGE_PURPLE = Color(20, CSSColorCode('FFA500'), CSSColorCode('800080'), "OrangePurpleStar")
    DARK_BLUE_BLUE = Color(21, CSSColorCode('00008B'), CSSColorCode('0000FF'), "DarkBlueBlueSquare")
    DARK_BLUE_PINK = Color(22, CSSColorCode('00008B'), CSSColorCode('FFC0CB'), "DarkBluePinkCrossCircle")
    MAROON_GREEN = Color(23, CSSColorCode('800000'), CSSColorCode('00FF00'), "MaroonGreenCrossCircle")
    __piece_list: list[Piece]

    def __init__(self):
        pieces_1_17 = [
            Piece(1, PieceSet.ORANGE_BLUE, PieceSet.PINK_BLUE, PieceSet.BORDER, PieceSet.BORDER),
            Piece(2, PieceSet.ORANGE_BLUE, PieceSet.GREEN_DARK_BLUE, PieceSet.BORDER, PieceSet.BORDER),
            Piece(3, PieceSet.DARK_BLUE_YELLOW, PieceSet.PINK_BLUE, PieceSet.BORDER, PieceSet.BORDER),
            Piece(4, PieceSet.PINK_BLUE, PieceSet.DARK_BLUE_YELLOW, PieceSet.BORDER, PieceSet.BORDER),
            Piece(5, PieceSet.PINK_YELLOW_CROSS_CIRCLE, PieceSet.ORANGE_BLUE, PieceSet.BORDER, PieceSet.ORANGE_BLUE),
            Piece(6, PieceSet.PURPLE_BLUE, PieceSet.DARK_BLUE_YELLOW, PieceSet.BORDER, PieceSet.ORANGE_BLUE),
            Piece(7, PieceSet.PURPLE_YELLOW, PieceSet.ORANGE_BLUE, PieceSet.BORDER, PieceSet.ORANGE_BLUE),
            Piece(8, PieceSet.PURPLE_YELLOW, PieceSet.BROWN_ORANGE, PieceSet.BORDER, PieceSet.ORANGE_BLUE),
            Piece(9, PieceSet.GREEN_ORANGE, PieceSet.PINK_BLUE, PieceSet.BORDER, PieceSet.ORANGE_BLUE),
            Piece(10, PieceSet.BLUE_PINK_CASTLE, PieceSet.GREEN_DARK_BLUE, PieceSet.BORDER, PieceSet.ORANGE_BLUE),
            Piece(11, PieceSet.YELLOW_GREEN, PieceSet.DARK_BLUE_YELLOW, PieceSet.BORDER, PieceSet.ORANGE_BLUE),
            Piece(12, PieceSet.DARK_BLUE_ORANGE, PieceSet.GREEN_DARK_BLUE, PieceSet.BORDER, PieceSet.ORANGE_BLUE),
            Piece(13, PieceSet.DARK_BLUE_ORANGE, PieceSet.BROWN_ORANGE, PieceSet.BORDER, PieceSet.ORANGE_BLUE),
            Piece(14, PieceSet.PINK_YELLOW_CASTLE, PieceSet.GREEN_DARK_BLUE, PieceSet.BORDER, PieceSet.ORANGE_BLUE),
            Piece(15, PieceSet.PURPLE_BLUE, PieceSet.ORANGE_BLUE, PieceSet.BORDER, PieceSet.DARK_BLUE_YELLOW),
            Piece(16, PieceSet.YELLOW_BLUE, PieceSet.PINK_BLUE, PieceSet.BORDER, PieceSet.DARK_BLUE_YELLOW),
            Piece(17, PieceSet.GREEN_PINK, PieceSet.BROWN_ORANGE, PieceSet.BORDER, PieceSet.DARK_BLUE_YELLOW)]
        pieces_18_34 = [
            Piece(18, PieceSet.MAROON_YELLOW, PieceSet.BROWN_ORANGE, PieceSet.BORDER, PieceSet.DARK_BLUE_YELLOW),
            Piece(19, PieceSet.BLUE_PINK_CASTLE, PieceSet.DARK_BLUE_YELLOW, PieceSet.BORDER, PieceSet.DARK_BLUE_YELLOW),
            Piece(20, PieceSet.YELLOW_GREEN, PieceSet.DARK_BLUE_YELLOW, PieceSet.BORDER, PieceSet.DARK_BLUE_YELLOW),
            Piece(21, PieceSet.BLUE_PINK_SPADE, PieceSet.GREEN_DARK_BLUE, PieceSet.BORDER, PieceSet.DARK_BLUE_YELLOW),
            Piece(22, PieceSet.YELLOW_DARK_BLUE, PieceSet.ORANGE_BLUE, PieceSet.BORDER, PieceSet.DARK_BLUE_YELLOW),
            Piece(23, PieceSet.YELLOW_DARK_BLUE, PieceSet.BROWN_ORANGE, PieceSet.BORDER, PieceSet.DARK_BLUE_YELLOW),
            Piece(24, PieceSet.ORANGE_PURPLE, PieceSet.ORANGE_BLUE, PieceSet.BORDER, PieceSet.DARK_BLUE_YELLOW),
            Piece(25, PieceSet.PINK_YELLOW_CASTLE, PieceSet.BROWN_ORANGE, PieceSet.BORDER, PieceSet.DARK_BLUE_YELLOW),
            Piece(26,
                  PieceSet.PINK_YELLOW_CROSS_CIRCLE, PieceSet.DARK_BLUE_YELLOW, PieceSet.BORDER, PieceSet.PINK_BLUE),
            Piece(27,
                  PieceSet.PINK_YELLOW_CROSS_CIRCLE, PieceSet.PINK_BLUE, PieceSet.BORDER, PieceSet.PINK_BLUE),
            Piece(28,
                  PieceSet.PURPLE_BLUE, PieceSet.PINK_BLUE, PieceSet.BORDER, PieceSet.PINK_BLUE),
            Piece(29,
                  PieceSet.YELLOW_BLUE, PieceSet.PINK_BLUE, PieceSet.BORDER, PieceSet.PINK_BLUE),
            Piece(30,
                  PieceSet.BLUE_PINK_CASTLE, PieceSet.BROWN_ORANGE, PieceSet.BORDER, PieceSet.PINK_BLUE),
            Piece(31,
                  PieceSet.YELLOW_GREEN, PieceSet.DARK_BLUE_YELLOW, PieceSet.BORDER, PieceSet.PINK_BLUE),
            Piece(32,
                  PieceSet.ORANGE_PURPLE, PieceSet.PINK_BLUE, PieceSet.BORDER, PieceSet.PINK_BLUE),
            Piece(33,
                  PieceSet.DARK_BLUE_ORANGE, PieceSet.DARK_BLUE_YELLOW, PieceSet.BORDER, PieceSet.PINK_BLUE),
            Piece(34,
                  PieceSet.DARK_BLUE_ORANGE, PieceSet.GREEN_DARK_BLUE, PieceSet.BORDER, PieceSet.PINK_BLUE)
        ]
        pieces_35_51 = [
            Piece(35, PieceSet.DARK_BLUE_BLUE, PieceSet.BROWN_ORANGE, PieceSet.BORDER, PieceSet.PINK_BLUE),
            Piece(36, PieceSet.DARK_BLUE_PINK, PieceSet.GREEN_DARK_BLUE, PieceSet.BORDER, PieceSet.PINK_BLUE),
            Piece(37, PieceSet.YELLOW_BLUE, PieceSet.ORANGE_BLUE, PieceSet.BORDER, PieceSet.GREEN_DARK_BLUE),
            Piece(38, PieceSet.MAROON_GREEN, PieceSet.BROWN_ORANGE, PieceSet.BORDER, PieceSet.GREEN_DARK_BLUE),
            Piece(39, PieceSet.GREEN_ORANGE, PieceSet.BROWN_ORANGE, PieceSet.BORDER, PieceSet.GREEN_DARK_BLUE),
            Piece(40, PieceSet.MAROON_YELLOW, PieceSet.DARK_BLUE_YELLOW, PieceSet.BORDER, PieceSet.GREEN_DARK_BLUE),
            Piece(41, PieceSet.MAROON_YELLOW, PieceSet.PINK_BLUE, PieceSet.BORDER, PieceSet.GREEN_DARK_BLUE),
            Piece(42, PieceSet.YELLOW_GREEN, PieceSet.ORANGE_BLUE, PieceSet.BORDER, PieceSet.GREEN_DARK_BLUE),
            Piece(43, PieceSet.YELLOW_GREEN, PieceSet.DARK_BLUE_YELLOW, PieceSet.BORDER, PieceSet.GREEN_DARK_BLUE),
            Piece(44, PieceSet.YELLOW_GREEN, PieceSet.PINK_BLUE, PieceSet.BORDER, PieceSet.GREEN_DARK_BLUE),
            Piece(45, PieceSet.BLUE_PINK_SPADE, PieceSet.ORANGE_BLUE, PieceSet.BORDER, PieceSet.GREEN_DARK_BLUE),
            Piece(46, PieceSet.ORANGE_PURPLE, PieceSet.GREEN_DARK_BLUE, PieceSet.BORDER, PieceSet.GREEN_DARK_BLUE),
            Piece(47, PieceSet.DARK_BLUE_ORANGE, PieceSet.GREEN_DARK_BLUE, PieceSet.BORDER, PieceSet.GREEN_DARK_BLUE),
            Piece(48, PieceSet.DARK_BLUE_BLUE, PieceSet.GREEN_DARK_BLUE, PieceSet.BORDER, PieceSet.GREEN_DARK_BLUE),
            Piece(49, PieceSet.PINK_YELLOW_CROSS_CIRCLE, PieceSet.BROWN_ORANGE, PieceSet.BORDER, PieceSet.BROWN_ORANGE),
            Piece(50, PieceSet.PURPLE_BLUE, PieceSet.ORANGE_BLUE, PieceSet.BORDER, PieceSet.BROWN_ORANGE),
            Piece(51, PieceSet.PURPLE_BLUE, PieceSet.DARK_BLUE_YELLOW, PieceSet.BORDER, PieceSet.BROWN_ORANGE)
        ]
        self.__piece_list = []
        self.__piece_list.extend(pieces_1_17)
        self.__piece_list.extend(pieces_18_34)
        self.__piece_list.extend(pieces_35_51)
