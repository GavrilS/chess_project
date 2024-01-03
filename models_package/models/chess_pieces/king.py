from chess_pieces.basic import ChessPiece


class King(ChessPiece):

    def __init__(self, color='white', start_position='low'):
        super().__init__(rank='king', color=color, start_position=start_position)


    def check_available_moves(self, board, position):
        possible_moves = []
        row, col = self.get_coordinates(position)
        
        # Check above row
        if self.verify_board_row(row-1):
            if self.verify_board_col(col-1) and self.verify_board_piece(board[row-1][col-1].piece):
                possible_moves.append(str(row-1) + ':' + str(col-1))

            if self.verify_board_piece(board[row-1][col].piece):
                possible_moves.append(str(row-1) + ':' + str(col))

            if self.verify_board_col(col+1) and self.verify_board_piece(board[row-1][col+1].piece):
                possible_moves.append(str(row-1) + ':' + str(col+1))
        
        # Check below row
        if self.verify_board_row(row+1):
            if self.verify_board_col(col-1) and self.verify_board_piece(board[row+1][col-1].piece):
                possible_moves.append(str(row+1) + ':' + str(col-1))

            if self.verify_board_piece(board[row+1][col].piece):
                possible_moves.append(str(row+1) + ':' + str(col))

            if self.verify_board_col(col+1) and self.verify_board_piece(board[row+1][col+1].piece):
                possible_moves.append(str(row+1) + ':' + str(col+1))

        # Check current row position
        if self.verify_board_col(col-1) and self.verify_board_piece(board[row][col-1].piece):
            possible_moves.append(str(row) + ':' + str(col-1))
        
        if self.verify_board_col(col+1) and self.verify_board_piece(board[row][col+1].piece):
            possible_moves.append(str(row) + ':' + str(col+1))

        return possible_moves


    def test_for_check(self, board, position):
        pass

    
    def pawn_check(self, board, position):
        in_check = False
        row, col = self.get_coordinates(position)
        if self.start_position == 'low':
            if self.verify_board_row(row+1) and self.verify_board_col(col-1):
                field_piece = board[row+1][col-1].piece
                if self.verify_board_piece(field_piece) and field_piece.rank == 'pawn':
                    in_check = True
                    return in_check

            if self.verify_board_row(row+1) and self.verify_board_col(col+1):
                field_piece = board[row+1][col+1]:
                if self.verify_board_piece(field_piece) and field_piece.rank == 'pawn':
                    in_check = True

        else:
            if self.verify_board_row(row-1) and self.verify_board_col(col-1):
                field_piece = board[row-1][col-1].piece
                if self.verify_board_piece(field_piece) and field_piece.rank == 'pawn':
                    in_check = True
                    return in_check
            
            if self.verify_board_row(row-1) and self.verify_board_col(col+1):
                field_piece = board[row-1][col+1].piece
                if self.verify_board_piece(field_piece) and field_piece.rank == 'pawn':
                    in_check = True

        return in_check


    def __str__(self):
        return f"{self.color[0]}{self.rank[0]}"


    def __repr__(self):
        return f"King('{self.color})"




if __name__=='__main__':
    k = King(color='black')
    print('k.rank: ', k.rank)
    print('k.color: ', k.color)
