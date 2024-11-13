#render a welcome message
#get_move
#render players turn
#error message for: to enter valid move,
#lower or uppercase accepted
#not too moves in the same cell
#updated board after turn
#render winner



#create game class and init properties

class Game():
    def __init__(self, turn, tie, winner, board):
        self.turn = 'X', 'O'
        self.tie = False
        self.winner = None
        self.board = {
  'a1': None, 'b1': None, 'c1': None,
  'a2': None, 'b2': None, 'c2': None,
  'a3': None, 'b3': None, 'c3': None,
}

