import array

game_size = 9


class Sudoku:
    SudokuNumbers = [0] * (game_size * game_size + game_size)

    def read_from_file(self):
        file = open("input.txt", "r")
        for i in range(game_size * game_size + game_size - 1):
            self.SudokuNumbers[i] = file.readline(1)

    def print(self):
        row = 0
        col = 0
        for i in range(game_size * game_size + game_size - 1):
            if row == 3:
                print("|", end="")
                row = 0
            if col == 27:
                print("")
                print("______________", end="")
                col = 0
            print(self.SudokuNumbers[i], end="")
            if self.SudokuNumbers[i] != "\n":
                row += 1
                col += 1
        print("|")

    def fitness(self):
        i = 0