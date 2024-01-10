from board_components.chess_board import ChessBoard
from chess_pieces.pawn import Pawn
from chess_pieces.rook import Rook
from chess_pieces.knight import Knight
from chess_pieces.bishop import Bishop
from chess_pieces.queen import Queen
from chess_pieces.king import King


def setup_test():
    board = ChessBoard()
    print('========Board Created========')

    # White king for the test
    king_white = King(color='white', start_position='low')
    board.get_square(4, 4).piece = king_white
    
    # Black pieces for the test
    bishop_black = Bishop('black', 'high')
    knight_black = Knight('black', 'high')
    pawn_black = Pawn('black', 'high')
    queen_black = Queen('black', 'high')
    board.get_square(3, 4).piece = bishop_black
    board.get_square(3, 3).piece = knight_black
    board.get_square(2, 4).piece = queen_black
    board.get_square(5, 3).piece = pawn_black

    return board


def main():
    board = setup_test()
    board.status()



if __name__=='__main__':
    main()
