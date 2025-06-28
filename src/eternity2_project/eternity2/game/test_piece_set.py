from typing import Optional
from unittest import TestCase

from src.eternity2_project.eternity2.game.board import Board
from src.eternity2_project.eternity2.game.piece_set import PieceSet
from src.eternity2_project.eternity2.game.color import Color
from src.eternity2_project.eternity2.game.piece import Piece
from src.eternity2_project.eternity2.rotated_piece.rotated_piece import RotatedPiece
from src.eternity2_project.eternity2.rotated_piece.rotation import Rotation
from src.eternity2_project.eternity2.situation.placed_piece import PlacedPiece


class TestPieceSet(TestCase):
    def test_get_no_placed_pieces_no_placed_pieces(self):
        # Act
        pieces: list[Piece] = PieceSet().get_no_placed_pieces([])

        # Assert
        self.assertEqual(len(pieces), 256)

    def test_get_no_placed_pieces_one_placed_piece(self):
        # Arrange
        piece: Piece = Piece(1, PieceSet.ORANGE_BLUE_CROSS, PieceSet.PINK_BLUE_CROSS, PieceSet.EDGE, PieceSet.EDGE)
        placed_piece: PlacedPiece = PlacedPiece(Board().get_square(0, 0), RotatedPiece(piece, Rotation.DEGREE_0))

        # Act
        pieces: list[Piece] = PieceSet().get_no_placed_pieces([placed_piece])

        # Assert
        self.assertEqual(len(pieces), 255)

    def test_check_pieces(self):

        codes = ["AQXX", "AEXX", "IQXX", "QIXX", "BAXA", "JIXA", "FAXA", "FMXA", "KQXA", "GEXA", "OIXA", "HEXA", "HMXA",
                 "UEXA", "JAXI", "RQXI", "NMXI", "SMXI", "GIXI", "OIXI", "DEXI", "LAXI", "LMXI", "TAXI", "UAXI", "BIXQ",
                 "BQXQ", "JQXQ", "RQXQ", "GMXQ", "OIXQ", "TQXQ", "HIXQ", "HEXQ", "PMXQ", "VEXQ", "RAXE", "CMXE", "KMXE",
                 "SIXE", "SQXE", "OAXE", "OIXE", "OQXE", "DAXE", "TEXE", "HEXE", "PEXE", "BMXM", "JAXM", "JIXM", "FAXM",
                 "GEXM", "DEXM", "DMXM", "HQXM", "PAXM", "PMXM", "UIXM", "VQXM", "FRBB", "NGBB", "JCBJ", "BHBR", "RVBR",
                 "NNBR", "KJBR", "TFBR", "VHBR", "CGBC", "GLBC", "NRBK", "ODBK", "TOBK", "HCBK", "NOBS", "SOBS", "CPBG",
                 "TCBG", "PUBG", "SRBO", "RRBD", "KDBD", "RSBL", "FNBL", "HLBL", "PTBL", "BUBT", "FVBT", "DPBT", "KLBH",
                 "SOBH", "SDBH", "DUBH", "LNBH", "UCBU", "DSBV", "THBV", "UFBV", "VUBV", "LOJJ", "LPJJ", "PSJJ", "VFJJ",
                 "DOJR", "CHJF", "SHJF", "DOJF", "PKJF", "OLJN", "LOJN", "TSJC", "TPJC", "NDJK", "GLJK", "LKJK", "VPJK",
                 "CUJS", "PLJG", "HVJO", "NVJD", "FPJT", "NSJT", "TOJT", "LVJH", "UOJH", "NFJP", "SUJP", "DCJP", "THJP",
                 "FTJU", "LNJU", "NPJV", "KDJV", "DCJV", "PTJV", "TGRR", "FCRF", "FKRF", "FLRF", "SURF", "OFRF", "PLRF",
                 "UURF", "CDRN", "RLRC", "RVRC", "CNRC", "OLRC", "FKRS", "DVRS", "KKRG", "KSRG", "VPRG", "GGRD", "GLRD",
                 "VGRD", "GPRT", "HFRT", "UURH", "FTRP", "NTRP", "OKRV", "DPRV", "CDFN", "DHFN", "CCFK", "KOFS", "SUFS",
                 "DHFG", "TPFG", "UKFG", "OOFO", "LTFO", "GUFD", "GSFL", "NDFT", "LPFH", "HOFH", "GPFP", "KPFU", "GKFU",
                 "SHNN", "VGNC", "SLNK", "HHNK", "UGNS", "NUNG", "CSNG", "PSNG", "CCNO", "OTNO", "KGND", "UKNL", "UVNL",
                 "VONL", "KVNT", "SHNT", "TTNT", "SCNH", "UHNP", "VGNP", "LSNU", "LHNU", "PCNU", "VUNU", "VGCC", "SVCK",
                 "HOCK", "KSCG", "POCG", "CPCO", "HHCD", "CTCL", "DVCL", "VUCL", "SOCT", "DLCP", "KDCU", "KPCV", "UUCV",
                 "UVCV", "LVKK", "TGKK", "POKK", "SOKG", "LLKG", "SHKD", "GVKT", "PHKT", "LTKH", "LUKH", "STSS", "PDSG",
                 "GDSD", "GTSD", "LOSD", "DPSL", "OVST", "UOST", "GUSH", "DUSH", "OLGO", "THGO", "VTGD", "PVGU", "UVOO",
                 "LDOD", "DUOL", "PUOT", "VHDD", "HLDL", "PTLH", "UPTP", "PVTV", "UVHV"]
        for index, code in enumerate(codes):
            piece: Piece = PieceSet().get_piece(index + 1)
            self.assertEqual(piece.get_up_color(), self.convert_to_color(code[0]))
            self.assertEqual(piece.get_right_color(), self.convert_to_color(code[1]))
            self.assertEqual(piece.get_down_color(), self.convert_to_color(code[2]))
            self.assertEqual(piece.get_left_color(), self.convert_to_color(code[3]))

    @classmethod
    def search_color_1_to_10(cls, code_letter: str) -> Optional[Color]:
        if code_letter == "X":
            return PieceSet.EDGE
        if code_letter == "A":
            return PieceSet.ORANGE_BLUE_CROSS
        if code_letter == "Q":
            return PieceSet.PINK_BLUE_CROSS
        if code_letter == "E":
            return PieceSet.GREEN_DARK_BLUE_HEXAGON
        if code_letter == "I":
            return PieceSet.DARK_BLUE_YELLOW_FLOWER
        if code_letter == "B":
            return PieceSet.PINK_YELLOW_DOTTED_CROSS
        if code_letter == "J":
            return PieceSet.PURPLE_BLUE_SPADE
        if code_letter == "F":
            return PieceSet.PURPLE_YELLOW_CROSS_IN_CIRCLE
        if code_letter == "M":
            return PieceSet.BROWN_ORANGE
        if code_letter == "K":
            return PieceSet.GREEN_ORANGE_SPADE
        return None

    @classmethod
    def search_color_11_to_23(cls, code_letter: str) -> Optional[Color]:
        if code_letter == "G":
            return PieceSet.BLUE_PINK_CASTLE
        if code_letter == "O":
            return PieceSet.YELLOW_GREEN_SQUARE
        if code_letter == "H":
            return PieceSet.DARK_BLUE_ORANGE_DOTTED_CROSS
        if code_letter == "U":
            return PieceSet.PINK_YELLOW_CASTLE
        if code_letter == "R":
            return PieceSet.YELLOW_BLUE_STAR
        if code_letter == "N":
            return PieceSet.GREEN_PINK_DOTTED_CROSS
        if code_letter == "S":
            return PieceSet.MAROON_YELLOW_STAR
        if code_letter == "D":
            return PieceSet.BLUE_PINK_SPADE
        if code_letter == "L":
            return PieceSet.YELLOW_DARK_BLUE_CASTLE
        if code_letter == "T":
            return PieceSet.ORANGE_PURPLE_STAR
        if code_letter == "P":
            return PieceSet.DARK_BLUE_BLUE_SQUARE
        if code_letter == "V":
            return PieceSet.DARK_BLUE_PINK_CROSS_IN_CIRCLE
        return PieceSet.MAROON_GREEN_CROSS_IN_CIRCLE

    @classmethod
    def convert_to_color(cls, code_letter: str) -> Color:
        color_1_to_10: Optional[Color] = cls.search_color_1_to_10(code_letter)
        if color_1_to_10 is not None:
            return color_1_to_10
        return cls.search_color_11_to_23(code_letter)
