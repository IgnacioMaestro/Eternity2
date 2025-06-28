from unittest import TestCase
from typing import List, Optional

from src.eternity2_project.eternity2.css_color.css_color import CSSColor
from src.eternity2_project.eternity2.printer.line_printer import LinePrinter
from src.eternity2_project.eternity2.game.color import Color
from src.eternity2_project.eternity2.rotated_piece.piece import Piece
from src.eternity2_project.eternity2.rotated_piece.rotated_piece import RotatedPiece
from src.eternity2_project.eternity2.rotated_piece.rotation import Rotation


class TestLinePrinter(TestCase):
    def setUp(self):
        # Set maxDiff to None to see the full diff when tests fail
        self.maxDiff = None

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

        # Create a list of 16 pieces (some rotated pieces and some None)
        self.pieces_list: List[Optional[RotatedPiece]] = [
            self.rotated_piece1, self.rotated_piece2, None, self.rotated_piece1,
            self.rotated_piece2, None, self.rotated_piece1, self.rotated_piece2,
            None, self.rotated_piece1, self.rotated_piece2, None,
            self.rotated_piece1, self.rotated_piece2, None, self.rotated_piece1
        ]

    def test_constructor(self):
        # Arrange & Act
        line_printer = LinePrinter(self.pieces_list)

        # Assert
        self.assertIsNotNone(line_printer)

    def test_create_valid(self):
        # Arrange & Act
        line_printer = LinePrinter.create(self.pieces_list)

        # Assert
        self.assertIsNotNone(line_printer)

    def test_create_invalid_length(self):
        # Arrange
        invalid_pieces_list = self.pieces_list[:-1]  # Remove one element to make it invalid

        # Act & Assert
        with self.assertRaises(ValueError):
            LinePrinter.create(invalid_pieces_list)

    def test_print_up_piece_empty(self):
        # Arrange
        line_printer = LinePrinter(self.pieces_list)

        # Act
        result = line_printer.print_up_piece(None)

        # Assert
        expected_up_piece = " " * LinePrinter.PIECE_WIDTH
        self.assertEqual(expected_up_piece, result)

    def test_print_up_piece_no_empty(self):
        # Arrange
        line_printer = LinePrinter(self.pieces_list)

        # Act
        result = line_printer.print_up_piece(self.rotated_piece1)

        # Assert
        expected_up_piece = " " * 24 + str(self.rotated_piece1.get_up_color()) + " " * 24
        self.assertEqual(expected_up_piece, result)

    def test_print_row_up_line(self):
        # Arrange
        line_printer = LinePrinter(self.pieces_list)

        # Act
        up_line: str = line_printer.print_row_up_line()

        # Assert
        expected_up_line = (
                line_printer.print_up_piece(self.rotated_piece1) + "|" +
                line_printer.print_up_piece(self.rotated_piece2) + "|" +
                line_printer.print_up_piece(None) + "|" +
                line_printer.print_up_piece(self.rotated_piece1) + "|" +
                line_printer.print_up_piece(self.rotated_piece2) + "|" +
                line_printer.print_up_piece(None) + "|" +
                line_printer.print_up_piece(self.rotated_piece1) + "|" +
                line_printer.print_up_piece(self.rotated_piece2) + "|" +
                line_printer.print_up_piece(None) + "|" +
                line_printer.print_up_piece(self.rotated_piece1) + "|" +
                line_printer.print_up_piece(self.rotated_piece2) + "|" +
                line_printer.print_up_piece(None) + "|" +
                line_printer.print_up_piece(self.rotated_piece1) + "|" +
                line_printer.print_up_piece(self.rotated_piece2) + "|" +
                line_printer.print_up_piece(None) + "|" +
                line_printer.print_up_piece(self.rotated_piece1) + "\n")
        self.assertEqual(expected_up_line, up_line)

    def test_print_center_piece_empty(self):
        # Arrange
        line_printer = LinePrinter(self.pieces_list)

        # Act
        center_piece: str = line_printer.print_center_piece(None)

        # Assert
        expected_center_piece = " " * LinePrinter.PIECE_WIDTH
        self.assertEqual(expected_center_piece, center_piece)

    def test_print_center_piece_no_empty(self):
        # Arrange
        line_printer = LinePrinter(self.pieces_list)

        # Act
        center_piece: str = line_printer.print_center_piece(self.rotated_piece1)

        # Assert
        expected_center_piece = (
                str(self.rotated_piece1.get_left_color()) + " " * 42 + str(self.rotated_piece1.get_right_color()))
        self.assertEqual(expected_center_piece, center_piece)

    def test_print_row_center_line(self):
        # Arrange
        line_printer = LinePrinter(self.pieces_list)

        # Act
        up_line: str = line_printer.print_row_center_line()

        # Assert
        expected_up_line = (
                line_printer.print_center_piece(self.rotated_piece1) + "|" +
                line_printer.print_center_piece(self.rotated_piece2) + "|" +
                line_printer.print_center_piece(None) + "|" +
                line_printer.print_center_piece(self.rotated_piece1) + "|" +
                line_printer.print_center_piece(self.rotated_piece2) + "|" +
                line_printer.print_center_piece(None) + "|" +
                line_printer.print_center_piece(self.rotated_piece1) + "|" +
                line_printer.print_center_piece(self.rotated_piece2) + "|" +
                line_printer.print_center_piece(None) + "|" +
                line_printer.print_center_piece(self.rotated_piece1) + "|" +
                line_printer.print_center_piece(self.rotated_piece2) + "|" +
                line_printer.print_center_piece(None) + "|" +
                line_printer.print_center_piece(self.rotated_piece1) + "|" +
                line_printer.print_center_piece(self.rotated_piece2) + "|" +
                line_printer.print_center_piece(None) + "|" +
                line_printer.print_center_piece(self.rotated_piece1) + "\n")
        self.assertEqual(expected_up_line, up_line)

    def test_print_down_piece_empty(self):
        # Arrange
        line_printer = LinePrinter(self.pieces_list)

        # Act
        result = line_printer.print_down_piece(None)

        # Assert
        expected_down_piece = " " * LinePrinter.PIECE_WIDTH
        self.assertEqual(expected_down_piece, result)

    def test_print_down_piece_no_empty(self):
        # Arrange
        line_printer = LinePrinter(self.pieces_list)

        # Act
        result = line_printer.print_down_piece(self.rotated_piece1)

        # Assert
        expected_down_piece = " " * 23 + str(self.rotated_piece1.get_down_color()) + " " * 23
        self.assertEqual(expected_down_piece, result)

    def test_print_row_down_line(self):
        # Arrange
        line_printer = LinePrinter(self.pieces_list)

        # Act
        down_line: str = line_printer.print_row_down_line()

        # Assert
        expected_down_line = (
                line_printer.print_down_piece(self.rotated_piece1) + "|" +
                line_printer.print_down_piece(self.rotated_piece2) + "|" +
                line_printer.print_down_piece(None) + "|" +
                line_printer.print_down_piece(self.rotated_piece1) + "|" +
                line_printer.print_down_piece(self.rotated_piece2) + "|" +
                line_printer.print_down_piece(None) + "|" +
                line_printer.print_down_piece(self.rotated_piece1) + "|" +
                line_printer.print_down_piece(self.rotated_piece2) + "|" +
                line_printer.print_down_piece(None) + "|" +
                line_printer.print_down_piece(self.rotated_piece1) + "|" +
                line_printer.print_down_piece(self.rotated_piece2) + "|" +
                line_printer.print_down_piece(None) + "|" +
                line_printer.print_down_piece(self.rotated_piece1) + "|" +
                line_printer.print_down_piece(self.rotated_piece2) + "|" +
                line_printer.print_down_piece(None) + "|" +
                line_printer.print_down_piece(self.rotated_piece1) + "\n")
        self.assertEqual(expected_down_line, down_line)

    def test_print_row_line(self):
        # Arrange
        line_printer = LinePrinter(self.pieces_list)

        # Act
        row_line: str = line_printer.print_row_in_3_lines()

        # Assert
        expected_row_line = (
                line_printer.print_row_up_line() +
                line_printer.print_row_center_line() +
                line_printer.print_row_down_line())
        self.assertEqual(expected_row_line, row_line)
        print(row_line)
