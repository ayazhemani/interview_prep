"""Solution for Console game of Sudoku (Single Digit)
"""
import os

class bcolors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    AMBER = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Sudoku:

    def __init__(self, board_stream):
        self.board = [[None]*9 for i in xrange(9)]
        self.board_colors = [[None]*9 for i in xrange(9)]

        for i in xrange(81):
            self.board[i/9][i%9] = int(board_stream[i])

        for i in xrange(9):
            for j in xrange(9):
                if int(self.board[i][j]) < 10 and int(self.board[i][j]) > 0:
                    self.board_colors[i][j] = bcolors.BOLD
                else:
                    self.board_colors[i][j] = bcolors.BLUE

    def get_row(self, row_num):
        return self.board[row_num]

    def get_column(self, column_num):
        result = []
        for i in xrange(9):
            result.append(self.board[i][column_num])
        return result #[self.board[i][column_num] for i in xrange(9)]

    def get_block(self, row, col):
        block_num = (col/3) + 3*(row/3)

        block_row = block_num / 3
        block_col = block_num % 3

        result = []
        for i in xrange(0 + block_row*3, 4 + block_row*3):
            for j in xrange(0 + block_col*3, 4 + block_col*3):
                result.append(self.board[i][j])
        return result

    def validate_input(self, row, col):
        insert_val = self.board[row][col]
        self.board_colors[row][col] = bcolors.BLUE

        row_digits = self.get_row(row)
        col_digits = self.get_column(col)
        block_digits = self.get_block(row, col)
        all_digits = row_digits + col_digits + block_digits
        print all_digits

        if all_digits.count(insert_val) > 1 and insert_val != 0:
            self.board_colors[row][col] = bcolors.RED
            return False

        return True

    def print_board(self):
        """Clear screen and pretty print the layout of the current sudoku board

        Args:
            board (int[9][9]): current state of the Sudoku game

        Returns:
            None: No output is returned
        """
        sp = ' ' # Extra space for pretty print
        os.system('clear')
        output = ""
        for i in xrange(9):
            if i%3 == 0:
                output = output + ('+' + '-'*(3+4*len(sp)))*3 + '+\n'
            for j in xrange(9):
                if j%3 == 0:
                    output = output + '|' + sp
                if self.board[i][j] == 0:
                    output = output + ' ' + sp
                else:
                    output = output + self.board_colors[i][j] + \
                             str(self.board[i][j]) + bcolors.ENDC + sp
            output = output + '|\n'
            output = output + bcolors.ENDC
        output = output + ('+' + '-'*(3+4*len(sp)))*3 + '+\n'
        print output
        return output


def play_sudoku(game):
    """Initiates the game of sudoku
    """
    buffer_warning = ''
    while True:
        game.print_board()
        print buffer_warning
        inserted = map(int, list(raw_input("Provide the [Row#, Col#, and value] to insert: ")))
        game.board[inserted[0]][inserted[1]] = inserted[2]
        if not game.validate_input(inserted[0], inserted[1]):
            buffer_warning = 'INCORRECT VALUE INSERTED! PLEASE TRY AGAIN...'
        else:
            buffer_warning = 'CORRECT SO FAR...'
    return




def main():
    """Receives input from stdin, provides output to stdout.
    Input expected as integers 0-9, where 0 indicates a blank
    """
    # Read the Sudoku puzzle input

    board_stream = raw_input().strip()
    #board_stream = '000000010002000034000051000000006500070300080003000000000080000580000900690000000'


    new_game = Sudoku(board_stream)
    play_sudoku(new_game)

if __name__ == '__main__':
    main()
