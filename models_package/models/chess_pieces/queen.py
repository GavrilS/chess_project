from chess_pieces.basic import ChessPiece


class Queen(ChessPiece):

    def __init__(self, color='white'):
        super().__init__(rank='queen', color=color)


    def move(self, board, position):
        pass


    def check_available_moves(self, board):
        pass




if __name__=='__main__':
    q = Queen()
    print('q.rank: ', q.rank)
    print('q.color: ', q.color)
