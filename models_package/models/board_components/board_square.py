"""This class represents a single square on the chess board."""
from chess_pieces.basic import ChessPiece


class BoardSquare:

    def __init__(self, position, color, piece=None):
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


    def __str__(self):
        if not self._piece:
            # return f"{self._position}:{self._color[0]}"
            return f"{self._position}{self._color[0].upper()}"
        # return f"{self._position}:{self._color[0]}:{self._piece}"
        return f"{self._position}{self._color[0].upper()}:{self._piece}"


    def __repr__(self):
        if not self._piece:
            return f"BoardSquare('{self._position}', '{self._color}')"
        return f"BoardSquare('{self._position}', '{self._color}', {self._piece})"
