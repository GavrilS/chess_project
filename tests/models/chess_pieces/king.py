from board_components.chess_board import ChessBoard
from chess_pieces.pawn import Pawn
from chess_pieces.rook import Rook
from chess_pieces.knight import Knight
from chess_pieces.bishop import Bishop
from chess_pieces.queen import Queen
from chess_pieces.king import King


def setup_test():
    chess_set_white = []
    chess_set_black = []

    king_white = King(color='white', start_position='low')
    chess_set_white.append(king_white)
    bishop_black = Bishop('black', 'high')
    chess_set_black.append(bishop_black)

    return chess_set_white, chess_set_black


def main():
    white_set, black_set = setup_test()
    board = ChessBoard()
    board.populate_board(white_set, black_set)
    print('*'*40)
    board.status()



if __name__=='__main__':
    main()
