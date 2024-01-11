from chess_pieces.basic import ChessPiece


class King(ChessPiece):

    def __init__(self, color='white', start_position='low'):
        super().__init__(rank='king', color=color, start_position=start_position)


    def check_available_moves(self, board, position):
        possible_moves = []
        row, col = self.get_coordinates(position)
        
        # Check above row
        if self.verify_board_row(row-1):
            if self.verify_board_col(col-1) and self.verify_board_piece(board.get_square(row-1, col-1).piece):
                possible_moves.append(str(row-1) + ':' + str(col-1))

            if self.verify_board_piece(board.get_square(row-1, col).piece):
                possible_moves.append(str(row-1) + ':' + str(col))

            if self.verify_board_col(col+1) and self.verify_board_piece(board.get_square(row-1, col+1).piece):
                possible_moves.append(str(row-1) + ':' + str(col+1))
        
        # Check below row
        if self.verify_board_row(row+1):
            if self.verify_board_col(col-1) and self.verify_board_piece(board.get_square(row+1, col-1).piece):
                possible_moves.append(str(row+1) + ':' + str(col-1))

            if self.verify_board_piece(board.get_square(row+1, col).piece):
                possible_moves.append(str(row+1) + ':' + str(col))

            if self.verify_board_col(col+1) and self.verify_board_piece(board.get_square(row+1, col+1).piece):
                possible_moves.append(str(row+1) + ':' + str(col+1))

        # Check current row position
        if self.verify_board_col(col-1) and self.verify_board_piece(board.get_square(row, col-1).piece):
            possible_moves.append(str(row) + ':' + str(col-1))
        
        if self.verify_board_col(col+1) and self.verify_board_piece(board.get_square(row, col+1).piece):
            possible_moves.append(str(row) + ':' + str(col+1))

        return possible_moves


    def test_for_check(self, board, position):
        in_check = False
        if self.king_check(board, position) or self.knight_check(board, position) or \
            self.bishop_queen_check(board, position) or self.rook_queen_check(board, position) or \
            self.pawn_check(board, position):
            in_check = True
        return in_check


    def king_check(self, board, position):
        in_check = False
        row, col = self.get_coordinates(position)

        # Check above positions for enemy king
        if self.verify_board_row(row-1):
            if self.verify_board_col(col-1) and self.verify_board_piece_for_check(board.get_square(row-1, col-1).piece, 'king'):
                return True
            
            if self.verify_board_piece_for_check(board.get_square(row-1, col).piece, 'king'):
                return True

            if self.verify_board_col(col+1) and self.verify_board_piece_for_check(board.get_square(row-1, col+1).piece, 'king'):
                return True

        # Check below positions for enemy king
        if self.verify_board_row(row+1):
            if self.verify_board_col(col-1) and self.verify_board_piece_for_check(board.get_square(row+1, col-1).piece, 'king'):
                return True
            
            if self.verify_board_piece_for_check(board.get_square(row+1, col).piece, 'king'):
                return True

            if self.verify_board_col(col+1) and self.verify_board_piece_for_check(board.get_square(row+1, col+1).piece, 'king'):
                return True

        # Check positions to the left and right for enemy king
        if self.verify_board_col(col-1) and self.verify_board_piece_for_check(board.get_square(row, col-1).piece, 'king'):
            return True
        
        if self.verify_board_col(col+1) and self.verify_board_piece_for_check(board.get_square(row, col+1).piece, 'king'):
            return True

        # No king was found in the neighbouring fields
        return in_check


    def knight_check(self, board, position):
        in_check = False
        row, col = self.get_coordinates(position)
        
        # Check above positions for knight check
        if self.verify_board_row(row+2):
            if self.verify_board_col(col-1) and self.verify_board_piece_for_check(board.get_square(row+2, col-1).piece, 'knight'):
                return True

            if self.verify_board_col(col+1) and self.verify_board_piece_for_check(board.get_square(row+2, col+1).piece, 'knight'):
                return True

        # Check below positions for knight check
        if self.verify_board_row(row-2):
            if self.verify_board_col(col-1) and self.verify_board_piece_for_check(board.get_square(row-2, col-1).piece, 'knight'):
                return True

            if self.verify_board_col(col+1) and self.verify_board_piece_for_check(board.get_square(row-2, col+1).piece, 'knight'):
                return True

        # Check positions to the left for knight check
        if self.verify_board_col(col-2):
            if self.verify_board_row(row-1) and self.verify_board_piece_for_check(board.get_square(row-1, col-2).piece, 'knight'):
                return True

            if self.verify_board_row(row+1) and self.verify_board_piece_for_check(board.get_square(row+1, col-2).piece, 'knight'):
                return True

        # Check positions to the right for knight check
        if self.verify_board_row(col+2):
            if self.verify_board_row(row-1) and self.verify_board_piece_for_check(board.get_square(row-1, col+2).piece, 'knight'):
                return True

            if self.verify_board_row(row+1) and self.verify_board_piece_for_check(board.get_square(row+1, col+2).piece, 'knight'):
                return True

        return in_check


    def bishop_queen_check(self, board, position):
        in_check = False
        row, col = self.get_coordinates(position)
        flag = True
        current_row = row
        current_col = col

        # Move up left diagonal to test for bishop check
        while flag:
            if self.verify_board_row(current_row-1) and self.verify_board_col(current_col-1):
                piece = board.get_square(current_row-1, current_col-1).piece
                if self.verify_board_piece_for_check(piece, 'bishop') or self.verify_board_piece_for_check(piece, 'queen'):
                    in_check = True
                    return in_check
                elif piece:
                    flag = False
                else:
                    current_row-=1
                    current_col-=1
            else:
                break

        current_row = row
        current_col = col
        flag = True
        # Move up right diagonal to test for bishop check
        while flag:
            if self.verify_board_row(current_row-1) and self.verify_board_col(current_col+1):
                piece = board.get_square(current_row-1, current_col+1).piece
                if self.verify_board_piece_for_check(piece, 'bishop') or self.verify_board_piece_for_check(piece, 'queen'):
                    in_check = True
                    return in_check
                elif piece:
                    flag = False
                else:
                    current_row-=1
                    current_col+=1
            else:
                break

        current_row = row
        current_col = col
        flag = True
        # Move down left diagonal to test for bishop check
        while flag:
            if self.verify_board_row(current_row+1) and self.verify_board_col(current_col-1):
                piece = board.get_square(current_row+1, current_col-1).piece
                if self.verify_board_piece_for_check(piece, 'bishop') or self.verify_board_piece_for_check(piece, 'queen'):
                    in_check = True
                    return in_check
                elif piece:
                    flag = False
                else:
                    current_row+=1
                    current_col-=1
            else:
                break

        current_row = row
        current_col = col
        flag = True
        # Move down right diagonal to test for bishop check
        while flag:
            if self.verify_board_row(current_row+1) and self.verify_board_col(current_col+1):
                piece = board.get_square(current_row+1, current_col+1).piece
                if self.verify_board_piece_for_check(piece, 'bishop') or self.verify_board_piece_for_check(piece, 'queen'):
                    in_check = True
                    return in_check
                elif piece:
                    flag = False
                else:
                    current_row+=1
                    current_col+=1
            else:
                break

        return in_check


    def rook_queen_check(self, board, position):
        in_check = False
        row, col = self.get_coordinates(position)
        flag = True
        current_row = row
        current_col = col

        # Move up from the current field
        while flag:
            if self.verify_board_row(current_row-1):
                piece = board.get_square(current_row-1, current_col).piece
                if self.verify_board_piece_for_check(piece, 'rook') or self.verify_board_piece_for_check(piece, 'queen'):
                    in_check = True
                    return in_check
                elif piece:
                    flag = False
                else:
                    current_row -= 1
            else:
                break

        flag = True
        current_row = row
        # Move down from the current position
        while flag:
            if self.verify_board_row(current_row+1):
                piece = board.get_square(current_row+1, current_col).piece
                if self.verify_board_piece_for_check(piece, 'rook') or self.verify_board_piece_for_check(piece, 'queen'):
                    in_check = True
                    return in_check
                elif piece:
                    flag = False
                else:
                    current_row += 1
            else:
                break

        flag = True
        current_row = row
        # Move to the left from the current position
        while flag:
            if self.verify_board_col(current_col-1):
                piece = board.get_square(current_row, current_col-1).piece
                if self.verify_board_piece_for_check(piece, 'rook') or self.verify_board_piece_for_check(piece, 'queen'):
                    in_check = True
                    return in_check
                elif piece:
                    flag = False
                else:
                    current_col -= 1
            else:
                break

        flag = True
        current_col = col
        # Move to the right from the current position
        while flag:
            if self.verify_board_col(current_col+1):
                piece = board.get_square(current_row, current_col+1).piece
                if self.verify_board_piece_for_check(piece, 'rook') or self.verify_board_piece_for_check(piece, 'queen'):
                    in_check = True
                    return in_check
                elif piece:
                    flag = False
                else:
                    current_col += 1
            else:
                break

        return in_check

    
    def pawn_check(self, board, position):
        in_check = False
        row, col = self.get_coordinates(position)
        if self.start_position == 'low':
            if self.verify_board_row(row+1) and self.verify_board_col(col-1):
                field_piece = board.get_square(row+1, col-1).piece
                if self.verify_board_piece_for_check(field_piece) and field_piece.rank == 'pawn':
                    in_check = True
                    return in_check

            if self.verify_board_row(row+1) and self.verify_board_col(col+1):
                field_piece = board.get_square(row+1, col+1).piece
                if self.verify_board_piece_for_check(field_piece, 'pawn'):
                    in_check = True

        else:
            if self.verify_board_row(row-1) and self.verify_board_col(col-1):
                field_piece = board.get_square(row-1, col-1).piece
                if self.verify_board_piece_for_check(field_piece, 'pawn'):
                    in_check = True
                    return in_check
            
            if self.verify_board_row(row-1) and self.verify_board_col(col+1):
                field_piece = board.get_square(row-1, col+1).piece
                if self.verify_board_piece_for_check(field_piece, 'pawn'):
                    in_check = True

        return in_check


    def verify_board_piece_for_check(self, piece, rank):
        if not piece or piece.color == self.color:
            return False
        return piece.rank == rank


    def __str__(self):
        return f"{self.color[0]}{self.rank[0]}"


    def __repr__(self):
        return f"King('{self.color})"




if __name__=='__main__':
    k = King(color='black')
    print('k.rank: ', k.rank)
    print('k.color: ', k.color)
