from chess_board import ChessBoard
from chess_pieces.pawn import Pawn
from chess_pieces.rook import Rook
from chess_pieces.knight import Knight
from chess_pieces.bishop import Bishop
from chess_pieces.queen import Queen
from chess_pieces.king import King



def main():
    black_set = create_chess_set(set_color='black')
    white_set = create_chess_set(set_color='white')
    board = ChessBoard()
    board.populate_board(black_set, white_set)
    # board.populate_board(white_set, black_set)
    board.status()


def create_chess_set(set_color='white'):
    chess_set = []
    for i in range(8):
        chess_set.append(Pawn(color=set_color))

    for i in range(2):
        chess_set.append(Rook(color=set_color))
        chess_set.append(Bishop(color=set_color))
        chess_set.append(Knight(color=set_color))
    
    chess_set.append(Queen(color=set_color))
    chess_set.append(King(color=set_color))

    return chess_set



if __name__=='__main__':
    main()
