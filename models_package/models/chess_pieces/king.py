from chess_pieces.basic import ChessPiece


class King(ChessPiece):

    def __init__(self, color='white'):
        super().__init__(rank='king', color=color)


    def move(self, board, position):
        pass


    def check_available_moves(self, board):
        pass




if __name__=='__main__':
    k = King(color='black')
    print('k.rank: ', k.rank)
    print('k.color: ', k.color)
