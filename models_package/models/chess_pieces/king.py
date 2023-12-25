from chess_pieces.basic import ChessPiece


class King(ChessPiece):

    def __init__(self, color='white'):
        super().__init__(rank='king', color=color)


    def move(self, board, position):
        pass


    def check_available_moves(self, board):
        pass


    def __str__(self):
        return f"{self.color[0]}{self.rank[0]}"


    def __repr__(self):
        return f"King('{self.color})"




if __name__=='__main__':
    k = King(color='black')
    print('k.rank: ', k.rank)
    print('k.color: ', k.color)
