from chess_pieces.basic import ChessPiece


class Bishop(ChessPiece):

    def __init__(self, color='white', start_position='low'):
        super().__init__(rank='bishop', color=color, start_position=start_position)


    def check_available_moves(self, board, position):
        possible_moves = []
        row, col = self.get_coordinates(position)
        current_row = row
        current_col = col
        flag = True
        # Move up left diagonal
        while flag:
            flag = False
            # if current_row-1 >= START_ROW and current_row-1 <= END_ROW and current_col-1 >= START_COL and current_col-1 <= END_COL:
            if self.verify_board_row(row=current_row-1) and self.verify_board_col(col=current_col-1):
                if self.verify_board_piece(board.get_square(current_row-1,current_col-1).piece):
                    possible_moves.append(str(current_row-1) + ':' + str(current_col-1))
                    if not board.get_square(current_row-1,current_col-1).piece:
                        current_row -= 1
                        current_col -= 1
                        flag = True
        
        current_row = row
        current_col = col
        flag = True
        # Move up right diagonal
        while flag:
            flag = False
            # if current_row-1 >= START_ROW and current_row-1 <= END_ROW and current_col+1 >= START_COL and current_col+1 <= END_COL:
            if self.verify_board_row(row=current_row-1) and self.verify_board_col(col=current_col+1):
                if self.verify_board_piece(board.get_square(current_row-1,current_col+1).piece):
                    possible_moves.append(str(current_row-1) + ':' + str(current_col+1))
                    if not board.get_square(current_row-1,current_col+1).piece:
                        current_row -= 1
                        current_col += 1
                        flag = True

        current_row = row
        current_col = col
        flag = True
        # Move down left diagonal
        while flag:
            flag = False
            # if current_row+1 >= START_ROW and current_row+1 <= END_ROW and current_col-1 >= START_COL and current_col-1 <= END_COL:
            if self.verify_board_row(current_row+1) and self.verify_board_col(current_col-1):
                if self.verify_board_piece(board.get_square(current_row+1,current_col-1).piece):
                    possible_moves.append(str(current_row+1) + ':' + str(current_col-1))
                    if not board.get_square(current_row+1,current_col-1).piece:
                        current_row += 1
                        current_col -= 1
                        flag = True

        current_row = row
        current_col = col
        flag = True
        # Move down right diagonal
        while flag:
            flag = False
            # if current_row+1 >= START_ROW and current_row+1 <= END_ROW and current_col+1 >= START_COL and current_col-1 <= END_COL:
            if self.verify_board_row(current_row+1) and self.verify_board_col(current_col+1):
                if self.verify_board_piece(board.get_square(current_row+1,current_col+1).piece):
                    possible_moves.append(str(current_row+1) + ':' + str(current_col+1))
                    if not board.get_square(current_row+1,current_col+1).piece:
                        current_row += 1
                        current_col += 1
                        flag = True

        return possible_moves


    def __str__(self):
        return f"{self.color[0]}{self.rank[0]}"


    def __repr__(self):
        return f"Bishop('{self.color})"




if __name__=='__main__':
    b = Bishop(color='black')
    print('b.rank: ', b.rank)
    print('b.color: ', b.color)
