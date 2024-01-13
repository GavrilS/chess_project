from chess_pieces.basic import ChessPiece


class Knight(ChessPiece):

    def __init__(self, color='white', start_position='low'):
        super().__init__(rank='knight', color=color, start_position=start_position)


    def check_available_moves(self, board, position):
        possible_moves = []
        row, col = self.get_coordinates(position)

        # Check above positions - row + 2
        if self.verify_board_row(row+2):
            if self.verify_board_col(col-1) and self.verify_board_piece(board.get_square(row+2,col-1).piece):
                possible_moves.append(str(row+2) + ':' + str(col-1))

            if self.verify_board_col(col+1) and self.verify_board_piece(board.get_square(row+2,col+1).piece):
                possible_moves.append(str(row+2) + ':' + str(col+1))

        # Check below positions - row - 2
        if self.verify_board_row(row-2):
            if self.verify_board_col(col-1) and self.verify_board_piece(board.get_square(row-2,col-1).piece):
                possible_moves.append(str(row-2) + ':' + str(col-1))

            if self.verify_board_col(col+1) and self.verify_board_piece(board.get_square(row-2,col+1).piece):
                possible_moves.append(str(row-2) + ':' + str(col+1))

        # Check positions to the left - col - 2
        if self.verify_board_col(col-2):
            if self.verify_board_row(row-1) and self.verify_board_piece(board.get_square(row-1,col-2).piece):
                possible_moves.append(str(row-1) + ':' + str(col-2))

            if self.verify_board_row(row+1) and self.verify_board_piece(board.get_square(row+1,col-2).piece):
                possible_moves.append(str(row+1) + ':' + str(col-2))

        # Check positions to the right - col + 2
        if self.verify_board_col(col+2):
            if self.verify_board_row(row-1) and self.verify_board_piece(board.get_square(row-1,col+2).piece):
                possible_moves.append(str(row-1) + ':' + str(col+2))

            if self.verify_board_row(row+1) and self.verify_board_piece(board.get_square(row+1,col+2).piece):
                possible_moves.append(str(row+1) + ':' + str(col+2))

        return possible_moves


    def __str__(self):
        return f"{self.color[0]}{self.rank[:2]}"


    def __repr__(self):
        return f"Knight('{self.color})"




if __name__=='__main__':
    k = Knight()
    print('k.rank: ', k.rank)
    print('k.color: ', k.color)
