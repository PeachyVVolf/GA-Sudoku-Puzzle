import Sudoku_Storage
import random

population_size = 5


class SudokuGame:

    arr = [0] * population_size

    def __init__(self):
        self.game = Sudoku_Storage.Sudoku()  # create Sudoku
        self.game.read_from_file()   # read from file and populate array
        self.game.fitness()  # calculate and print fitness score, 100% fitness would be 243
        self.game.print()    # print Sudoku

    def create_sudoku_children(self):
        for i in range(population_size):
            self.arr[i] = Sudoku_Storage.Sudoku()
            self.arr[i].deep_copy(self.game)
            self.add_in_sudoku(self.arr[i])

    def add_in_sudoku(self, board):
        for i in range(Sudoku_Storage.game_size * Sudoku_Storage.game_size + Sudoku_Storage.game_size):
            if board.SudokuNumbers[i] == 0:
                board.SudokuNumbers[i] = random.randint(1, 9)
        board.fitness()

    def mutate_sudoku(self, array_index):
        random_index_to_mutate = random.randint(0, Sudoku_Storage.game_size * Sudoku_Storage.game_size + Sudoku_Storage.game_size - 1)
        self.arr[array_index].SudokuNumbers[random_index_to_mutate] = random.randint(1, 9)
        self.arr[array_index].fitness()
        self.arr[array_index].print_fitness()
        if self.arr[array_index]. fitness_score == Sudoku_Storage.best_fitness:
            exit()

    def sort_by_max_fitness(self):
        temp = Sudoku_Storage.Sudoku()
        for i in range(population_size):
            for j in range(population_size - 1):
                if self.arr[j].fitness_score < self.arr[j + 1].fitness_score:
                    temp.deep_copy(self.arr[j])
                    self.arr[j].deep_copy(self.arr[j + 1])
                    self.arr[j + 1].deep_copy(temp)

        print("_________________________AFTER SORT_________________________")
        for i in range(population_size):
            self.arr[i].print_fitness()

    def crossover(self, first_index):
        second_index = random.randint(0, population_size - 1)
        cut_off = random.randint(0, Sudoku_Storage.game_size * Sudoku_Storage.game_size + Sudoku_Storage.game_size)

