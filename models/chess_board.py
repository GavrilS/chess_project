"""This is the class that will implement the chess board."""

EMPTY_FIELD_VALUE = 0

class ChessBoard:
    

    def __init__(self):
        self._build_board()


    def status(self):
        # print('*******Board*******')
        for i in range(8):
            for j in range(8):
                print(self._board[i][j], end=' ')
            print()


    def _populate_board(self):
        pass


    def _build_board(self):
        board = []
        for i in range(8):
            row = []
            board.append(row)
            for j in range(8):
                board[i].append(EMPTY_FIELD_VALUE)

        self._board = board



if __name__=='__main__':
    print('Testing chess board class creation.')
    b = ChessBoard()
    b.status()
    print('Test finished.')
