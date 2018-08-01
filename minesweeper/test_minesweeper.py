"""TDD Test Cases for minesweeper.py
"""

import unittest
from minesweeper import minesweeper_game, Minesweeper

class TestMinesweeper(unittest.TestCase):
    """Description
    """
    def test_board_print(self):
        """Description
        """
        test_game = Minesweeper(10, 10)
        test_game.board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 0, 1, 1, 1, 0, 0, 0, 0], ['*', 1, 0, 1, '*', 1, 0, 0, 0, 0], [1, 1, 1, 2, 2, 1, 0, 0, 0, 0], [0, 1, 2, '*', 1, 0, 0, 0, 0, 0], [0, 1, '*', 3, 2, 1, 0, 0, 0, 0], [0, 1, 1, 2, '*', 1, 0, 0, 0, 0]]
        result = test_game.print_board()
        expected = '- - - - - - - - - - \n- - - - - - - - - - \n- - - - - - - - - - \n- - - - - - - - - - \n1 1 - 1 1 1 - - - - \n* 1 - 1 * 1 - - - - \n1 1 1 2 2 1 - - - - \n- 1 2 * 1 - - - - - \n- 1 * 3 2 1 - - - - \n- 1 1 2 * 1 - - - - \n'
        self.assertEquals(result, expected)

if __name__ == '__main__':
    unittest.main(exit=False)
