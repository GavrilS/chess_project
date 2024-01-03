from chess_pieces.basic import ChessPiece


class Queen(ChessPiece):

    def __init__(self, color='white', start_position='low'):
        super().__init__(rank='queen', color=color, start_position=start_position)


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
                # if not board[current_row-1][current_col-1].piece or board[current_row-1][current_col-1].piece.color != self.color:
                if self.verify_board_piece(board[current_row-1][current_col-1].piece):
                    possible_moves.append(str(current_row-1) + ':' + str(current_col-1))
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
                # if not board[current_row-1][current_col+1].piece or board[current_row-1][current_col+1].piece.color != self.color:
                if self.verify_board_piece(board[current_row-1][current_col+1].piece):
                    possible_moves.append(str(current_row-1) + ':' + str(current_col+1))
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
                # if not board[current_row+1][current_col-1].piece or board[current_row+1][current_col-1].piece.color != self.color:
                if self.verify_board_piece(board[current_row+1][current_col-1].piece):
                    possible_moves.append(str(current_row+1) + ':' + str(current_col-1))
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
                # if not board[current_row+1][current_col+1].piece or board[current_row+1][current_col+1].piece.color != self.color:
                if self.verify_board_piece(board[current_row+1][current_col+1].piece):
                    possible_moves.append(str(current_row+1) + ':' + str(current_col+1))
                    current_row += 1
                    current_col += 1
                    flag = True

        current_row = row
        current_col = col
        flag = True
        # Move up the field from current position
        while flag:
            flag = False
            # if current_row-1 >= START_ROW and current_row-1 <= END_ROW:
            if self.verify_board_row(row=current_row-1):
                # if not board[current_row-1][current_col].piece or board[current_row-1][current_col].piece.color != self.color:
                if self.verify_board_piece(piece=board[current_row-1][current_col].piece):
                    possible_moves.append(str(current_row-1) + ':' + str(current_col))
                    current_row -= 1
                    flag = True

        current_row = row
        flag = True
        # Move down the field from current position
        while flag:
            flag = False
            # if current_row+1 >= START_ROW and current_row+1 <= END_ROW:
            if self.verify_board_row(row=current_row+1):
                # if not board[current_row+1][current_col].piece or board[current_row+1][current_col].piece.color != self.color:
                if self.verify_board_piece(piece=board[current_row+1][current_col].piece):
                    possible_moves.append(str(current_row+1) + ':' + str(current_col))
                    current_row += 1
                    flag = True
        
        current_row = row
        flag = True
        # Move to the left from current position
        while flag:
            flag = False
            # if current_col-1 >= START_COL and current_col-1 <= END_COL:
            if self.verify_board_col(col=current_col-1):
                # if not board[current_row][current_col-1].piece or board[current_row][current_col-1].piece.color != self.color:
                if self.verify_board_piece(piece=board[current_row][current_col-1].piece):
                    possible_moves.append(str(current_row) + ':' + str(current_col-1))
                    current_col -= 1
                    flag = True

        current_col = col
        flag = True
        # Move to the right from current position
        while flag:
            flag = False
            # if current_col+1 >= START_COL and current_col+1 <= END_COL:
            if self.verify_board_col(col=current_col+1):
                # if not board[current_row][current_col+1].piece or board[current_row][current_col+1].piece.color != self.color:
                if self.verify_board_piece(piece=board[current_row][current_col+1].piece):
                    possible_moves.append(str(current_row) + ':' + str(current_col+1))
                    current_col += 1
                    flag = True

        return possible_moves


    def __str__(self):
        return f"{self.color[0]}{self.rank[0]}"


    def __repr__(self):
        return f"Queen('{self.color})"



if __name__=='__main__':
    q = Queen()
    print('q.rank: ', q.rank)
    print('q.color: ', q.color)
