from basic import ChessPiece


class Pawn(ChessPiece):

    def __init__(self, color='white'):
        super().__init__(rank='pawn', color=color)


    def move(self, board, position):
        pass


    def check_available_moves(self, board):
        pass




if __name__=='__main__':
    p = Pawn()
    print('p.rank: ', p.rank)
    print('p.color: ', p.color)
