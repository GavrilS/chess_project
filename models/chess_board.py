"""This is the class that will implement the chess board."""
from models.chess_pieces.basic import ChessPiece

WHITE_FIELD_VALUE = 0
BLACK_FIELD_VALUE = 1
POS_ONE_ROWS = (0, 1)
POS_TWO_ROWS = (6, 7)
ROOK_POS = (0, 7)
KNIGHT_POS = (1, 6)
BISHOP_POS = (2, 5)
ROYAL_POS = (3, 4)
PAWN_POS = (0, 1, 2, 3, 4, 5, 6, 7)


class ChessBoard:
    

    def __init__(self):
        self._build_board()


    def status(self):
        # print('*******Board*******')
        for i in range(8):
            for j in range(8):
                print(self._board[i][j], end=' ')
            print()


    def _populate_board(self, pos_one_pieces, pos_two_pieces):
        for piece in pos_one_pieces:
            self._verify_piece(piece)
            pawn_row = POS_ONE_ROWS[1]
            non_pawn_row = POS_ONE_ROWS[0]
            if piece.rank == 'pawn':
                col = self._check_pos(row=pawn_row, PAWN_POS)
                self.set_piece(row=pawn_row, col, piece)
            elif piece.ran = 'rook':
                col = self._check_pos(row=non_pawn_row, ROOK_POS)
                self.set_piece(row=non_pawn_row, col, piece)


    def set_piece(self, row, col, piece):
        self._board[row][col] = piece

    
    def _check_pos(self, row, columns):
        for i in columns:
            if not isinstance(self._board[row][i], ChessPiece):
                return i
        print('No empty position found among the supplied options for this piece... Exiting!')
        exit()


    def _verify_piece(self, piece):
        if not isinstance(piece, ChessPiece):
                print('A piece was provided that does not belong to the board... Exiting!')
                exit()


    def _build_board(self):
        board = []
        current_field_val = WHITE_FIELD_VALUE
        for i in range(8):
            row = []
            board.append(row)
            for j in range(8):
                board[i].append(current_field_val)
                if current_field_val == 0:
                    current_field_val = 1
                else:
                    current_field_val = 0

            if current_field_val == 0:
                current_field_val = 1
            else:
                current_field_val = 0

        self._board = board



if __name__=='__main__':
    print('Testing chess board class creation.')
    b = ChessBoard()
    b.status()
    print('Test finished.')
