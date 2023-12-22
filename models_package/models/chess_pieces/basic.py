"""This class signifies a basic chess piece and lists the necessary fields and methods a piece needs to 
implement.
"""
from abc import ABC, abstractmethod, abstractproperty


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
