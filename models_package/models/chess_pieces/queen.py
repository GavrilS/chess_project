from chess_pieces.basic import ChessPiece


class Queen(ChessPiece):

    def __init__(self, color='white'):
        super().__init__(rank='queen', color=color)


    def move(self, board, position):
        pass


    def check_available_moves(self, board):
        pass


    def __str__(self):
        return f"{self.color[0]}{self.rank[0]}"


    def __repr__(self):
        return f"Queen('{self.color})"



if __name__=='__main__':
    q = Queen()
    print('q.rank: ', q.rank)
    print('q.color: ', q.color)
