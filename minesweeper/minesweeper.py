"""Solution for Minesweeper Game
"""
from random import randint
import os

class Minesweeper:
    def __init__(self, width, height):
        self.difficulty = 0.05
        self.height = height
        self.width = width
        self.board = [[None] * width for x in xrange(height)]
        self.unhidden_board = [[None] * width for x in xrange(height)]
        self.game_won = False
        self.game_ended = False
        self.create_board()
        return

    def is_game_won(self):
        for i in xrange(self.width):
            for j in xrange(self.height):
                if self.board[i][j] == '*' and self.unhidden_board[i][j] != 'f':
                    self.game_won = False
                    return self.game_won
        self.game_won = True
        self.game_ended = True
        return self.game_won

    def print_board(self):
        output = ''
        for line in self.board:
            for block in line:
                if block == 0:
                    output = output + '- '
                else:
                    output = output + str(block) + ' '
            output = output +  '\n'
        print output
        return output

    def print_secret_board(self):
        """Print values for unhidden board
        User indicated "Flagged" mine with 'F'
        User indicates "Cleared" block with 'C'
        """
        print '-'*(self.width*2+2)
        for i in xrange(self.width):
            print '|',
            for j in xrange(self.height):
                if self.unhidden_board[i][j] == 'c':
                    if self.board[i][j] == 0:
                        print '-',
                    else:
                        print self.board[i][j],
                elif self.unhidden_board[i][j] == 'f':
                    print self.unhidden_board[i][j],
                else:
                    print ' ',
            print '|'
        print '-'*(self.width*2+2)

    def clear_zeroed_neighbors(self, x, y):
        #check if block has of value 0 and set view to cleared
        self.unhidden_board[x][y] = 'c'

        for i in xrange(-1, 2):
            for j in xrange(-1, 2):
                new_x = x + i
                new_y = y + j
                if (new_x == x and new_y == y) or \
                    (new_x >= self.width or new_x < 0) or \
                    (new_y >= self.height or new_y < 0):
                    continue
                else:
                    if self.unhidden_board[new_x][new_y] != 'c':
                        self.unhidden_board[new_x][new_y] = 'c'
                        if self.board[new_x][new_y] == 0:
                            self.clear_zeroed_neighbors(new_x, new_y)
        return


    def create_board(self):
        """Populate board with Hidden Mines according to difficulty
        Ensure at least one mine is present in game

        Returns:
            board: Description
        """
        #Determine number and placement of mines
        num_of_mines = int(self.difficulty * self.height * self.width + 1)
        for i in xrange(num_of_mines):
            self.board[randint(0, self.width - 1)][randint(0, self.width - 1)] = '*'

        #Populate board with number hints
        for x in xrange(self.width):
            for y in xrange(self.height):
                score = 0
                for i in xrange(-1, 2):
                    for j in xrange(-1, 2):
                        new_x = x + i
                        new_y = y + j
                        if (new_x == x and new_y == y) or \
                            (new_x >= self.width or new_x < 0) or \
                            (new_y >= self.height or new_y < 0):
                            continue
                        if self.board[new_x][new_y] == '*':
                            score += 1
                if self.board[x][y] != '*':

                    self.board[x][y] = score
        return self.board

def minesweeper_game(game):
    """Main loop for minesweeper game
    """
    x, y, val = 0, 0, None
    warning = False
    while not game.game_ended:
        os.system("clear")
        print "Guess can be 'c' to clear or 'f' to flag a mine"
        if warning:
            print "INVALID GUESS!! PLEASE TRY AGAIN"
            warning = False
        game.print_secret_board()
        guess = list(raw_input("Enter the [y, x, guess] values:").split(','))
        if guess[2] != 'c' and guess[2] != 'f':
            warning = True
        else:
            game.unhidden_board[int(guess[0])][int(guess[1])] = guess[2]
            if guess[2] == 'c' and game.board[int(guess[0])][int(guess[1])] == 0:
                game.clear_zeroed_neighbors(int(guess[0]), int(guess[1]))
            elif guess[2] == 'c' and game.board[int(guess[0])][int(guess[1])] == '*':
                game.game_ended = True
        game.is_game_won()
    if game.game_won:
        os.system("clear")
        print "YOU WON THE GAME!!"
    else:
        os.system("clear")
        print "YOU LOSE! :'("
    return

def main():
    """Receives input from stdin, provides output to stdout.
    """
    height = 10
    width = 10
    try:
        width, height = map(int,raw_input("Input the size of the board (width, height):").split(','))
    except:
        pass
    new_game = Minesweeper(width, height)
    minesweeper_game(new_game)

if __name__ == '__main__':
    main()
