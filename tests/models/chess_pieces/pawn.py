from board_components.chess_board import ChessBoard
from chess_pieces.pawn import Pawn
from chess_pieces.rook import Rook
from chess_pieces.knight import Knight
from chess_pieces.bishop import Bishop
from chess_pieces.queen import Queen
from chess_pieces.king import King


PAWN_POSITION_ROW = 4
PAWN_POSITION_COL = 4


def setup_test():
    board = ChessBoard()
    print('========Board Created========\n\n\n')

    # White pawn for the test
    white_pawn = Pawn(color='white', start_position='low')
    board.get_square(PAWN_POSITION_ROW, PAWN_POSITION_COL).piece = white_pawn
    
    # Black pieces for the test
    bishop_black = Bishop('black', 'high')
    knight_black = Knight('black', 'high')
    pawn_black = Pawn('black', 'high')
    queen_black = Queen('black', 'high')
    board.get_square(3, 4).piece = bishop_black
    board.get_square(5, 3).piece = knight_black
    board.get_square(5, 4).piece = queen_black
    board.get_square(5, 5).piece = pawn_black

    return board


def test_pawn_moves():
    board = setup_test()
    board.status()
    white_pawn = board.get_square(PAWN_POSITION_ROW, PAWN_POSITION_COL).piece
    current_position = f"{PAWN_POSITION_ROW}:{PAWN_POSITION_COL}"
    available_moves = white_pawn.check_available_moves(board, current_position)
    allowed_positions = []

    for i in range(8):
        for j in range(8):
            if f"{i}:{j}" in available_moves:
                allowed_positions.append((i, j))

    print('\n\n\nAllowed positions: \n', allowed_positions)
    for position in allowed_positions:
        board.set_square(position[0], position[1], 'A')

    print('\n\n\nAfter checking available moves:')
    board.status()


if __name__=='__main__':
    test_pawn_moves()
