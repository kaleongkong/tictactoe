#!/usr/bin/python
import random
import sys  # for exiting without an error


class TicGame(object):
    def __init__(self):
        '''
        Let's assume the human player will always be X.

        >>> game = TicGame()

        >>> print(game)
        <BLANKLINE>
        <BLANKLINE>
        <BLANKLINE>
        <BLANKLINE>

        >>> game.human_moves_to(0)

        '''
        self.game_over = False
        self.board = [' ' for _ in range(0, 9)]
        self.game_loop()
    
    def game_loop(self):
        while not self.game_over:
            self.get_human_move()
            end_condition = self.check_end_condition()
            if end_condition and end_condition != 'tie':
                print("{the_winner} wins!".format(the_winner=end_condition))
                sys.exit(0)
            elif end_condition == 'tie':
                print("It's a tie game.")
                sys.exit(0)
            self.make_cpu_move()

    def __str__(self):
        '''
        The rendering logic
        '''
        board_str = ""
        for i, xo in enumerate(self.board, 1):  # start at index 1, for modulo
            board_str += xo
            if i % 3 == 0:
                board_str += '\n'
        return board_str

    def get_human_move(self):
        try:
            move = raw_input("Your move [1-9]> ")
            # indexing from 0, so a human 1 is actually 0 in self.board list
            self.human_moves_to(int(move) - 1)
            print(self)
        except:
            # no exit condition defined!
            self.get_human_move()

    def human_moves_to(self, location):
        if self.board[location] != ' ':
            raise
        else:
            self.board[location] = 'X'
    
    def check_end_condition(self, checking_human=True):
        '''
        Check if there are any three-in-a-row, and respond accordingly.

        There are 8 possible win conditions in a 1-9 configuration, any one of

        123  147
        456  258
        789  369
        159
        357
        
        Check for any of those and return the winner
        '''
        win_conditions = ['123', '456', '789', '147', '258', '369', '159',
                          '357']
        # possible outcomes: 'player' (win) and 'cpu' (lose), 'draw', and False
        tmp_board = ''
        for i, _ in enumerate(self.board, 1):
            if checking_human and _ == 'X':
                tmp_board += str(i)
            elif not checking_human and _ == 'O':
                tmp_board += str(i)
        for w in win_conditions:
            if w in tmp_board:
                if checking_human:
                    return 'player'
                else:
                    return 'cpu'
        if ' ' not in self.board:
            # A tie occurs when the board is full AND nobody wins. We checked
            # for a winner in the above for loops, now we've seen there are
            # no more spaces to fill, so it's a tie:
            return 'tie'

        # the above doesn't work if there are other moves between, ex:
        # 1,2,4,6,7 should result in a win but does not. Adjusting...

        # if w in [p for p in permutations(tmp_board)]:
        # TODO: out of time!
        return False

    def make_cpu_move(self):
        '''
        We assumed the human will always be X, so the opponent must be O.
        TODO
        '''
        cpu_choice = random.choice([i for i, _ in enumerate(self.board)
                                    if _ == ' '])
        self.board[cpu_choice] = 'O'
        print(self)

if __name__ == "__main__":
    # import doctest; doctest.testmod()
    game = TicGame()
