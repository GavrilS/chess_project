from chess_pieces.basic import ChessPiece


class Bishop(ChessPiece):

    def __init__(self, color='white'):
        super().__init__(rank='bishop', color=color)


    def move(self, board, position):
        pass


    def check_available_moves(self, board):
        pass




if __name__=='__main__':
    b = Bishop(color='black')
    print('b.rank: ', b.rank)
    print('b.color: ', b.color)
