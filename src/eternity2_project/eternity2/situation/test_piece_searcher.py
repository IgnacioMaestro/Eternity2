from unittest import TestCase

from src.eternity2_project.eternity2.game.board import Board
from src.eternity2_project.eternity2.game.piece_set import PieceSet
from src.eternity2_project.eternity2.piece.constraints import Constraints
from src.eternity2_project.eternity2.piece.rotated_piece import RotatedPiece
from src.eternity2_project.eternity2.piece.rotation import Rotation
from src.eternity2_project.eternity2.situation.piece_searcher import PieceSearcher
from src.eternity2_project.eternity2.situation.placed_piece import PlacedPiece


class TestPieceSearcher(TestCase):
    def setUp(self):
        self.placed_piece = PlacedPiece(
            Board().get_square(0, 0), RotatedPiece(PieceSet().get_piece(139), Rotation.DEGREE_0))
        self.edge_placed_piece = PlacedPiece(
            Board().get_square(0, 0), RotatedPiece(PieceSet().get_piece(5), Rotation.DEGREE_0))
        self.corner_placed_piece = PlacedPiece(
            Board().get_square(0, 0), RotatedPiece(PieceSet().get_piece(1), Rotation.DEGREE_0))

    def test_search_all_constraints_none(self):
        # Arrange
        constraints = Constraints(None, None, None, None)

        # Act
        rotated_pieces: list[RotatedPiece] = PieceSearcher([], constraints).search()

        # Assert
        self.assertEqual(len(rotated_pieces), 240 - 60)

    def test_search_one_constraints_edge(self):
        # Arrange
        constraints = Constraints(PieceSet.EDGE, None, None, None)

        # Act
        rotated_pieces: list[RotatedPiece] = PieceSearcher([], constraints).search()

        # Assert
        self.assertEqual(len(rotated_pieces), 60 - 4)

    def test_search_two_constraints_edge(self):
        # Arrange
        constraints = Constraints(PieceSet.EDGE, PieceSet.EDGE, None, None)

        # Act
        rotated_pieces: list[RotatedPiece] = PieceSearcher([], constraints).search()

        # Assert
        self.assertEqual(len(rotated_pieces), 4)

    def test_search_all_constraints_equal(self):
        # Arrange
        constraints = Constraints(
            PieceSet.BLUE_PINK_CASTLE, PieceSet.BLUE_PINK_CASTLE, PieceSet.BLUE_PINK_CASTLE, PieceSet.BLUE_PINK_CASTLE)

        # Act
        rotated_pieces: list[RotatedPiece] = PieceSearcher([], constraints).search()

        # Assert
        self.assertEqual(len(rotated_pieces), 0)

    def test_search_all_constraints_none_one_placed_pieces(self):
        # Arrange
        constraints = Constraints(None, None, None, None)

        # Act
        rotated_pieces: list[RotatedPiece] = PieceSearcher([self.placed_piece], constraints).search()

        # Assert
        self.assertEqual(len(rotated_pieces), 240 - 60 - 1)

    def test_search_one_constraints_edge_one_placed_pieces_no_edge(self):
        # Arrange
        constraints = Constraints(PieceSet.EDGE, None, None, None)

        # Act
        rotated_pieces: list[RotatedPiece] = PieceSearcher([self.placed_piece], constraints).search()

        # Assert
        self.assertEqual(len(rotated_pieces), 60 - 4)

    def test_search_one_constraints_edge_one_placed_pieces_edge(self):
        # Arrange
        constraints = Constraints(PieceSet.EDGE, None, None, None)

        # Act
        rotated_pieces: list[RotatedPiece] = PieceSearcher([self.edge_placed_piece], constraints).search()

        # Assert
        self.assertEqual(len(rotated_pieces), 60 - 4 - 1)

    def test_search_two_constraints_edge_one_placed_pieces_no_corner(self):
        # Arrange
        constraints = Constraints(PieceSet.EDGE, PieceSet.EDGE, None, None)

        # Act
        rotated_pieces: list[RotatedPiece] = PieceSearcher([self.placed_piece], constraints).search()

        # Assert
        self.assertEqual(len(rotated_pieces), 4)

    def test_search_two_constraints_edge_one_placed_pieces_corner(self):
        # Arrange
        constraints = Constraints(PieceSet.EDGE, PieceSet.EDGE, None, None)

        # Act
        rotated_pieces: list[RotatedPiece] = PieceSearcher([self.corner_placed_piece], constraints).search()

        # Assert
        self.assertEqual(len(rotated_pieces), 4 - 1)
