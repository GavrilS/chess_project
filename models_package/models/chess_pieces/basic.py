"""This class signifies a basic chess piece and lists the necessary fields and methods a piece needs to 
implement.
"""
from abc import ABC, abstractmethod, abstractproperty

END_ROW = 7
START_ROW = 0
START_COL = 0
END_COL = 7


class ChessPiece(ABC):
    '''The basic chess piece class; all pieces inherit from this one.
        Required parameters:
            rank: the type of piece - queen, king, pawn...
            color: the color of the piece - white or black
            start_position: 2 options - low(starts at the rows with index 0 and 1) or high(starts at rows with 
            index 6 or 7)
    '''

    def __init__(self, rank='empty', color='white', start_position='low'):
        self.rank = rank
        self.color = color
        self.start_position = start_position


    def move(self, board, position, next_position):
        possible_moves = self.check_available_moves(board, position)
        if next_position in possible_moves:
            return True
        else:
            return False


    def get_coordinates(self, position):
        current_coordinates = position.split(':')
        row = int(current_coordinates[0])
        col = int(current_coordinates[1])

        return row, col


    @abstractmethod
    def check_available_moves(self, board, position):
        pass


    def verify_board_row(self, row):
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


    @property
    def start_position(self):
        return self.__start_position


    @start_position.setter
    def start_position(self, start_position):
        self.__start_position = start_position



if __name__=='__main__':
    # Verify class cannot be instantiated
    try:
        cp = ChessPiece()
        print('cp.rank: ', cp.rank)
        print('cp.color: ', cp.color)
    except Exception as e:
        print('Error instantiating ChessPiece base class: \n', e)
