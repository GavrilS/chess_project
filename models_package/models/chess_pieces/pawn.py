from chess_pieces.basic import ChessPiece


class Pawn(ChessPiece):

    def __init__(self, color='white', start_position='low'):
        super().__init__(rank='pawn', color=color, start_position=start_position)


    def check_available_moves(self, board, position):
        possible_moves = []
        row, col = self.get_coordinates(position)
        if self.start_position == 'low':
            # if row + 1 > FINAL_LOW_ROW and row + 1 <= FINAL_HIGH_ROW:
            if self.verify_board_row(row+1):
                # if col - 1 >= START_COL and col - 1 < END_COL:
                if self.verify_board_col(col-1):
                    if self.verify_board_piece(board.get_square(row+1, col-1).piece):
                        possible_moves.append(str(row+1) + ':' + str(col-1))

                if not board.get_square(row+1,col).piece:
                    possible_moves.append(str(row+1) + ':' + str(col))

                # if col + 1 > START_COL and col + 1 <= END_COL:
                if self.verify_board_col(col+1):
                    if self.verify_board_piece(board.get_square(row+1,col+1).piece):
                        possible_moves.append(str(row+1) + ':' + str(col+1))
        else:
            # if row - 1 >= FINAL_LOW_ROW and row - 1 < FINAL_HIGH_ROW:
            if self.verify_board_row(row-1):
                # if col - 1 >= START_COL and col - 1 < END_COL:
                if self.verify_board_col(col-1):
                    if self.verify_board_piece(board.get_square(row-1,col-1).piece):
                        possible_moves.append(str(row-1) + ':' + str(col-1))
                
                if not board.get_square(row-1,col).piece:
                    possible_moves.append(str(row-1) + ':' + str(col))

                # if col + 1 > START_COL and col + 1 <= END_COL:
                if self.verify_board_col(col+1):
                    if self.verify_board_piece(board.get_square(row+1,col+1).piece):
                        possible_moves.append(str(row+1) + ':' + str(col+1))

        return possible_moves


    def __str__(self):
        return f"{self.color[0]}{self.rank[0]}"


    def __repr__(self):
        return f"Pawn('{self.color})"



if __name__=='__main__':
    p = Pawn()
    print('p.rank: ', p.rank)
    print('p.color: ', p.color)
