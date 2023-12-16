from basic import ChessPiece


class Knight(ChessPiece):

    def __init__(self, color='white'):
        super().__init__(rank='knight', color=color)


    def move(self, board, position):
        pass


    def check_available_moves(self, board):
        pass




if __name__=='__main__':
    k = Knight()
    print('k.rank: ', k.rank)
    print('k.color: ', k.color)
