from board_components.chess_board import ChessBoard
from chess_pieces.pawn import Pawn
from chess_pieces.rook import Rook
from chess_pieces.knight import Knight
from chess_pieces.bishop import Bishop
from chess_pieces.queen import Queen
from chess_pieces.king import King


KING_POSITION_ROW = 4
KING_POSITION_COL = 4


def setup_test():
    board = ChessBoard()
    print('========Board Created========\n\n\n')

    # White king for the test
    king_white = King(color='white', start_position='low')
    white_pawn = Pawn(color='white', start_position='low')
    board.get_square(KING_POSITION_ROW, KING_POSITION_COL).piece = king_white
    board.get_square(3, 5).piece = white_pawn
    
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


def test_king_moves():
    board = setup_test()
    board.status()
    wking = board.get_square(KING_POSITION_ROW, KING_POSITION_COL).piece
    current_position = f"{KING_POSITION_ROW}:{KING_POSITION_COL}"
    available_moves = wking.check_available_moves(board, current_position)

    for i in range(8):
        for j in range(8):
            if f"{i}:{j}" in available_moves:
                board.set_square(i, j, 'A')

    print('\n\n\nAfter checking available moves:')
    board.status()


if __name__=='__main__':
    test_king_moves()
