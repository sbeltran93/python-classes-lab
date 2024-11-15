#game inital properties -done
#make board -done
#input for turn -done
# turns 'x' 'o'
#switch turns -done did in loop
#render the board -done
#make a starting turn
#lowercase input -done
#winning combos -done
#winner -done
#tie?
# message for player turn, invalid input, winner, tie

#create game class and init properties

class Game(): #step1, step8
    def __init__(self):
        self.turn = 'X'
        self.tie = False
        self.winner = None
        self.board = {
        'a1': None, 'b1': None, 'c1': None,
        'a2': None, 'b2': None, 'c2': None,
        'a3': None, 'b3': None, 'c3': None,
        }
        
   #welcome message #step2
    def play_game(self):
        print('Welcome players!')
        print('Player 1 is "X" and player 2 is "O".')

        while self.winner is None and self.tie is False:
            self.render()
            self.get_move()
            self.check_winner()
            self.check_for_tie()
            if self.winner or self.tie:
                self.print_message()
                break
            self.switch_turn()

    #gameboard #step 3
    def print_board(self):
        b = self.board
        print(f"""
                A   B   C
            1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
                ----------
            2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
                ----------
            3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """)

    def print_message(self):
        if self.tie:
            print('Tie game! Try again?')
        elif self.winner:
            print(f"{self.winner} wins!")
        else: print(f"Its player {self.turn}'s turn!")    

 #input of player #loop alternating between players. #invalid input msg
    def get_move(self): #step 4
        while True:
            move = input(f"Enter your move player {self.turn},: ").lower()
            if move in self.board and self.board[move] == None:
    #players turn
                self.board[move] = self.turn
                break
            else:
                 print('Invalid move. Please pick a open space.')
                 continue

    #winning combinations #step 5 #might need to fix something #directions say for loop, will look up
    def check_winner(self):
        winning_combinations = [
            ['a1', 'a2', 'a3'],
            ['b1', 'b2', 'b3'],
            ['c1', 'c2', 'c3'],
            ['a1', 'b2', 'c3'],
            ['a3', 'b2', 'c1'],
            ['a1', 'b1', 'c1'],
            ['a2', 'b2', 'c2'],
            ['a3', 'b3', 'c3'],
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] and self.board[combo[0]] is not None:
                self.winner = self.board[combo[0]]
                return
            
    def check_for_tie(self):
        if all (self.board[key] is not None for key in self.board):
            if self.winner is None:
                self.tie = True

    def switch_turn(self):
        self.turn = 'O' if self.turn == 'X' else 'X'

    def render(self): #step 3 continued
        self.print_board()
        self.print_message()
    
    #instantiate game
game = Game()

    #call play_game method
game.play_game()

