"""This is the class that will implement the chess board."""
from chess_pieces.basic import ChessPiece
from board_components.board_square import BoardSquare

ROWS = [1, 2, 3, 4, 5, 6, 7, 8]
COLS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
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
        self._coordinates = {}
        self._build_board()
        self.status()
        # print('*******Board*******')


    def status(self):
        # print('*******Board*******')
        for i in range(8):
            for j in range(8):
                print(self._board[i][j], end=' ')
            print()


    def populate_board(self, pos_one_pieces, pos_two_pieces):
        for piece in pos_one_pieces:
            self._verify_piece(piece)
            pawn_row = POS_ONE_ROWS[1]
            non_pawn_row = POS_ONE_ROWS[0]
            if piece.rank == 'pawn':
                col = self._check_initial_pos(row=pawn_row, columns=PAWN_POS)
                print('pawn initial col -> ', col)
                self.set_piece(row=pawn_row, col=col, piece=piece)
            elif piece.rank == 'rook':
                col = self._check_initial_pos(row=non_pawn_row, columns=ROOK_POS)
                print('rook initial col -> ', col)
                self.set_piece(row=non_pawn_row, col=col, piece=piece)
            elif piece.rank == 'knight':
                col = self._check_initial_pos(row=non_pawn_row, columns=KNIGHT_POS)
                print('knight initial col -> ', col)
                self.set_piece(row=non_pawn_row, col=col, piece=piece)
            elif piece.rank == 'bishop':
                col = self._check_initial_pos(row=non_pawn_row, columns=BISHOP_POS)
                print('bishop initial col -> ', col)
                self.set_piece(row=non_pawn_row, col=col, piece=piece)
            elif piece.rank == 'queen':
                col = self._select_royal_pos(row=non_pawn_row, piece=piece)
                print('queen initial col -> ', col)
                self.set_piece(row=non_pawn_row, col=col, piece=piece)
            elif piece.rank == 'king':
                col = self._select_royal_pos(row=non_pawn_row, piece=piece)
                print('king initial col -> ', col)
                self.set_piece(row=non_pawn_row, col=col, piece=piece)


    def set_piece(self, row, col, piece):
        try:
            self._board[row][col].piece = piece
        except Exception as e:
            print('ERROR trying to assign piece to a specific field on the board -> \n', e)


    def _select_royal_pos(self, row, piece):
        searched_field = -1
        if piece.rank == 'queen':
            if piece.color == 'white':
                searched_field = WHITE_FIELD_VALUE
            else:
                searched_field = BLACK_FIELD_VALUE
        else:
            if piece.color == 'white':
                searched_field = BLACK_FIELD_VALUE
            else:
                searched_field = WHITE_FIELD_VALUE

        if self._board[row][ROYAL_POS[0]] == searched_field:
            return ROYAL_POS[0]
        else:
            return ROYAL_POS[1]

    
    def _check_initial_pos(self, row, columns):
        for i in columns:
            print('Check initial pos columns i -> ', i)
            if not isinstance(self._board[row][i].piece, ChessPiece):
                return i
        print('No empty position found among the supplied options for this piece... Exiting!')
        exit()


    def _verify_piece(self, piece):
        if not isinstance(piece, ChessPiece):
            print('A piece was provided that does not belong to the board... Exiting!')
            exit()


    # Updated build board method as a matrix of BoardSquare objects
    def _build_board(self):
        board = []
        current_color = 'black'
        for i in range(8):
            row = []
            board.append(row)
            for j in range(8):
                current_position = COLS[j] + str(ROWS[i])
                self._coordinates[str(i) + ':' + str(j)] = COLS[j] + str(ROWS[i])
                self._coordinates[COLS[j] + str(ROWS[i])] = str(i) + ':' + str(j)
                square = BoardSquare(position=current_position, color=current_color)
                board[i].append(square)
                if current_color == 'black':
                    current_color = 'white'
                else:
                    current_color = 'black'
            
            if current_color == 'black':
                current_color = 'white'
            else:
                current_color = 'black'
        
        self._board = board

    # Initial method to build board as a matrix of numbers representing colors
    # def _build_board(self):
    #     board = []
    #     current_field_val = WHITE_FIELD_VALUE
    #     for i in range(8):
    #         row = []
    #         board.append(row)
    #         for j in range(8):
    #             board[i].append(current_field_val)
    #             if current_field_val == 0:
    #                 current_field_val = 1
    #             else:
    #                 current_field_val = 0

    #         if current_field_val == 0:
    #             current_field_val = 1
    #         else:
    #             current_field_val = 0

    #     self._board = board


    def get_coordinates(self, value=None):
        if not value:
            return self._coordinates
        return self._coordinates[value]



if __name__=='__main__':
    print('Testing chess board class creation.')
    b = ChessBoard()
    b.status()
    print('Test finished.')
