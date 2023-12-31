"""This class signifies a basic chess piece and lists the necessary fields and methods a piece needs to 
implement.
"""
from abc import ABC, abstractmethod, abstractproperty

END_ROW = 7
START_ROW = 0
START_COL = 0
END_COL = 7


class ChessPiece(ABC):

    def __init__(self, rank='empty', color='white'):
        self.rank = rank
        self.color = color


    @abstractmethod
    def move(self, board, position):
        pass


    @abstractmethod
    def check_available_moves(self, board):
        pass


    def verify_board_raw(self, row):
        if row >= START_ROW and row <= END_ROW:
            return True
        else:
            return False

    
    def verify_board_col(self, col):
        if col >= START_COL and col <= END_COL:
            return True
        else:
            return False


    def verify_board_piece(self, piece):
        if not piece or piece.color != self.color:
            return True
        else:
            return False


    @property
    def rank(self):
        return self.__rank

    
    @rank.setter
    def rank(self, rank):
        self.__rank = rank

    
    @property
    def color(self):
        return self.__color

    
    @color.setter
    def color(self, color):
        self.__color = color



if __name__=='__main__':
    # Verify class cannot be instantiated
    try:
        cp = ChessPiece()
        print('cp.rank: ', cp.rank)
        print('cp.color: ', cp.color)
    except Exception as e:
        print('Error instantiating ChessPiece base class: \n', e)
