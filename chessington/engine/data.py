"""
Data classes for easy representation of concepts such as a square on the board or a player.
"""

from collections import namedtuple
from enum import Enum, auto

class Player(Enum):
    """
    The two players in a game of chess.
    """
    WHITE = auto()
    BLACK = auto()

    def opponent(self):
        if self == Player.WHITE: return Player.BLACK
        else: return Player.WHITE


class Square(namedtuple('Square', 'row col')):
    """
    An immutable pair (row, col) representing the coordinates of a square.
    """

    @staticmethod
    def at(row, col):
        """
        Creates a square at the given row and column.
        """
        return Square(row=row, col=col)