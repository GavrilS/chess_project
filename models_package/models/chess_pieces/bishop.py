from chess_pieces.basic import ChessPiece


class Bishop(ChessPiece):

    def __init__(self, color='white'):
        super().__init__(rank='bishop', color=color)


    def move(self, board, position):
        pass


    def check_available_moves(self, board):
        pass


    def __str__(self):
        return f"{self.color[0]}{self.rank[0]}"


    def __repr__(self):
        return f"Bishop('{self.color})"




if __name__=='__main__':
    b = Bishop(color='black')
    print('b.rank: ', b.rank)
    print('b.color: ', b.color)
