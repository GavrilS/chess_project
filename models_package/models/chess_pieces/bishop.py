from chess_pieces.basic import ChessPiece

END_ROW = 7
START_ROW = 0
START_COL = 0
END_COL = 7


class Bishop(ChessPiece):

    def __init__(self, color='white'):
        super().__init__(rank='bishop', color=color)


    def move(self, board, position, next_position):
        pass


    def check_available_moves(self, board, position):
        possible_moves = []
        current_coordinates = position.split(':')
        int(row) = current_coordinates[0]
        int(col) = current_coordinates[1]
        current_row = row
        current_col = col
        flag = True
        # Move up left diagonal
        while flag:
            flag = False
            if current_row-1 >= START_ROW and current_row-1 <= END_ROW and current_col-1 >= START_COL and current_col-1 <= END_COL:
                if not board[row-1][col-1].piece or board[row-1][col-1].piece.color != self.color:
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
            if current_row-1 >= START_ROW and current_row-1 <= END_ROW and current_col+1 >= START_COL and current_col+1 <= END_COL:
                if not board[row-1][col+1].piece or board[row-1][col+1].piece.color != self.color:
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


    def __str__(self):
        return f"{self.color[0]}{self.rank[0]}"


    def __repr__(self):
        return f"Bishop('{self.color})"




if __name__=='__main__':
    b = Bishop(color='black')
    print('b.rank: ', b.rank)
    print('b.color: ', b.color)
