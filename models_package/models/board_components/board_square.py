"""This class represents a single square on the chess board."""
from chess_pieces.basic import ChessPiece


class BoardSquare:

    def __init__(self, pos, color, piece=None):
        self._position = position
        self._color = color
        self._piece = piece

    
    @property
    def position(self):
        return self._position
    

    @property
    def color(self):
        return self._color

    
    @property
    def piece(self):
        return self._piece

    @piece.setter
    def piece(self, chess_piece):
        if isinstance(chess_piece, ChessPiece):
            self._piece = chess_piece
        else:
            print('Trying to set non ChessPiece object to the piece attribute of the BoardSquare -> NOT ALLOWED!!!')

    @piece.deleter
    def piece(self):
        self._piece = None
