from .color import Color
from .css_color_code import CSSColorCode
from .piece import Piece


class PieceSet:
    BORDER = Color(1, CSSColorCode('808080'), CSSColorCode('808080'), "Border")
    ORANGE_BLUE = Color(2, CSSColorCode('FFA500'), CSSColorCode('0000FF'), "OrangeBlueCross")
    PINK_BLUE = Color(3, CSSColorCode('FFC0CB'), CSSColorCode('0000FF'), "PinkBlueCross")
    GREEN_DARK_BLUE = Color(4, CSSColorCode('00FF00'), CSSColorCode('00008B'), "GreenDarkBlueHexagon")
    DARK_BLUE_YELLOW = Color(5, CSSColorCode('00008B'), CSSColorCode('FFFF00'), "DarkBlueYellowFlower")
    PINK_YELLOW_DOTTED_CROSS = Color(6, CSSColorCode('FFC0CB'), CSSColorCode('FFFF00'), "PinkYellowDottedCross")
    PURPLE_BLUE_SPADE = Color(7, CSSColorCode('800080'), CSSColorCode('0000FF'), "PurpleBlueSpade")
    PURPLE_YELLOW_CROSS_IN_CIRCLE = Color(8, CSSColorCode('800080'), CSSColorCode('FFFF00'), "PurpleYellowCrossCircle")
    BROWN_ORANGE = Color(9, CSSColorCode('A52A2A'), CSSColorCode('FFA500'), "BrownOrange")
    GREEN_ORANGE_SPADE = Color(10, CSSColorCode('00FF00'), CSSColorCode('FFA500'), "GreenOrangeSpade")
    BLUE_PINK_CASTLE = Color(11, CSSColorCode('0000FF'), CSSColorCode('FFC0CB'), "BluePinkCastle")
    YELLOW_GREEN_SQUARE = Color(12, CSSColorCode('FFFF00'), CSSColorCode('00FF00'), "YellowGreenSquare")
    DARK_BLUE_ORANGE_DOTTED_CROSS = Color(
        13, CSSColorCode('00008B'), CSSColorCode('FFA500'), "DarkBlueOrangeCrossCircle")
    PINK_YELLOW_CASTLE = Color(14, CSSColorCode('FFC0CB'), CSSColorCode('FFFF00'), "PinkYellowCastle")
    YELLOW_BLUE_STAR = Color(15, CSSColorCode('FFFF00'), CSSColorCode('0000FF'), "YellowBlueStar")
    GREEN_PINK_DOTTED_CROSS = Color(16, CSSColorCode('00FF00'), CSSColorCode('FFC0CB'), "GreenPinkDottedCross")
    MAROON_YELLOW_STAR = Color(17, CSSColorCode('800000'), CSSColorCode('FFFF00'), "MaroonYellowStar")
    BLUE_PINK_SPADE = Color(18, CSSColorCode('0000FF'), CSSColorCode('FFC0CB'), "BluePinkSpade")
    YELLOW_DARK_BLUE_CASTLE = Color(19, CSSColorCode('FFFF00'), CSSColorCode('00008B'), "YellowDarkBlueCastle")
    ORANGE_PURPLE_STAR = Color(20, CSSColorCode('FFA500'), CSSColorCode('800080'), "OrangePurpleStar")
    DARK_BLUE_BLUE_SQUARE = Color(21, CSSColorCode('00008B'), CSSColorCode('0000FF'), "DarkBlueBlueSquare")
    DARK_BLUE_PINK_CROSS_IN_CIRCLE = Color(
        22, CSSColorCode('00008B'), CSSColorCode('FFC0CB'), "DarkBluePinkCrossCircle")
    MAROON_GREEN_CROSS_IN_CIRCLE = Color(23, CSSColorCode('800000'), CSSColorCode('00FF00'), "MaroonGreenCrossCircle")
    __piece_list: list[Piece]

    def __init__(self):
        pieces_1_16 = [
            Piece(1, PieceSet.ORANGE_BLUE, PieceSet.PINK_BLUE, PieceSet.BORDER, PieceSet.BORDER),
            Piece(2, PieceSet.ORANGE_BLUE, PieceSet.GREEN_DARK_BLUE, PieceSet.BORDER, PieceSet.BORDER),
            Piece(3, PieceSet.DARK_BLUE_YELLOW, PieceSet.PINK_BLUE, PieceSet.BORDER, PieceSet.BORDER),
            Piece(4, PieceSet.PINK_BLUE, PieceSet.DARK_BLUE_YELLOW, PieceSet.BORDER, PieceSet.BORDER),
            Piece(5, PieceSet.PINK_YELLOW_DOTTED_CROSS, PieceSet.ORANGE_BLUE, PieceSet.BORDER, PieceSet.ORANGE_BLUE),
            Piece(6, PieceSet.PURPLE_BLUE_SPADE, PieceSet.DARK_BLUE_YELLOW, PieceSet.BORDER, PieceSet.ORANGE_BLUE),
            Piece(7, PieceSet.PURPLE_YELLOW_CROSS_IN_CIRCLE, PieceSet.ORANGE_BLUE, PieceSet.BORDER,
                  PieceSet.ORANGE_BLUE),
            Piece(8, PieceSet.PURPLE_YELLOW_CROSS_IN_CIRCLE, PieceSet.BROWN_ORANGE, PieceSet.BORDER,
                  PieceSet.ORANGE_BLUE),
            Piece(9, PieceSet.GREEN_ORANGE_SPADE, PieceSet.PINK_BLUE, PieceSet.BORDER, PieceSet.ORANGE_BLUE),
            Piece(10, PieceSet.BLUE_PINK_CASTLE, PieceSet.GREEN_DARK_BLUE, PieceSet.BORDER, PieceSet.ORANGE_BLUE),
            Piece(11, PieceSet.YELLOW_GREEN_SQUARE, PieceSet.DARK_BLUE_YELLOW, PieceSet.BORDER, PieceSet.ORANGE_BLUE),
            Piece(12, PieceSet.DARK_BLUE_ORANGE_DOTTED_CROSS, PieceSet.GREEN_DARK_BLUE, PieceSet.BORDER,
                  PieceSet.ORANGE_BLUE),
            Piece(13, PieceSet.DARK_BLUE_ORANGE_DOTTED_CROSS, PieceSet.BROWN_ORANGE, PieceSet.BORDER,
                  PieceSet.ORANGE_BLUE),
            Piece(14, PieceSet.PINK_YELLOW_CASTLE, PieceSet.GREEN_DARK_BLUE, PieceSet.BORDER, PieceSet.ORANGE_BLUE),
            Piece(15, PieceSet.PURPLE_BLUE_SPADE, PieceSet.ORANGE_BLUE, PieceSet.BORDER, PieceSet.DARK_BLUE_YELLOW),
            Piece(16, PieceSet.YELLOW_BLUE_STAR, PieceSet.PINK_BLUE, PieceSet.BORDER, PieceSet.DARK_BLUE_YELLOW)
            ]
        pieces_17_32 = [
            Piece(17, PieceSet.GREEN_PINK_DOTTED_CROSS, PieceSet.BROWN_ORANGE, PieceSet.BORDER,
                  PieceSet.DARK_BLUE_YELLOW),
            Piece(18, PieceSet.MAROON_YELLOW_STAR, PieceSet.BROWN_ORANGE, PieceSet.BORDER, PieceSet.DARK_BLUE_YELLOW),
            Piece(19, PieceSet.BLUE_PINK_CASTLE, PieceSet.DARK_BLUE_YELLOW, PieceSet.BORDER, PieceSet.DARK_BLUE_YELLOW),
            Piece(20, PieceSet.YELLOW_GREEN_SQUARE, PieceSet.DARK_BLUE_YELLOW, PieceSet.BORDER,
                  PieceSet.DARK_BLUE_YELLOW),
            Piece(21, PieceSet.BLUE_PINK_SPADE, PieceSet.GREEN_DARK_BLUE, PieceSet.BORDER, PieceSet.DARK_BLUE_YELLOW),
            Piece(22, PieceSet.YELLOW_DARK_BLUE_CASTLE, PieceSet.ORANGE_BLUE, PieceSet.BORDER,
                  PieceSet.DARK_BLUE_YELLOW),
            Piece(23, PieceSet.YELLOW_DARK_BLUE_CASTLE, PieceSet.BROWN_ORANGE, PieceSet.BORDER,
                  PieceSet.DARK_BLUE_YELLOW),
            Piece(24, PieceSet.ORANGE_PURPLE_STAR, PieceSet.ORANGE_BLUE, PieceSet.BORDER, PieceSet.DARK_BLUE_YELLOW),
            Piece(25, PieceSet.PINK_YELLOW_CASTLE, PieceSet.BROWN_ORANGE, PieceSet.BORDER, PieceSet.DARK_BLUE_YELLOW),
            Piece(26,
                  PieceSet.PINK_YELLOW_DOTTED_CROSS, PieceSet.DARK_BLUE_YELLOW, PieceSet.BORDER, PieceSet.PINK_BLUE),
            Piece(27,
                  PieceSet.PINK_YELLOW_DOTTED_CROSS, PieceSet.PINK_BLUE, PieceSet.BORDER, PieceSet.PINK_BLUE),
            Piece(28,
                  PieceSet.PURPLE_BLUE_SPADE, PieceSet.PINK_BLUE, PieceSet.BORDER, PieceSet.PINK_BLUE),
            Piece(29,
                  PieceSet.YELLOW_BLUE_STAR, PieceSet.PINK_BLUE, PieceSet.BORDER, PieceSet.PINK_BLUE),
            Piece(30,
                  PieceSet.BLUE_PINK_CASTLE, PieceSet.BROWN_ORANGE, PieceSet.BORDER, PieceSet.PINK_BLUE),
            Piece(31,
                  PieceSet.YELLOW_GREEN_SQUARE, PieceSet.DARK_BLUE_YELLOW, PieceSet.BORDER, PieceSet.PINK_BLUE),
            Piece(32,
                  PieceSet.ORANGE_PURPLE_STAR, PieceSet.PINK_BLUE, PieceSet.BORDER, PieceSet.PINK_BLUE)
        ]
        pieces_33_48 = [
            Piece(33,
                  PieceSet.DARK_BLUE_ORANGE_DOTTED_CROSS, PieceSet.DARK_BLUE_YELLOW, PieceSet.BORDER,
                  PieceSet.PINK_BLUE),
            Piece(34,
                  PieceSet.DARK_BLUE_ORANGE_DOTTED_CROSS, PieceSet.GREEN_DARK_BLUE, PieceSet.BORDER, PieceSet.PINK_BLUE),
            Piece(35, PieceSet.DARK_BLUE_BLUE_SQUARE, PieceSet.BROWN_ORANGE, PieceSet.BORDER, PieceSet.PINK_BLUE),
            Piece(36, PieceSet.DARK_BLUE_PINK_CROSS_IN_CIRCLE, PieceSet.GREEN_DARK_BLUE, PieceSet.BORDER,
                  PieceSet.PINK_BLUE),
            Piece(37, PieceSet.YELLOW_BLUE_STAR, PieceSet.ORANGE_BLUE, PieceSet.BORDER, PieceSet.GREEN_DARK_BLUE),
            Piece(38, PieceSet.MAROON_GREEN_CROSS_IN_CIRCLE, PieceSet.BROWN_ORANGE, PieceSet.BORDER,
                  PieceSet.GREEN_DARK_BLUE),
            Piece(39, PieceSet.GREEN_ORANGE_SPADE, PieceSet.BROWN_ORANGE, PieceSet.BORDER, PieceSet.GREEN_DARK_BLUE),
            Piece(40, PieceSet.MAROON_YELLOW_STAR, PieceSet.DARK_BLUE_YELLOW, PieceSet.BORDER,
                  PieceSet.GREEN_DARK_BLUE),
            Piece(41, PieceSet.MAROON_YELLOW_STAR, PieceSet.PINK_BLUE, PieceSet.BORDER, PieceSet.GREEN_DARK_BLUE),
            Piece(42, PieceSet.YELLOW_GREEN_SQUARE, PieceSet.ORANGE_BLUE, PieceSet.BORDER, PieceSet.GREEN_DARK_BLUE),
            Piece(43, PieceSet.YELLOW_GREEN_SQUARE, PieceSet.DARK_BLUE_YELLOW, PieceSet.BORDER,
                  PieceSet.GREEN_DARK_BLUE),
            Piece(44, PieceSet.YELLOW_GREEN_SQUARE, PieceSet.PINK_BLUE, PieceSet.BORDER, PieceSet.GREEN_DARK_BLUE),
            Piece(45, PieceSet.BLUE_PINK_SPADE, PieceSet.ORANGE_BLUE, PieceSet.BORDER, PieceSet.GREEN_DARK_BLUE),
            Piece(46, PieceSet.ORANGE_PURPLE_STAR, PieceSet.GREEN_DARK_BLUE, PieceSet.BORDER, PieceSet.GREEN_DARK_BLUE),
            Piece(47, PieceSet.DARK_BLUE_ORANGE_DOTTED_CROSS, PieceSet.GREEN_DARK_BLUE, PieceSet.BORDER,
                  PieceSet.GREEN_DARK_BLUE),
            Piece(48, PieceSet.DARK_BLUE_BLUE_SQUARE, PieceSet.GREEN_DARK_BLUE, PieceSet.BORDER,
                  PieceSet.GREEN_DARK_BLUE)
        ]
        pieces_49_64 = [
            Piece(49, PieceSet.PINK_YELLOW_DOTTED_CROSS, PieceSet.BROWN_ORANGE, PieceSet.BORDER, PieceSet.BROWN_ORANGE),
            Piece(50, PieceSet.PURPLE_BLUE_SPADE, PieceSet.ORANGE_BLUE, PieceSet.BORDER, PieceSet.BROWN_ORANGE),
            Piece(51, PieceSet.PURPLE_BLUE_SPADE, PieceSet.DARK_BLUE_YELLOW, PieceSet.BORDER, PieceSet.BROWN_ORANGE),
            Piece(52, PieceSet.PURPLE_YELLOW_CROSS_IN_CIRCLE, PieceSet.ORANGE_BLUE, PieceSet.BORDER,
                  PieceSet.BROWN_ORANGE),
            Piece(53, PieceSet.BLUE_PINK_CASTLE, PieceSet.GREEN_DARK_BLUE, PieceSet.BORDER, PieceSet.BROWN_ORANGE),
            Piece(54, PieceSet.BLUE_PINK_SPADE, PieceSet.ORANGE_BLUE, PieceSet.BORDER, PieceSet.BROWN_ORANGE),
            Piece(55, PieceSet.BLUE_PINK_SPADE, PieceSet.BROWN_ORANGE, PieceSet.BORDER, PieceSet.BROWN_ORANGE),
            Piece(56, PieceSet.DARK_BLUE_ORANGE_DOTTED_CROSS, PieceSet.PINK_BLUE, PieceSet.BORDER,
                  PieceSet.BROWN_ORANGE),
            Piece(57, PieceSet.DARK_BLUE_BLUE_SQUARE, PieceSet.ORANGE_BLUE, PieceSet.BORDER, PieceSet.BROWN_ORANGE),
            Piece(58, PieceSet.DARK_BLUE_BLUE_SQUARE, PieceSet.BROWN_ORANGE, PieceSet.BORDER, PieceSet.BROWN_ORANGE),
            Piece(59, PieceSet.PINK_YELLOW_CASTLE, PieceSet.DARK_BLUE_YELLOW, PieceSet.BORDER, PieceSet.BROWN_ORANGE),
            Piece(60, PieceSet.DARK_BLUE_PINK_CROSS_IN_CIRCLE, PieceSet.ORANGE_BLUE, PieceSet.BORDER,
                  PieceSet.BROWN_ORANGE),
            Piece(61,
                  PieceSet.PURPLE_YELLOW_CROSS_IN_CIRCLE, PieceSet.YELLOW_BLUE_STAR,
                  PieceSet.PINK_YELLOW_DOTTED_CROSS, PieceSet.PINK_YELLOW_DOTTED_CROSS),
            Piece(62,
                  PieceSet.GREEN_PINK_DOTTED_CROSS, PieceSet.BLUE_PINK_CASTLE,
                  PieceSet.PINK_YELLOW_DOTTED_CROSS, PieceSet.PINK_YELLOW_DOTTED_CROSS),
            Piece(63,
                  PieceSet.PURPLE_BLUE_SPADE, PieceSet.MAROON_GREEN_CROSS_IN_CIRCLE,
                  PieceSet.PINK_YELLOW_DOTTED_CROSS, PieceSet.PURPLE_BLUE_SPADE),
            Piece(64,
                  PieceSet.PINK_YELLOW_DOTTED_CROSS, PieceSet.DARK_BLUE_ORANGE_DOTTED_CROSS,
                  PieceSet.PINK_YELLOW_DOTTED_CROSS, PieceSet.YELLOW_BLUE_STAR)
        ]
        pieces_65_80 = [
            Piece(65,
                  PieceSet.YELLOW_BLUE_STAR, PieceSet.DARK_BLUE_PINK_CROSS_IN_CIRCLE,
                  PieceSet.PINK_YELLOW_DOTTED_CROSS, PieceSet.YELLOW_BLUE_STAR),
            Piece(66,
                  PieceSet.GREEN_PINK_DOTTED_CROSS, PieceSet.GREEN_PINK_DOTTED_CROSS,
                  PieceSet.PINK_YELLOW_DOTTED_CROSS, PieceSet.YELLOW_BLUE_STAR),
            Piece(67,
                  PieceSet.GREEN_ORANGE_SPADE, PieceSet.PURPLE_BLUE_SPADE,
                  PieceSet.PINK_YELLOW_DOTTED_CROSS, PieceSet.YELLOW_BLUE_STAR),
            Piece(68, PieceSet.ORANGE_PURPLE_STAR, PieceSet.PURPLE_YELLOW_CROSS_IN_CIRCLE,
                  PieceSet.PINK_YELLOW_DOTTED_CROSS, PieceSet.YELLOW_BLUE_STAR),
            Piece(69, PieceSet.DARK_BLUE_PINK_CROSS_IN_CIRCLE, PieceSet.DARK_BLUE_ORANGE_DOTTED_CROSS,
                  PieceSet.PINK_YELLOW_DOTTED_CROSS, PieceSet.YELLOW_BLUE_STAR),
            Piece(70, PieceSet.MAROON_GREEN_CROSS_IN_CIRCLE, PieceSet.BLUE_PINK_CASTLE,
                  PieceSet.PINK_YELLOW_DOTTED_CROSS, PieceSet.MAROON_GREEN_CROSS_IN_CIRCLE),
            Piece(71, PieceSet.BLUE_PINK_CASTLE, PieceSet.YELLOW_DARK_BLUE_CASTLE,
                  PieceSet.PINK_YELLOW_DOTTED_CROSS, PieceSet.MAROON_GREEN_CROSS_IN_CIRCLE),
            Piece(72, PieceSet.GREEN_PINK_DOTTED_CROSS, PieceSet.YELLOW_BLUE_STAR,
                  PieceSet.PINK_YELLOW_DOTTED_CROSS, PieceSet.GREEN_ORANGE_SPADE),
            Piece(73, PieceSet.YELLOW_GREEN_SQUARE, PieceSet.BLUE_PINK_SPADE,
                  PieceSet.PINK_YELLOW_DOTTED_CROSS, PieceSet.GREEN_ORANGE_SPADE),
            Piece(74, PieceSet.ORANGE_PURPLE_STAR, PieceSet.YELLOW_GREEN_SQUARE,
                  PieceSet.PINK_YELLOW_DOTTED_CROSS, PieceSet.GREEN_ORANGE_SPADE),
            Piece(75, PieceSet.DARK_BLUE_ORANGE_DOTTED_CROSS, PieceSet.MAROON_GREEN_CROSS_IN_CIRCLE,
                  PieceSet.PINK_YELLOW_DOTTED_CROSS, PieceSet.GREEN_ORANGE_SPADE),
            Piece(76, PieceSet.GREEN_PINK_DOTTED_CROSS, PieceSet.YELLOW_GREEN_SQUARE,
                  PieceSet.PINK_YELLOW_DOTTED_CROSS, PieceSet.MAROON_YELLOW_STAR),
            Piece(77, PieceSet.MAROON_YELLOW_STAR, PieceSet.YELLOW_GREEN_SQUARE,
                  PieceSet.PINK_YELLOW_DOTTED_CROSS, PieceSet.MAROON_YELLOW_STAR),
            Piece(78, PieceSet.MAROON_GREEN_CROSS_IN_CIRCLE, PieceSet.DARK_BLUE_BLUE_SQUARE,
                  PieceSet.PINK_YELLOW_DOTTED_CROSS, PieceSet.BLUE_PINK_CASTLE),
            Piece(79, PieceSet.ORANGE_PURPLE_STAR, PieceSet.MAROON_GREEN_CROSS_IN_CIRCLE,
                  PieceSet.PINK_YELLOW_DOTTED_CROSS, PieceSet.BLUE_PINK_CASTLE),
            Piece(80, PieceSet.DARK_BLUE_BLUE_SQUARE, PieceSet.PINK_YELLOW_CASTLE,
                  PieceSet.PINK_YELLOW_DOTTED_CROSS, PieceSet.BLUE_PINK_CASTLE),
            Piece(81, PieceSet.MAROON_YELLOW_STAR, PieceSet.YELLOW_BLUE_STAR,
                  PieceSet.PINK_YELLOW_DOTTED_CROSS, PieceSet.YELLOW_GREEN_SQUARE),
            Piece(82, PieceSet.YELLOW_BLUE_STAR, PieceSet.YELLOW_BLUE_STAR,
                  PieceSet.PINK_YELLOW_DOTTED_CROSS, PieceSet.BLUE_PINK_SPADE),
            Piece(83, PieceSet.GREEN_ORANGE_SPADE, PieceSet.BLUE_PINK_SPADE,
                  PieceSet.PINK_YELLOW_DOTTED_CROSS, PieceSet.BLUE_PINK_SPADE)
        ]
        pieces_81_96 = []
        self.__piece_list = []
        self.__piece_list.extend(pieces_1_16)
        self.__piece_list.extend(pieces_17_32)
        self.__piece_list.extend(pieces_33_48)
        self.__piece_list.extend(pieces_49_64)
        self.__piece_list.extend(pieces_65_80)
