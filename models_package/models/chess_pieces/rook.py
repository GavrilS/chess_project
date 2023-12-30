from chess_pieces.basic import ChessPiece

END_ROW = 7
START_ROW = 0
START_COL = 0
END_COL = 7


class Rook(ChessPiece):

    def __init__(self, color='white'):
        super().__init__(rank='rook', color=color)


    def move(self, board, position, next_position):
        possible_moves = self.check_available_moves(board, position)
        if next_position in possible_moves:
            return True
        else:
            return False


    def check_available_moves(self, board, position):
        possible_moves = []
        current_coordinates = position.spli(':')
        int(row) = current_coordinates[0]
        int(col) = current_coordinates[1]
        flag = True
        current_row = row
        current_col = col

        # Move up the field from current position
        while flag:
            flag = False
            if current_row-1 >= START_ROW and current_row-1 <= END_ROW:
                if not board[current_row-1][current_col].piece or board[current_row-1][current_col].piece.color != self.color:
                    possible_moves.append(str(current_row-1) + ':' + str(current_col))
                    current_row -= 1
                    flag = True

        current_row = row
        flag = True
        # Move down the field from current position
        while flag:
            flag = False
            if current_row+1 >= START_ROW and current_row+1 <= END_ROW:
                if not board[current_row+1][current_col].piece or board[current_row+1][current_col].piece.color != self.color:
                    possible_moves.append(str(current_row+1) + ':' + str(current_col))
                    current_row += 1
                    flag = True
        
        current_row = row
        flag = True
        # Move to the left from current position
        while flag:
            flag = False
            if current_col-1 >= START_COL and current_col-1 <= END_COL:
                if not board[current_row][current_col-1].piece or board[current_row][current_col-1].piece.color != self.color:
                    possible_moves.append(str(current_row) + ':' + str(current_col-1))
                    current_col -= 1
                    flag = True

        current_col = col
        flag = True
        # Move to the right from current position
        while flag:
            flag = False
            if current_col+1 >= START_COL and current_col+1 <= END_COL:
                if not board[current_row][current_col+1].piece or board[current_row][current_col+1].piece.color != self.color:
                    possible_moves.append(str(current_row) + ':' + str(current_col+1))
                    current_col += 1
                    flag = True

        return possible_moves


    def __str__(self):
        return f"{self.color[0]}{self.rank[0]}"


    def __repr__(self):
        return f"Rook('{self.color})"




if __name__=='__main__':
    r = Rook(color='black')
    print('r.rank: ', r.rank)
    print('r.color: ', r.color)
