from chess_pieces.basic import ChessPiece


class Knight(ChessPiece):

    def __init__(self, color='white'):
        super().__init__(rank='knight', color=color)


    def move(self, board, position):
        pass


    def check_available_moves(self, board):
        pass


    def __str__(self):
        return f"{self.color[0]}{self.rank[0]}"


    def __repr__(self):
        return f"Knight('{self.color})"




if __name__=='__main__':
    k = Knight()
    print('k.rank: ', k.rank)
    print('k.color: ', k.color)
