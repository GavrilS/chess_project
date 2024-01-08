from board_components.chess_board import ChessBoard
from chess_pieces.pawn import Pawn
from chess_pieces.rook import Rook
from chess_pieces.knight import Knight
from chess_pieces.bishop import Bishop
from chess_pieces.queen import Queen
from chess_pieces.king import King



def main():
    black_set = create_chess_set(set_color='black')
    white_set = create_chess_set(set_color='white', start_position='high')
    board = ChessBoard()
    print('*'*40)
    board.populate_board(black_set, white_set)
    # board.populate_board(white_set, black_set)
    board.status()
    print('*'*40)
    print('current board coordinates: ', board.get_coordinates())


def create_chess_set(set_color='white', start_position='low'):
    chess_set = []
    for i in range(8):
        chess_set.append(Pawn(color=set_color, start_position=start_position))

    for i in range(2):
        chess_set.append(Rook(color=set_color, start_position=start_position))
        chess_set.append(Bishop(color=set_color, start_position=start_position))
        chess_set.append(Knight(color=set_color, start_position=start_position))
    
    chess_set.append(Queen(color=set_color, start_position=start_position))
    chess_set.append(King(color=set_color, start_position=start_position))

    return chess_set



if __name__=='__main__':
    main()
