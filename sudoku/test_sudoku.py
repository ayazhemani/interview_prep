"""TDD Test Cases for suducku.py
"""

import unittest
from sudoku import play_sudoku, Sudoku

class TestSuducku(unittest.TestCase):
    """Description
    """
    new_game = Sudoku('000000010002000034000051000000006500070300080003000000000080000580000900690000000')

    def test_board_print(self):
        """Description
        """
        result = self.new_game.print_board()
        self.assertEquals(result, "+-------+-------+-------+\n|   |   | \x1b[1m1\x1b[0m |\n\x1b[0m|  \x1b[1m2\x1b[0m|   | \x1b[1m3\x1b[0m\x1b[1m4\x1b[0m|\n\x1b[0m|   | \x1b[1m5\x1b[0m\x1b[1m1\x1b[0m|   |\n\x1b[0m+-------+-------+-------+\n|   |  \x1b[1m6\x1b[0m|\x1b[1m5\x1b[0m  |\n\x1b[0m| \x1b[1m7\x1b[0m |\x1b[1m3\x1b[0m  | \x1b[1m8\x1b[0m |\n\x1b[0m|  \x1b[1m3\x1b[0m|   |   |\n\x1b[0m+-------+-------+-------+\n|   | \x1b[1m8\x1b[0m |   |\n\x1b[0m|\x1b[1m5\x1b[0m\x1b[1m8\x1b[0m |   |\x1b[1m9\x1b[0m  |\n\x1b[0m|\x1b[1m6\x1b[0m\x1b[1m9\x1b[0m |   |   |\n\x1b[0m+-------+-------+-------+")

if __name__ == '__main__':
    unittest.main(exit=False)
