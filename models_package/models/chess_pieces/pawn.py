from chess_pieces.basic import ChessPiece


class Pawn(ChessPiece):

    def __init__(self, color='white', initial_position='low'):
        super().__init__(rank='pawn', color=color)
        self._initial_position = initial_position


    def move(self, board, position):
        pass


    def check_available_moves(self, board, position):
        possible_moves = {}
        current_coordinates = position.split(':')
        row = current_coordinates[0]
        col = current_coordinates[1]
        if initial_position == 'low':
            pass


    def __str__(self):
        return f"{self.color[0]}{self.rank[0]}"


    def __repr__(self):
        return f"Pawn('{self.color})"


    @property
    def position(self):
        return self._initial_position




if __name__=='__main__':
    p = Pawn()
    print('p.rank: ', p.rank)
    print('p.color: ', p.color)
