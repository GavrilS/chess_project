from chess_pieces.basic import ChessPiece


class Rook(ChessPiece):

    def __init__(self, color='white'):
        super().__init__(rank='rook', color=color)


    def move(self, board, position):
        pass


    def check_available_moves(self, board):
        pass


    def __str__(self):
        return f"{self.color[0]}{self.rank[0]}"


    def __repr__(self):
        return f"Rook('{self.color})"




if __name__=='__main__':
    r = Rook(color='black')
    print('r.rank: ', r.rank)
    print('r.color: ', r.color)
