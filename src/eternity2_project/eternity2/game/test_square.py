from unittest import TestCase

from src.eternity2_project.eternity2.game.square import Square


class TestSquare(TestCase):
    def test_is_corner_corner(self):
        # Arrange
        square: Square = Square(0, 0)

        # Act
        is_corner: bool = square.is_corner()

        # Assert
        self.assertTrue(is_corner)

        # Arrange
        square: Square = Square(0, 15)

        # Act
        is_corner: bool = square.is_corner()

        # Assert
        self.assertTrue(is_corner)

        # Arrange
        square: Square = Square(15, 0)

        # Act
        is_corner: bool = square.is_corner()

        # Assert
        self.assertTrue(is_corner)

        # Arrange
        square: Square = Square(15, 15)

        # Act
        is_corner: bool = square.is_corner()

        # Assert
        self.assertTrue(is_corner)

    def test_is_corner_border(self):
        # Arrange
        square: Square = Square(0, 1)

        # Act
        is_corner: bool = square.is_corner()

        # Assert
        self.assertFalse(is_corner)

    def test_is_corner_internal(self):
        # Arrange
        square: Square = Square(1, 1)

        # Act
        is_corner: bool = square.is_corner()

        # Assert
        self.assertFalse(is_corner)
