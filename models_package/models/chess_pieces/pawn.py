from chess_pieces.basic import ChessPiece


class Pawn(ChessPiece):

    def __init__(self, color='white'):
        super().__init__(rank='pawn', color=color)


    def move(self, board, position):
        pass


    def check_available_moves(self, board):
        pass


    def __str__(self):
        return f"{self.color[0]}{self.rank[0]}"


    def __repr__(self):
        return f"Pawn('{self.color})"




if __name__=='__main__':
    p = Pawn()
    print('p.rank: ', p.rank)
    print('p.color: ', p.color)
