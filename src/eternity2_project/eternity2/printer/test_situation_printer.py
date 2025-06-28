from unittest import TestCase
from typing import List, Optional

from src.eternity2_project.eternity2.piece.color import Color
from src.eternity2_project.eternity2.css_color.css_color import CSSColor
from src.eternity2_project.eternity2.piece.piece import Piece
from src.eternity2_project.eternity2.piece.rotation import Rotation
from src.eternity2_project.eternity2.piece.rotated_piece import RotatedPiece
from src.eternity2_project.eternity2.printer.situation_printer import SituationPrinter


class TestSituationPrinter(TestCase):
    def setUp(self):
        # Create some colors for testing
        self.edge_color = Color(1, CSSColor("#000000"), CSSColor("#FFFFFF"), "Edge")
        self.color1 = Color(2, CSSColor("#FF0000"), CSSColor("#00FF00"), "Color1")
        self.color2 = Color(3, CSSColor("#0000FF"), CSSColor("#FFFF00"), "Color2")

        # Create some pieces for testing
        self.piece1 = Piece(1, self.edge_color, self.color1, self.color2, self.edge_color)
        self.piece2 = Piece(2, self.color1, self.color2, self.edge_color, self.color1)

        # Create some rotated pieces for testing
        self.rotated_piece1 = RotatedPiece(self.piece1, Rotation.DEGREE_0)
        self.rotated_piece2 = RotatedPiece(self.piece2, Rotation.DEGREE_90)

        # Create a list of 16x16=256 pieces (some rotated pieces and some None)
        # We'll create a pattern where each row alternates between rotated_piece1 and rotated_piece2
        self.pieces_list: List[Optional[RotatedPiece]] = []
        for i in range(SituationPrinter.ROW_COUNT):
            row = []
            for j in range(SituationPrinter.ROW_WIDTH):
                if (i + j) % 2 == 0:
                    row.append(self.rotated_piece1)
                else:
                    row.append(self.rotated_piece2)
            self.pieces_list.extend(row)

    def test_constructor(self):
        # Arrange & Act
        situation_printer = SituationPrinter(self.pieces_list)

        # Assert
        self.assertIsNotNone(situation_printer)

    def test_create_valid(self):
        # Arrange & Act
        situation_printer = SituationPrinter.create(self.pieces_list)

        # Assert
        self.assertIsNotNone(situation_printer)

    def test_create_invalid_length(self):
        # Arrange
        invalid_pieces_list = self.pieces_list[:-1]  # Remove one element to make it invalid

        # Act & Assert
        with self.assertRaises(ValueError):
            SituationPrinter.create(invalid_pieces_list)

    def test_print_row(self):
        # Arrange
        situation_printer = SituationPrinter(self.pieces_list)
        row_index = 0

        # Act
        result = situation_printer.print_row(row_index)

        # Assert
        self.assertIsNotNone(result)
        # We don't test the exact output because it depends on LinePrinter.print_row_in_3_lines()
        # which is already tested in TestLinePrinter
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

    def test_print(self):
        # Arrange
        situation_printer = SituationPrinter(self.pieces_list)

        # Act
        result = situation_printer.print()
        print(result)
        # Assert
        self.assertIsNotNone(result)
        # We don't test the exact output because it depends on LinePrinter.print_row_in_3_lines()
        # which is already tested in TestLinePrinter
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

    def test_print_with_none_pieces(self):
        # Arrange
        # Create a list with some None pieces
        pieces_with_none = self.pieces_list.copy()
        pieces_with_none[0] = None
        pieces_with_none[15] = None
        pieces_with_none[16] = None
        pieces_with_none[255] = None
        situation_printer = SituationPrinter(pieces_with_none)

        # Act
        result = situation_printer.print()

        # Assert
        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
