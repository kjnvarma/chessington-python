"""
Definitions of each of the different chess pieces.
"""

from abc import ABC, abstractmethod

from chessington.engine.data import Player, Square

class Piece(ABC):
    """
    An abstract base class from which all pieces inherit.
    """

    def __init__(self, player):
        self.player = player

    @abstractmethod
    def get_available_moves(self, board):
        """
        Get all squares that the piece is allowed to move to.
        """
        pass


class Pawn(Piece):
    """
    A class representing a chess pawn.
    """

    def move_to(self, board, to_square):
        current_square = board.find_piece(self)
        board.move_piece(current_square, to_square)

    def get_available_moves(self, board):
        square = board.find_piece(self)

        if square.row not in [0, 7, 1, 6]:
            if self.player == Player.WHITE:
                return [Square.at(square.row + 1, square.col)]
            if self.player == Player.BLACK:
                return [Square.at(square.row - 1, square.col)]
        if square.row in [1, 6]:
            if self.player == Player.WHITE:
                return [Square.at(square.row + 1, square.col), Square.at(square.row + 2, square.col)]
            if self.player == Player.BLACK:
                return [Square.at(square.row - 1, square.col), Square.at(square.row - 2, square.col)]

        return []


class Knight(Piece):
    """
    A class representing a chess knight.
    """

    def get_available_moves(self, board):
        return []


class Bishop(Piece):
    """
    A class representing a chess bishop.
    """

    def get_available_moves(self, board):
        return []


class Rook(Piece):
    """
    A class representing a chess rook.
    """

    def get_available_moves(self, board):
        return []


class Queen(Piece):
    """
    A class representing a chess queen.
    """

    def get_available_moves(self, board):
        return []


class King(Piece):
    """
    A class representing a chess king.
    """

    def get_available_moves(self, board):
        return []