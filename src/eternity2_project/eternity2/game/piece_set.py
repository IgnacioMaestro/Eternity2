from typing import Optional

from .color import Color
from .constraints import Constraints
from .css_color_code import CSSColorCode
from .piece import Piece
from .rotated_piece import RotatedPiece
from .rotation import Rotation
from ..situation.placed_piece import PlacedPiece


class PieceSet:
    BORDER = Color(1, CSSColorCode('808080'), CSSColorCode('808080'), "Border")
    ORANGE_BLUE_CROSS = Color(2, CSSColorCode('FFA500'), CSSColorCode('0000FF'), "OrangeBlueCross")
    PINK_BLUE_CROSS = Color(3, CSSColorCode('FFC0CB'), CSSColorCode('0000FF'), "PinkBlueCross")
    GREEN_DARK_BLUE_HEXAGON = Color(4, CSSColorCode('00FF00'), CSSColorCode('00008B'), "GreenDarkBlueHexagon")
    DARK_BLUE_YELLOW_FLOWER = Color(5, CSSColorCode('00008B'), CSSColorCode('FFFF00'), "DarkBlueYellowFlower")
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
            Piece(1, PieceSet.ORANGE_BLUE_CROSS, PieceSet.PINK_BLUE_CROSS, PieceSet.BORDER, PieceSet.BORDER),
            Piece(2, PieceSet.ORANGE_BLUE_CROSS, PieceSet.GREEN_DARK_BLUE_HEXAGON, PieceSet.BORDER, PieceSet.BORDER),
            Piece(3, PieceSet.DARK_BLUE_YELLOW_FLOWER, PieceSet.PINK_BLUE_CROSS, PieceSet.BORDER, PieceSet.BORDER),
            Piece(4, PieceSet.PINK_BLUE_CROSS, PieceSet.DARK_BLUE_YELLOW_FLOWER, PieceSet.BORDER, PieceSet.BORDER),
            Piece(5, PieceSet.PINK_YELLOW_DOTTED_CROSS, PieceSet.ORANGE_BLUE_CROSS, PieceSet.BORDER,
                  PieceSet.ORANGE_BLUE_CROSS),
            Piece(6, PieceSet.PURPLE_BLUE_SPADE, PieceSet.DARK_BLUE_YELLOW_FLOWER, PieceSet.BORDER,
                  PieceSet.ORANGE_BLUE_CROSS),
            Piece(7, PieceSet.PURPLE_YELLOW_CROSS_IN_CIRCLE, PieceSet.ORANGE_BLUE_CROSS, PieceSet.BORDER,
                  PieceSet.ORANGE_BLUE_CROSS),
            Piece(8, PieceSet.PURPLE_YELLOW_CROSS_IN_CIRCLE, PieceSet.BROWN_ORANGE, PieceSet.BORDER,
                  PieceSet.ORANGE_BLUE_CROSS),
            Piece(9, PieceSet.GREEN_ORANGE_SPADE, PieceSet.PINK_BLUE_CROSS, PieceSet.BORDER,
                  PieceSet.ORANGE_BLUE_CROSS),
            Piece(10, PieceSet.BLUE_PINK_CASTLE, PieceSet.GREEN_DARK_BLUE_HEXAGON, PieceSet.BORDER,
                  PieceSet.ORANGE_BLUE_CROSS),
            Piece(11, PieceSet.YELLOW_GREEN_SQUARE, PieceSet.DARK_BLUE_YELLOW_FLOWER, PieceSet.BORDER,
                  PieceSet.ORANGE_BLUE_CROSS),
            Piece(12, PieceSet.DARK_BLUE_ORANGE_DOTTED_CROSS, PieceSet.GREEN_DARK_BLUE_HEXAGON, PieceSet.BORDER,
                  PieceSet.ORANGE_BLUE_CROSS),
            Piece(13, PieceSet.DARK_BLUE_ORANGE_DOTTED_CROSS, PieceSet.BROWN_ORANGE, PieceSet.BORDER,
                  PieceSet.ORANGE_BLUE_CROSS),
            Piece(14, PieceSet.PINK_YELLOW_CASTLE, PieceSet.GREEN_DARK_BLUE_HEXAGON, PieceSet.BORDER,
                  PieceSet.ORANGE_BLUE_CROSS),
            Piece(15, PieceSet.PURPLE_BLUE_SPADE, PieceSet.ORANGE_BLUE_CROSS, PieceSet.BORDER,
                  PieceSet.DARK_BLUE_YELLOW_FLOWER),
            Piece(16, PieceSet.YELLOW_BLUE_STAR, PieceSet.PINK_BLUE_CROSS, PieceSet.BORDER,
                  PieceSet.DARK_BLUE_YELLOW_FLOWER)
        ]
        pieces_17_32 = [
            Piece(17, PieceSet.GREEN_PINK_DOTTED_CROSS, PieceSet.BROWN_ORANGE, PieceSet.BORDER,
                  PieceSet.DARK_BLUE_YELLOW_FLOWER),
            Piece(18, PieceSet.MAROON_YELLOW_STAR, PieceSet.BROWN_ORANGE, PieceSet.BORDER,
                  PieceSet.DARK_BLUE_YELLOW_FLOWER),
            Piece(19, PieceSet.BLUE_PINK_CASTLE, PieceSet.DARK_BLUE_YELLOW_FLOWER, PieceSet.BORDER,
                  PieceSet.DARK_BLUE_YELLOW_FLOWER),
            Piece(20, PieceSet.YELLOW_GREEN_SQUARE, PieceSet.DARK_BLUE_YELLOW_FLOWER, PieceSet.BORDER,
                  PieceSet.DARK_BLUE_YELLOW_FLOWER),
            Piece(21, PieceSet.BLUE_PINK_SPADE, PieceSet.GREEN_DARK_BLUE_HEXAGON, PieceSet.BORDER,
                  PieceSet.DARK_BLUE_YELLOW_FLOWER),
            Piece(22, PieceSet.YELLOW_DARK_BLUE_CASTLE, PieceSet.ORANGE_BLUE_CROSS, PieceSet.BORDER,
                  PieceSet.DARK_BLUE_YELLOW_FLOWER),
            Piece(23, PieceSet.YELLOW_DARK_BLUE_CASTLE, PieceSet.BROWN_ORANGE, PieceSet.BORDER,
                  PieceSet.DARK_BLUE_YELLOW_FLOWER),
            Piece(24, PieceSet.ORANGE_PURPLE_STAR, PieceSet.ORANGE_BLUE_CROSS, PieceSet.BORDER,
                  PieceSet.DARK_BLUE_YELLOW_FLOWER),
            Piece(25, PieceSet.PINK_YELLOW_CASTLE, PieceSet.BROWN_ORANGE, PieceSet.BORDER,
                  PieceSet.DARK_BLUE_YELLOW_FLOWER),
            Piece(26,
                  PieceSet.PINK_YELLOW_DOTTED_CROSS, PieceSet.DARK_BLUE_YELLOW_FLOWER, PieceSet.BORDER,
                  PieceSet.PINK_BLUE_CROSS),
            Piece(27,
                  PieceSet.PINK_YELLOW_DOTTED_CROSS, PieceSet.PINK_BLUE_CROSS, PieceSet.BORDER,
                  PieceSet.PINK_BLUE_CROSS),
            Piece(28,
                  PieceSet.PURPLE_BLUE_SPADE, PieceSet.PINK_BLUE_CROSS, PieceSet.BORDER, PieceSet.PINK_BLUE_CROSS),
            Piece(29,
                  PieceSet.YELLOW_BLUE_STAR, PieceSet.PINK_BLUE_CROSS, PieceSet.BORDER, PieceSet.PINK_BLUE_CROSS),
            Piece(30,
                  PieceSet.BLUE_PINK_CASTLE, PieceSet.BROWN_ORANGE, PieceSet.BORDER, PieceSet.PINK_BLUE_CROSS),
            Piece(31,
                  PieceSet.YELLOW_GREEN_SQUARE, PieceSet.DARK_BLUE_YELLOW_FLOWER, PieceSet.BORDER,
                  PieceSet.PINK_BLUE_CROSS),
            Piece(32,
                  PieceSet.ORANGE_PURPLE_STAR, PieceSet.PINK_BLUE_CROSS, PieceSet.BORDER, PieceSet.PINK_BLUE_CROSS)
        ]
        pieces_33_48 = [
            Piece(33,
                  PieceSet.DARK_BLUE_ORANGE_DOTTED_CROSS, PieceSet.DARK_BLUE_YELLOW_FLOWER, PieceSet.BORDER,
                  PieceSet.PINK_BLUE_CROSS),
            Piece(34,
                  PieceSet.DARK_BLUE_ORANGE_DOTTED_CROSS, PieceSet.GREEN_DARK_BLUE_HEXAGON, PieceSet.BORDER,
                  PieceSet.PINK_BLUE_CROSS),
            Piece(35, PieceSet.DARK_BLUE_BLUE_SQUARE, PieceSet.BROWN_ORANGE, PieceSet.BORDER, PieceSet.PINK_BLUE_CROSS),
            Piece(36, PieceSet.DARK_BLUE_PINK_CROSS_IN_CIRCLE, PieceSet.GREEN_DARK_BLUE_HEXAGON, PieceSet.BORDER,
                  PieceSet.PINK_BLUE_CROSS),
            Piece(37, PieceSet.YELLOW_BLUE_STAR, PieceSet.ORANGE_BLUE_CROSS, PieceSet.BORDER,
                  PieceSet.GREEN_DARK_BLUE_HEXAGON),
            Piece(38, PieceSet.MAROON_GREEN_CROSS_IN_CIRCLE, PieceSet.BROWN_ORANGE, PieceSet.BORDER,
                  PieceSet.GREEN_DARK_BLUE_HEXAGON),
            Piece(39, PieceSet.GREEN_ORANGE_SPADE, PieceSet.BROWN_ORANGE, PieceSet.BORDER,
                  PieceSet.GREEN_DARK_BLUE_HEXAGON),
            Piece(40, PieceSet.MAROON_YELLOW_STAR, PieceSet.DARK_BLUE_YELLOW_FLOWER, PieceSet.BORDER,
                  PieceSet.GREEN_DARK_BLUE_HEXAGON),
            Piece(41, PieceSet.MAROON_YELLOW_STAR, PieceSet.PINK_BLUE_CROSS, PieceSet.BORDER,
                  PieceSet.GREEN_DARK_BLUE_HEXAGON),
            Piece(42, PieceSet.YELLOW_GREEN_SQUARE, PieceSet.ORANGE_BLUE_CROSS, PieceSet.BORDER,
                  PieceSet.GREEN_DARK_BLUE_HEXAGON),
            Piece(43, PieceSet.YELLOW_GREEN_SQUARE, PieceSet.DARK_BLUE_YELLOW_FLOWER, PieceSet.BORDER,
                  PieceSet.GREEN_DARK_BLUE_HEXAGON),
            Piece(44, PieceSet.YELLOW_GREEN_SQUARE, PieceSet.PINK_BLUE_CROSS, PieceSet.BORDER,
                  PieceSet.GREEN_DARK_BLUE_HEXAGON),
            Piece(45, PieceSet.BLUE_PINK_SPADE, PieceSet.ORANGE_BLUE_CROSS, PieceSet.BORDER,
                  PieceSet.GREEN_DARK_BLUE_HEXAGON),
            Piece(46, PieceSet.ORANGE_PURPLE_STAR, PieceSet.GREEN_DARK_BLUE_HEXAGON, PieceSet.BORDER,
                  PieceSet.GREEN_DARK_BLUE_HEXAGON),
            Piece(47, PieceSet.DARK_BLUE_ORANGE_DOTTED_CROSS, PieceSet.GREEN_DARK_BLUE_HEXAGON, PieceSet.BORDER,
                  PieceSet.GREEN_DARK_BLUE_HEXAGON),
            Piece(48, PieceSet.DARK_BLUE_BLUE_SQUARE, PieceSet.GREEN_DARK_BLUE_HEXAGON, PieceSet.BORDER,
                  PieceSet.GREEN_DARK_BLUE_HEXAGON)
        ]
        pieces_49_64 = [
            Piece(49, PieceSet.PINK_YELLOW_DOTTED_CROSS, PieceSet.BROWN_ORANGE, PieceSet.BORDER, PieceSet.BROWN_ORANGE),
            Piece(50, PieceSet.PURPLE_BLUE_SPADE, PieceSet.ORANGE_BLUE_CROSS, PieceSet.BORDER, PieceSet.BROWN_ORANGE),
            Piece(51, PieceSet.PURPLE_BLUE_SPADE, PieceSet.DARK_BLUE_YELLOW_FLOWER, PieceSet.BORDER,
                  PieceSet.BROWN_ORANGE),
            Piece(52, PieceSet.PURPLE_YELLOW_CROSS_IN_CIRCLE, PieceSet.ORANGE_BLUE_CROSS, PieceSet.BORDER,
                  PieceSet.BROWN_ORANGE),
            Piece(53, PieceSet.BLUE_PINK_CASTLE, PieceSet.GREEN_DARK_BLUE_HEXAGON, PieceSet.BORDER,
                  PieceSet.BROWN_ORANGE),
            Piece(54, PieceSet.BLUE_PINK_SPADE, PieceSet.ORANGE_BLUE_CROSS, PieceSet.BORDER, PieceSet.BROWN_ORANGE),
            Piece(55, PieceSet.BLUE_PINK_SPADE, PieceSet.BROWN_ORANGE, PieceSet.BORDER, PieceSet.BROWN_ORANGE),
            Piece(56, PieceSet.DARK_BLUE_ORANGE_DOTTED_CROSS, PieceSet.PINK_BLUE_CROSS, PieceSet.BORDER,
                  PieceSet.BROWN_ORANGE),
            Piece(57, PieceSet.DARK_BLUE_BLUE_SQUARE, PieceSet.ORANGE_BLUE_CROSS, PieceSet.BORDER,
                  PieceSet.BROWN_ORANGE),
            Piece(58, PieceSet.DARK_BLUE_BLUE_SQUARE, PieceSet.BROWN_ORANGE, PieceSet.BORDER, PieceSet.BROWN_ORANGE),
            Piece(59, PieceSet.PINK_YELLOW_CASTLE, PieceSet.DARK_BLUE_YELLOW_FLOWER, PieceSet.BORDER,
                  PieceSet.BROWN_ORANGE),
            Piece(60, PieceSet.DARK_BLUE_PINK_CROSS_IN_CIRCLE, PieceSet.ORANGE_BLUE_CROSS, PieceSet.BORDER,
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
        ]
        pieces_81_96 = [
            Piece(81, PieceSet.MAROON_YELLOW_STAR, PieceSet.YELLOW_BLUE_STAR,
                  PieceSet.PINK_YELLOW_DOTTED_CROSS, PieceSet.YELLOW_GREEN_SQUARE),
            Piece(82, PieceSet.YELLOW_BLUE_STAR, PieceSet.YELLOW_BLUE_STAR,
                  PieceSet.PINK_YELLOW_DOTTED_CROSS, PieceSet.BLUE_PINK_SPADE),
            Piece(83, PieceSet.GREEN_ORANGE_SPADE, PieceSet.BLUE_PINK_SPADE,
                  PieceSet.PINK_YELLOW_DOTTED_CROSS, PieceSet.BLUE_PINK_SPADE),
            Piece(84, PieceSet.YELLOW_BLUE_STAR, PieceSet.MAROON_YELLOW_STAR,
                  PieceSet.PINK_YELLOW_DOTTED_CROSS, PieceSet.YELLOW_DARK_BLUE_CASTLE),
            Piece(85, PieceSet.PURPLE_YELLOW_CROSS_IN_CIRCLE, PieceSet.GREEN_PINK_DOTTED_CROSS,
                  PieceSet.PINK_YELLOW_DOTTED_CROSS, PieceSet.YELLOW_DARK_BLUE_CASTLE),
            Piece(86, PieceSet.DARK_BLUE_ORANGE_DOTTED_CROSS, PieceSet.YELLOW_DARK_BLUE_CASTLE,
                  PieceSet.PINK_YELLOW_DOTTED_CROSS, PieceSet.YELLOW_DARK_BLUE_CASTLE),
            Piece(87, PieceSet.DARK_BLUE_BLUE_SQUARE, PieceSet.ORANGE_PURPLE_STAR,
                  PieceSet.PINK_YELLOW_DOTTED_CROSS, PieceSet.YELLOW_DARK_BLUE_CASTLE),
            Piece(88, PieceSet.PINK_YELLOW_DOTTED_CROSS, PieceSet.PINK_YELLOW_CASTLE,
                  PieceSet.PINK_YELLOW_DOTTED_CROSS, PieceSet.ORANGE_PURPLE_STAR),
            Piece(89, PieceSet.PURPLE_YELLOW_CROSS_IN_CIRCLE, PieceSet.DARK_BLUE_PINK_CROSS_IN_CIRCLE,
                  PieceSet.PINK_YELLOW_DOTTED_CROSS, PieceSet.ORANGE_PURPLE_STAR),
            Piece(90, PieceSet.BLUE_PINK_SPADE, PieceSet.DARK_BLUE_BLUE_SQUARE,
                  PieceSet.PINK_YELLOW_DOTTED_CROSS, PieceSet.ORANGE_PURPLE_STAR),
            Piece(91, PieceSet.GREEN_ORANGE_SPADE, PieceSet.YELLOW_DARK_BLUE_CASTLE,
                  PieceSet.PINK_YELLOW_DOTTED_CROSS, PieceSet.DARK_BLUE_ORANGE_DOTTED_CROSS),
            Piece(92, PieceSet.MAROON_YELLOW_STAR, PieceSet.YELLOW_GREEN_SQUARE,
                  PieceSet.PINK_YELLOW_DOTTED_CROSS, PieceSet.DARK_BLUE_ORANGE_DOTTED_CROSS),
            Piece(93, PieceSet.MAROON_YELLOW_STAR, PieceSet.BLUE_PINK_SPADE,
                  PieceSet.PINK_YELLOW_DOTTED_CROSS, PieceSet.DARK_BLUE_ORANGE_DOTTED_CROSS),
            Piece(94, PieceSet.BLUE_PINK_SPADE, PieceSet.PINK_YELLOW_CASTLE,
                  PieceSet.PINK_YELLOW_DOTTED_CROSS, PieceSet.DARK_BLUE_ORANGE_DOTTED_CROSS),
            Piece(95, PieceSet.YELLOW_DARK_BLUE_CASTLE, PieceSet.GREEN_PINK_DOTTED_CROSS,
                  PieceSet.PINK_YELLOW_DOTTED_CROSS, PieceSet.DARK_BLUE_ORANGE_DOTTED_CROSS),
            Piece(96, PieceSet.PINK_YELLOW_CASTLE, PieceSet.MAROON_GREEN_CROSS_IN_CIRCLE,
                  PieceSet.PINK_YELLOW_DOTTED_CROSS, PieceSet.PINK_YELLOW_CASTLE)
        ]
        pieces_97_112 = [
            Piece(97, PieceSet.BLUE_PINK_SPADE, PieceSet.MAROON_YELLOW_STAR,
                  PieceSet.PINK_YELLOW_DOTTED_CROSS, PieceSet.DARK_BLUE_PINK_CROSS_IN_CIRCLE),
            Piece(98, PieceSet.ORANGE_PURPLE_STAR, PieceSet.DARK_BLUE_ORANGE_DOTTED_CROSS,
                  PieceSet.PINK_YELLOW_DOTTED_CROSS, PieceSet.DARK_BLUE_PINK_CROSS_IN_CIRCLE),
            Piece(99, PieceSet.PINK_YELLOW_CASTLE, PieceSet.PURPLE_YELLOW_CROSS_IN_CIRCLE,
                  PieceSet.PINK_YELLOW_DOTTED_CROSS, PieceSet.DARK_BLUE_PINK_CROSS_IN_CIRCLE),
            Piece(100, PieceSet.DARK_BLUE_PINK_CROSS_IN_CIRCLE, PieceSet.PINK_YELLOW_CASTLE,
                  PieceSet.PINK_YELLOW_DOTTED_CROSS, PieceSet.DARK_BLUE_PINK_CROSS_IN_CIRCLE),
            Piece(101, PieceSet.YELLOW_DARK_BLUE_CASTLE, PieceSet.YELLOW_GREEN_SQUARE,
                  PieceSet.PURPLE_BLUE_SPADE, PieceSet.PURPLE_BLUE_SPADE),
            Piece(102, PieceSet.YELLOW_DARK_BLUE_CASTLE, PieceSet.DARK_BLUE_BLUE_SQUARE,
                  PieceSet.PURPLE_BLUE_SPADE, PieceSet.PURPLE_BLUE_SPADE),
            Piece(103, PieceSet.DARK_BLUE_BLUE_SQUARE, PieceSet.MAROON_YELLOW_STAR,
                  PieceSet.PURPLE_BLUE_SPADE, PieceSet.PURPLE_BLUE_SPADE),
            Piece(104, PieceSet.DARK_BLUE_PINK_CROSS_IN_CIRCLE, PieceSet.PURPLE_YELLOW_CROSS_IN_CIRCLE,
                  PieceSet.PURPLE_BLUE_SPADE, PieceSet.PURPLE_BLUE_SPADE),
            Piece(105, PieceSet.BLUE_PINK_SPADE, PieceSet.YELLOW_GREEN_SQUARE,
                  PieceSet.PURPLE_BLUE_SPADE, PieceSet.YELLOW_BLUE_STAR),
            Piece(106, PieceSet.MAROON_GREEN_CROSS_IN_CIRCLE, PieceSet.DARK_BLUE_ORANGE_DOTTED_CROSS,
                  PieceSet.PURPLE_BLUE_SPADE, PieceSet.PURPLE_YELLOW_CROSS_IN_CIRCLE),
            Piece(107, PieceSet.MAROON_YELLOW_STAR, PieceSet.DARK_BLUE_ORANGE_DOTTED_CROSS,
                  PieceSet.PURPLE_BLUE_SPADE, PieceSet.PURPLE_YELLOW_CROSS_IN_CIRCLE),
            Piece(108, PieceSet.BLUE_PINK_SPADE, PieceSet.YELLOW_GREEN_SQUARE,
                  PieceSet.PURPLE_BLUE_SPADE, PieceSet.PURPLE_YELLOW_CROSS_IN_CIRCLE),
            Piece(109, PieceSet.DARK_BLUE_BLUE_SQUARE, PieceSet.GREEN_ORANGE_SPADE,
                  PieceSet.PURPLE_BLUE_SPADE, PieceSet.PURPLE_YELLOW_CROSS_IN_CIRCLE),
            Piece(110, PieceSet.YELLOW_GREEN_SQUARE, PieceSet.YELLOW_DARK_BLUE_CASTLE,
                  PieceSet.PURPLE_BLUE_SPADE, PieceSet.GREEN_PINK_DOTTED_CROSS),
            Piece(111, PieceSet.YELLOW_DARK_BLUE_CASTLE, PieceSet.YELLOW_GREEN_SQUARE,
                  PieceSet.PURPLE_BLUE_SPADE, PieceSet.GREEN_PINK_DOTTED_CROSS),
            Piece(112, PieceSet.ORANGE_PURPLE_STAR, PieceSet.MAROON_YELLOW_STAR,
                  PieceSet.PURPLE_BLUE_SPADE, PieceSet.MAROON_GREEN_CROSS_IN_CIRCLE)
        ]
        pieces_113_128 = [
            Piece(113, PieceSet.ORANGE_PURPLE_STAR, PieceSet.DARK_BLUE_BLUE_SQUARE,
                  PieceSet.PURPLE_BLUE_SPADE, PieceSet.MAROON_GREEN_CROSS_IN_CIRCLE),
            Piece(114, PieceSet.GREEN_PINK_DOTTED_CROSS, PieceSet.BLUE_PINK_SPADE,
                  PieceSet.PURPLE_BLUE_SPADE, PieceSet.GREEN_ORANGE_SPADE),
            Piece(115, PieceSet.BLUE_PINK_CASTLE, PieceSet.YELLOW_DARK_BLUE_CASTLE,
                  PieceSet.PURPLE_BLUE_SPADE, PieceSet.GREEN_ORANGE_SPADE),
            Piece(116, PieceSet.YELLOW_DARK_BLUE_CASTLE, PieceSet.GREEN_ORANGE_SPADE,
                  PieceSet.PURPLE_BLUE_SPADE, PieceSet.GREEN_ORANGE_SPADE),
            Piece(117, PieceSet.DARK_BLUE_PINK_CROSS_IN_CIRCLE, PieceSet.DARK_BLUE_BLUE_SQUARE,
                  PieceSet.PURPLE_BLUE_SPADE, PieceSet.GREEN_ORANGE_SPADE),
            Piece(118, PieceSet.MAROON_GREEN_CROSS_IN_CIRCLE, PieceSet.PINK_YELLOW_CASTLE,
                  PieceSet.PURPLE_BLUE_SPADE, PieceSet.MAROON_YELLOW_STAR),
            Piece(119, PieceSet.DARK_BLUE_BLUE_SQUARE, PieceSet.YELLOW_DARK_BLUE_CASTLE,
                  PieceSet.PURPLE_BLUE_SPADE, PieceSet.BLUE_PINK_CASTLE),
            Piece(120, PieceSet.DARK_BLUE_ORANGE_DOTTED_CROSS, PieceSet.DARK_BLUE_PINK_CROSS_IN_CIRCLE,
                  PieceSet.PURPLE_BLUE_SPADE, PieceSet.YELLOW_GREEN_SQUARE),
            Piece(121, PieceSet.GREEN_PINK_DOTTED_CROSS, PieceSet.DARK_BLUE_PINK_CROSS_IN_CIRCLE,
                  PieceSet.PURPLE_BLUE_SPADE, PieceSet.BLUE_PINK_SPADE),
            Piece(122, PieceSet.PURPLE_YELLOW_CROSS_IN_CIRCLE, PieceSet.DARK_BLUE_BLUE_SQUARE,
                  PieceSet.PURPLE_BLUE_SPADE, PieceSet.ORANGE_PURPLE_STAR),
            Piece(123, PieceSet.GREEN_PINK_DOTTED_CROSS, PieceSet.MAROON_YELLOW_STAR,
                  PieceSet.PURPLE_BLUE_SPADE, PieceSet.ORANGE_PURPLE_STAR),
            Piece(124, PieceSet.ORANGE_PURPLE_STAR, PieceSet.YELLOW_GREEN_SQUARE,
                  PieceSet.PURPLE_BLUE_SPADE, PieceSet.ORANGE_PURPLE_STAR),
            Piece(125, PieceSet.YELLOW_DARK_BLUE_CASTLE, PieceSet.DARK_BLUE_PINK_CROSS_IN_CIRCLE,
                  PieceSet.PURPLE_BLUE_SPADE, PieceSet.DARK_BLUE_ORANGE_DOTTED_CROSS),
            Piece(126, PieceSet.PINK_YELLOW_CASTLE, PieceSet.YELLOW_GREEN_SQUARE,
                  PieceSet.PURPLE_BLUE_SPADE, PieceSet.DARK_BLUE_ORANGE_DOTTED_CROSS),
            Piece(127, PieceSet.GREEN_PINK_DOTTED_CROSS, PieceSet.PURPLE_YELLOW_CROSS_IN_CIRCLE,
                  PieceSet.PURPLE_BLUE_SPADE, PieceSet.DARK_BLUE_BLUE_SQUARE),
            Piece(128, PieceSet.MAROON_YELLOW_STAR, PieceSet.PINK_YELLOW_CASTLE,
                  PieceSet.PURPLE_BLUE_SPADE, PieceSet.DARK_BLUE_BLUE_SQUARE)
        ]
        pieces_129_144 = [
            Piece(129, PieceSet.BLUE_PINK_SPADE, PieceSet.MAROON_GREEN_CROSS_IN_CIRCLE,
                  PieceSet.PURPLE_BLUE_SPADE, PieceSet.DARK_BLUE_BLUE_SQUARE),
            Piece(130, PieceSet.ORANGE_PURPLE_STAR, PieceSet.DARK_BLUE_ORANGE_DOTTED_CROSS,
                  PieceSet.PURPLE_BLUE_SPADE, PieceSet.DARK_BLUE_BLUE_SQUARE),
            Piece(131, PieceSet.PURPLE_YELLOW_CROSS_IN_CIRCLE, PieceSet.ORANGE_PURPLE_STAR,
                  PieceSet.PURPLE_BLUE_SPADE, PieceSet.PINK_YELLOW_CASTLE),
            Piece(132, PieceSet.YELLOW_DARK_BLUE_CASTLE, PieceSet.GREEN_PINK_DOTTED_CROSS,
                  PieceSet.PURPLE_BLUE_SPADE, PieceSet.PINK_YELLOW_CASTLE),
            Piece(133, PieceSet.GREEN_PINK_DOTTED_CROSS, PieceSet.DARK_BLUE_BLUE_SQUARE,
                  PieceSet.PURPLE_BLUE_SPADE, PieceSet.DARK_BLUE_PINK_CROSS_IN_CIRCLE),
            Piece(134, PieceSet.GREEN_ORANGE_SPADE, PieceSet.BLUE_PINK_SPADE,
                  PieceSet.PURPLE_BLUE_SPADE, PieceSet.DARK_BLUE_PINK_CROSS_IN_CIRCLE),
            Piece(135, PieceSet.BLUE_PINK_SPADE, PieceSet.MAROON_GREEN_CROSS_IN_CIRCLE,
                  PieceSet.PURPLE_BLUE_SPADE, PieceSet.DARK_BLUE_PINK_CROSS_IN_CIRCLE),
            Piece(136, PieceSet.DARK_BLUE_BLUE_SQUARE, PieceSet.ORANGE_PURPLE_STAR,
                  PieceSet.PURPLE_BLUE_SPADE, PieceSet.DARK_BLUE_PINK_CROSS_IN_CIRCLE),
            Piece(137, PieceSet.ORANGE_PURPLE_STAR, PieceSet.BLUE_PINK_CASTLE,
                  PieceSet.YELLOW_BLUE_STAR, PieceSet.YELLOW_BLUE_STAR),
            Piece(138, PieceSet.PURPLE_YELLOW_CROSS_IN_CIRCLE, PieceSet.MAROON_GREEN_CROSS_IN_CIRCLE,
                  PieceSet.YELLOW_BLUE_STAR, PieceSet.PURPLE_YELLOW_CROSS_IN_CIRCLE),
            Piece(139, PieceSet.PURPLE_YELLOW_CROSS_IN_CIRCLE, PieceSet.GREEN_ORANGE_SPADE,
                  PieceSet.YELLOW_BLUE_STAR, PieceSet.PURPLE_YELLOW_CROSS_IN_CIRCLE),
            Piece(140, PieceSet.PURPLE_YELLOW_CROSS_IN_CIRCLE, PieceSet.YELLOW_DARK_BLUE_CASTLE,
                  PieceSet.YELLOW_BLUE_STAR, PieceSet.PURPLE_YELLOW_CROSS_IN_CIRCLE),
            Piece(141, PieceSet.MAROON_YELLOW_STAR, PieceSet.PINK_YELLOW_CASTLE,
                  PieceSet.YELLOW_BLUE_STAR, PieceSet.PURPLE_YELLOW_CROSS_IN_CIRCLE),
            Piece(142, PieceSet.YELLOW_GREEN_SQUARE, PieceSet.PURPLE_YELLOW_CROSS_IN_CIRCLE,
                  PieceSet.YELLOW_BLUE_STAR, PieceSet.PURPLE_YELLOW_CROSS_IN_CIRCLE),
            Piece(143, PieceSet.DARK_BLUE_BLUE_SQUARE, PieceSet.YELLOW_DARK_BLUE_CASTLE,
                  PieceSet.YELLOW_BLUE_STAR, PieceSet.PURPLE_YELLOW_CROSS_IN_CIRCLE),
            Piece(144, PieceSet.PINK_YELLOW_CASTLE, PieceSet.PINK_YELLOW_CASTLE,
                  PieceSet.YELLOW_BLUE_STAR, PieceSet.PURPLE_YELLOW_CROSS_IN_CIRCLE)
        ]
        pieces_145_160 = [
            Piece(145, PieceSet.MAROON_GREEN_CROSS_IN_CIRCLE, PieceSet.BLUE_PINK_SPADE,
                  PieceSet.YELLOW_BLUE_STAR, PieceSet.GREEN_PINK_DOTTED_CROSS),
            Piece(146, PieceSet.YELLOW_BLUE_STAR, PieceSet.YELLOW_DARK_BLUE_CASTLE,
                  PieceSet.YELLOW_BLUE_STAR, PieceSet.MAROON_GREEN_CROSS_IN_CIRCLE),
            Piece(147, PieceSet.YELLOW_BLUE_STAR, PieceSet.DARK_BLUE_PINK_CROSS_IN_CIRCLE,
                  PieceSet.YELLOW_BLUE_STAR, PieceSet.MAROON_GREEN_CROSS_IN_CIRCLE),
            Piece(148, PieceSet.MAROON_GREEN_CROSS_IN_CIRCLE, PieceSet.GREEN_PINK_DOTTED_CROSS,
                  PieceSet.YELLOW_BLUE_STAR, PieceSet.MAROON_GREEN_CROSS_IN_CIRCLE),
            Piece(149, PieceSet.YELLOW_GREEN_SQUARE, PieceSet.YELLOW_DARK_BLUE_CASTLE,
                  PieceSet.YELLOW_BLUE_STAR, PieceSet.MAROON_GREEN_CROSS_IN_CIRCLE),
            Piece(150, PieceSet.PURPLE_YELLOW_CROSS_IN_CIRCLE, PieceSet.GREEN_ORANGE_SPADE,
                  PieceSet.YELLOW_BLUE_STAR, PieceSet.MAROON_YELLOW_STAR),
            Piece(151, PieceSet.BLUE_PINK_SPADE, PieceSet.DARK_BLUE_PINK_CROSS_IN_CIRCLE,
                  PieceSet.YELLOW_BLUE_STAR, PieceSet.MAROON_YELLOW_STAR),
            Piece(152, PieceSet.GREEN_ORANGE_SPADE, PieceSet.GREEN_ORANGE_SPADE,
                  PieceSet.YELLOW_BLUE_STAR, PieceSet.BLUE_PINK_CASTLE),
            Piece(153, PieceSet.GREEN_ORANGE_SPADE, PieceSet.MAROON_YELLOW_STAR,
                  PieceSet.YELLOW_BLUE_STAR, PieceSet.BLUE_PINK_CASTLE),
            Piece(154, PieceSet.DARK_BLUE_PINK_CROSS_IN_CIRCLE, PieceSet.DARK_BLUE_BLUE_SQUARE,
                  PieceSet.YELLOW_BLUE_STAR, PieceSet.BLUE_PINK_CASTLE),
            Piece(155, PieceSet.BLUE_PINK_CASTLE, PieceSet.BLUE_PINK_CASTLE,
                  PieceSet.YELLOW_BLUE_STAR, PieceSet.BLUE_PINK_SPADE),
            Piece(156, PieceSet.BLUE_PINK_CASTLE, PieceSet.YELLOW_DARK_BLUE_CASTLE,
                  PieceSet.YELLOW_BLUE_STAR, PieceSet.BLUE_PINK_SPADE),
            Piece(157, PieceSet.DARK_BLUE_PINK_CROSS_IN_CIRCLE, PieceSet.BLUE_PINK_CASTLE,
                  PieceSet.YELLOW_BLUE_STAR, PieceSet.BLUE_PINK_SPADE),
            Piece(158, PieceSet.BLUE_PINK_CASTLE, PieceSet.DARK_BLUE_BLUE_SQUARE,
                  PieceSet.YELLOW_BLUE_STAR, PieceSet.ORANGE_PURPLE_STAR),
            Piece(159, PieceSet.DARK_BLUE_ORANGE_DOTTED_CROSS, PieceSet.PURPLE_YELLOW_CROSS_IN_CIRCLE,
                  PieceSet.YELLOW_BLUE_STAR, PieceSet.ORANGE_PURPLE_STAR),
            Piece(160, PieceSet.PINK_YELLOW_CASTLE, PieceSet.PINK_YELLOW_CASTLE,
                  PieceSet.YELLOW_BLUE_STAR, PieceSet.DARK_BLUE_ORANGE_DOTTED_CROSS)
        ]
        pieces_161_176 = [
            Piece(161, PieceSet.PURPLE_YELLOW_CROSS_IN_CIRCLE, PieceSet.ORANGE_PURPLE_STAR,
                  PieceSet.YELLOW_BLUE_STAR, PieceSet.DARK_BLUE_BLUE_SQUARE),
            Piece(162, PieceSet.GREEN_PINK_DOTTED_CROSS, PieceSet.ORANGE_PURPLE_STAR,
                  PieceSet.YELLOW_BLUE_STAR, PieceSet.DARK_BLUE_BLUE_SQUARE),
            Piece(163, PieceSet.YELLOW_GREEN_SQUARE, PieceSet.GREEN_ORANGE_SPADE,
                  PieceSet.YELLOW_BLUE_STAR, PieceSet.DARK_BLUE_PINK_CROSS_IN_CIRCLE),
            Piece(164, PieceSet.BLUE_PINK_SPADE, PieceSet.DARK_BLUE_BLUE_SQUARE,
                  PieceSet.YELLOW_BLUE_STAR, PieceSet.DARK_BLUE_PINK_CROSS_IN_CIRCLE),
            Piece(165, PieceSet.MAROON_GREEN_CROSS_IN_CIRCLE, PieceSet.BLUE_PINK_SPADE,
                  PieceSet.PURPLE_YELLOW_CROSS_IN_CIRCLE, PieceSet.GREEN_PINK_DOTTED_CROSS),
            Piece(166, PieceSet.BLUE_PINK_SPADE, PieceSet.DARK_BLUE_ORANGE_DOTTED_CROSS,
                  PieceSet.PURPLE_YELLOW_CROSS_IN_CIRCLE, PieceSet.GREEN_PINK_DOTTED_CROSS),
            Piece(167, PieceSet.MAROON_GREEN_CROSS_IN_CIRCLE, PieceSet.MAROON_GREEN_CROSS_IN_CIRCLE,
                  PieceSet.PURPLE_YELLOW_CROSS_IN_CIRCLE, PieceSet.GREEN_ORANGE_SPADE),
            Piece(168, PieceSet.GREEN_ORANGE_SPADE, PieceSet.YELLOW_GREEN_SQUARE,
                  PieceSet.PURPLE_YELLOW_CROSS_IN_CIRCLE, PieceSet.MAROON_YELLOW_STAR),
            Piece(169, PieceSet.MAROON_YELLOW_STAR, PieceSet.PINK_YELLOW_CASTLE,
                  PieceSet.PURPLE_YELLOW_CROSS_IN_CIRCLE, PieceSet.MAROON_YELLOW_STAR),
            Piece(170, PieceSet.BLUE_PINK_SPADE, PieceSet.DARK_BLUE_ORANGE_DOTTED_CROSS,
                  PieceSet.PURPLE_YELLOW_CROSS_IN_CIRCLE, PieceSet.BLUE_PINK_CASTLE),
            Piece(171, PieceSet.ORANGE_PURPLE_STAR, PieceSet.DARK_BLUE_BLUE_SQUARE,
                  PieceSet.PURPLE_YELLOW_CROSS_IN_CIRCLE, PieceSet.BLUE_PINK_CASTLE),
            Piece(172, PieceSet.PINK_YELLOW_CASTLE, PieceSet.GREEN_ORANGE_SPADE,
                  PieceSet.PURPLE_YELLOW_CROSS_IN_CIRCLE, PieceSet.BLUE_PINK_CASTLE),
            Piece(173, PieceSet.YELLOW_GREEN_SQUARE, PieceSet.YELLOW_GREEN_SQUARE,
                  PieceSet.PURPLE_YELLOW_CROSS_IN_CIRCLE, PieceSet.YELLOW_GREEN_SQUARE),
            Piece(174, PieceSet.YELLOW_DARK_BLUE_CASTLE, PieceSet.ORANGE_PURPLE_STAR,
                  PieceSet.PURPLE_YELLOW_CROSS_IN_CIRCLE, PieceSet.YELLOW_GREEN_SQUARE),
            Piece(175, PieceSet.BLUE_PINK_CASTLE, PieceSet.PINK_YELLOW_CASTLE,
                  PieceSet.PURPLE_YELLOW_CROSS_IN_CIRCLE, PieceSet.BLUE_PINK_SPADE),
            Piece(176, PieceSet.BLUE_PINK_CASTLE, PieceSet.MAROON_YELLOW_STAR,
                  PieceSet.PURPLE_YELLOW_CROSS_IN_CIRCLE, PieceSet.YELLOW_DARK_BLUE_CASTLE)
        ]
        pieces_177_192 = [
            Piece(177, PieceSet.GREEN_PINK_DOTTED_CROSS, PieceSet.BLUE_PINK_SPADE,
                  PieceSet.PURPLE_YELLOW_CROSS_IN_CIRCLE, PieceSet.ORANGE_PURPLE_STAR),
            Piece(178, PieceSet.YELLOW_DARK_BLUE_CASTLE, PieceSet.DARK_BLUE_BLUE_SQUARE,
                  PieceSet.PURPLE_YELLOW_CROSS_IN_CIRCLE, PieceSet.DARK_BLUE_ORANGE_DOTTED_CROSS),
            Piece(179, PieceSet.DARK_BLUE_ORANGE_DOTTED_CROSS, PieceSet.YELLOW_GREEN_SQUARE,
                  PieceSet.PURPLE_YELLOW_CROSS_IN_CIRCLE, PieceSet.DARK_BLUE_ORANGE_DOTTED_CROSS),
            Piece(180, PieceSet.BLUE_PINK_CASTLE, PieceSet.DARK_BLUE_BLUE_SQUARE,
                  PieceSet.PURPLE_YELLOW_CROSS_IN_CIRCLE, PieceSet.DARK_BLUE_BLUE_SQUARE),
            Piece(181, PieceSet.GREEN_ORANGE_SPADE, PieceSet.DARK_BLUE_BLUE_SQUARE,
                  PieceSet.PURPLE_YELLOW_CROSS_IN_CIRCLE, PieceSet.PINK_YELLOW_CASTLE),
            Piece(182, PieceSet.BLUE_PINK_CASTLE, PieceSet.GREEN_ORANGE_SPADE,
                  PieceSet.PURPLE_YELLOW_CROSS_IN_CIRCLE, PieceSet.PINK_YELLOW_CASTLE),
            Piece(183, PieceSet.MAROON_YELLOW_STAR, PieceSet.DARK_BLUE_ORANGE_DOTTED_CROSS,
                  PieceSet.GREEN_PINK_DOTTED_CROSS, PieceSet.GREEN_PINK_DOTTED_CROSS),
            Piece(184, PieceSet.DARK_BLUE_PINK_CROSS_IN_CIRCLE, PieceSet.BLUE_PINK_CASTLE,
                  PieceSet.GREEN_PINK_DOTTED_CROSS, PieceSet.MAROON_GREEN_CROSS_IN_CIRCLE),
            Piece(185, PieceSet.MAROON_YELLOW_STAR, PieceSet.YELLOW_DARK_BLUE_CASTLE,
                  PieceSet.GREEN_PINK_DOTTED_CROSS, PieceSet.GREEN_ORANGE_SPADE),
            Piece(186, PieceSet.DARK_BLUE_ORANGE_DOTTED_CROSS, PieceSet.DARK_BLUE_ORANGE_DOTTED_CROSS,
                  PieceSet.GREEN_PINK_DOTTED_CROSS, PieceSet.GREEN_ORANGE_SPADE),
            Piece(187, PieceSet.PINK_YELLOW_CASTLE, PieceSet.BLUE_PINK_CASTLE,
                  PieceSet.GREEN_PINK_DOTTED_CROSS, PieceSet.MAROON_YELLOW_STAR),
            Piece(188, PieceSet.GREEN_PINK_DOTTED_CROSS, PieceSet.PINK_YELLOW_CASTLE,
                  PieceSet.GREEN_PINK_DOTTED_CROSS, PieceSet.BLUE_PINK_CASTLE),
            Piece(189, PieceSet.MAROON_GREEN_CROSS_IN_CIRCLE, PieceSet.MAROON_YELLOW_STAR,
                  PieceSet.GREEN_PINK_DOTTED_CROSS, PieceSet.BLUE_PINK_CASTLE),
            Piece(190, PieceSet.DARK_BLUE_BLUE_SQUARE, PieceSet.MAROON_YELLOW_STAR,
                  PieceSet.GREEN_PINK_DOTTED_CROSS, PieceSet.BLUE_PINK_CASTLE),
            Piece(191, PieceSet.MAROON_GREEN_CROSS_IN_CIRCLE, PieceSet.MAROON_GREEN_CROSS_IN_CIRCLE,
                  PieceSet.GREEN_PINK_DOTTED_CROSS, PieceSet.YELLOW_GREEN_SQUARE),
            Piece(192, PieceSet.YELLOW_GREEN_SQUARE, PieceSet.ORANGE_PURPLE_STAR,
                  PieceSet.GREEN_PINK_DOTTED_CROSS, PieceSet.YELLOW_GREEN_SQUARE)
        ]
        pieces_193_208 = [
            Piece(193, PieceSet.GREEN_ORANGE_SPADE, PieceSet.BLUE_PINK_CASTLE,
                  PieceSet.GREEN_PINK_DOTTED_CROSS, PieceSet.BLUE_PINK_SPADE),
            Piece(194, PieceSet.PINK_YELLOW_CASTLE, PieceSet.GREEN_ORANGE_SPADE,
                  PieceSet.GREEN_PINK_DOTTED_CROSS, PieceSet.YELLOW_DARK_BLUE_CASTLE),
            Piece(195, PieceSet.PINK_YELLOW_CASTLE, PieceSet.DARK_BLUE_PINK_CROSS_IN_CIRCLE,
                  PieceSet.GREEN_PINK_DOTTED_CROSS, PieceSet.YELLOW_DARK_BLUE_CASTLE),
            Piece(196, PieceSet.DARK_BLUE_PINK_CROSS_IN_CIRCLE, PieceSet.YELLOW_GREEN_SQUARE,
                  PieceSet.GREEN_PINK_DOTTED_CROSS, PieceSet.YELLOW_DARK_BLUE_CASTLE),
            Piece(197, PieceSet.GREEN_ORANGE_SPADE, PieceSet.DARK_BLUE_PINK_CROSS_IN_CIRCLE,
                  PieceSet.GREEN_PINK_DOTTED_CROSS, PieceSet.ORANGE_PURPLE_STAR),
            Piece(198, PieceSet.MAROON_YELLOW_STAR, PieceSet.DARK_BLUE_ORANGE_DOTTED_CROSS,
                  PieceSet.GREEN_PINK_DOTTED_CROSS, PieceSet.ORANGE_PURPLE_STAR),
            Piece(199, PieceSet.ORANGE_PURPLE_STAR, PieceSet.ORANGE_PURPLE_STAR,
                  PieceSet.GREEN_PINK_DOTTED_CROSS, PieceSet.ORANGE_PURPLE_STAR),
            Piece(200, PieceSet.MAROON_YELLOW_STAR, PieceSet.MAROON_GREEN_CROSS_IN_CIRCLE,
                  PieceSet.GREEN_PINK_DOTTED_CROSS, PieceSet.DARK_BLUE_ORANGE_DOTTED_CROSS),
            Piece(201, PieceSet.PINK_YELLOW_CASTLE, PieceSet.DARK_BLUE_ORANGE_DOTTED_CROSS,
                  PieceSet.GREEN_PINK_DOTTED_CROSS, PieceSet.DARK_BLUE_BLUE_SQUARE),
            Piece(202, PieceSet.DARK_BLUE_PINK_CROSS_IN_CIRCLE, PieceSet.BLUE_PINK_CASTLE,
                  PieceSet.GREEN_PINK_DOTTED_CROSS, PieceSet.DARK_BLUE_BLUE_SQUARE),
            Piece(203, PieceSet.YELLOW_DARK_BLUE_CASTLE, PieceSet.MAROON_YELLOW_STAR,
                  PieceSet.GREEN_PINK_DOTTED_CROSS, PieceSet.PINK_YELLOW_CASTLE),
            Piece(204, PieceSet.YELLOW_DARK_BLUE_CASTLE, PieceSet.DARK_BLUE_ORANGE_DOTTED_CROSS,
                  PieceSet.GREEN_PINK_DOTTED_CROSS, PieceSet.PINK_YELLOW_CASTLE),
            Piece(205, PieceSet.DARK_BLUE_BLUE_SQUARE, PieceSet.MAROON_GREEN_CROSS_IN_CIRCLE,
                  PieceSet.GREEN_PINK_DOTTED_CROSS, PieceSet.PINK_YELLOW_CASTLE),
            Piece(206, PieceSet.DARK_BLUE_PINK_CROSS_IN_CIRCLE, PieceSet.PINK_YELLOW_CASTLE,
                  PieceSet.GREEN_PINK_DOTTED_CROSS, PieceSet.PINK_YELLOW_CASTLE),
            Piece(207, PieceSet.DARK_BLUE_PINK_CROSS_IN_CIRCLE, PieceSet.BLUE_PINK_CASTLE,
                  PieceSet.MAROON_GREEN_CROSS_IN_CIRCLE, PieceSet.MAROON_GREEN_CROSS_IN_CIRCLE),
            Piece(208, PieceSet.MAROON_YELLOW_STAR, PieceSet.DARK_BLUE_PINK_CROSS_IN_CIRCLE,
                  PieceSet.MAROON_GREEN_CROSS_IN_CIRCLE, PieceSet.GREEN_ORANGE_SPADE)
        ]
        self.__piece_list = []
        self.__piece_list.extend(pieces_1_16)
        self.__piece_list.extend(pieces_17_32)
        self.__piece_list.extend(pieces_33_48)
        self.__piece_list.extend(pieces_49_64)
        self.__piece_list.extend(pieces_65_80)
        self.__piece_list.extend(pieces_81_96)
        self.__piece_list.extend(pieces_97_112)
        self.__piece_list.extend(pieces_113_128)
        self.__piece_list.extend(pieces_129_144)
        self.__piece_list.extend(pieces_145_160)
        self.__piece_list.extend(pieces_161_176)
        self.__piece_list.extend(pieces_177_192)
        self.__piece_list.extend(pieces_193_208)

    def get_piece(self, piece_number: int) -> Piece:
        return self.__piece_list[piece_number - 1]

    def get_no_placed_pieces(self, placed_pieces: list[PlacedPiece]) -> list[Piece]:
        pieces_without_rotation: list[Piece] = [placed_piece.get_piece() for placed_piece in placed_pieces]
        return [piece for piece in self.__piece_list if piece not in pieces_without_rotation]

    def search(self, constraints: Constraints) -> list[RotatedPiece]:
        valid_pieces: list[RotatedPiece] = []
        for piece in self.__piece_list:
            rotation: Optional[Rotation] = piece.is_valid(constraints)
            if rotation:
                valid_pieces.append(RotatedPiece(piece, rotation))
        return valid_pieces
