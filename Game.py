import Sudoku_Storage
import random

population_size = 10

class SudokuGame:

    arr = [0] * population_size
    game = 0

    def __init__(self):
        self.game = Sudoku_Storage.Sudoku()  # create Sudoku
        self.game.read_from_file()   # read from file and populate array
        self.game.fitness()  # calculate and print fitness score, 100% fitness would be 243
        self.game.print()    # print Sudoku

    def create_sudoku_children(self):
        for i in range(population_size):
            self.arr[i] = self.game
            self.add_in_sudoku((self.arr[i]))
            self.arr[i].print()

    def add_in_sudoku(self, board):
        for i in range(Sudoku_Storage.game_size * Sudoku_Storage.game_size + Sudoku_Storage.game_size):
            if board.SudokuNumbers[i] == '0':
                board.SudokuNumbers[i] = random.randint(1, 9)
        board.fitness()