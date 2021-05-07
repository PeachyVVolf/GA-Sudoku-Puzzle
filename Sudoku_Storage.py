game_size = 9
best_fitness = 243


def get_box_start_index(box_number):
    if box_number == 0:
        return 0
    elif box_number == 1:
        return 3
    elif box_number == 2:
        return 6
    elif box_number == 3:
        return 30
    elif box_number == 4:
        return 33
    elif box_number == 5:
        return 36
    elif box_number == 6:
        return 60
    elif box_number == 7:
        return 63
    elif box_number == 8:
        return 66


class Sudoku:
    SudokuNumbers = [0] * (game_size * game_size + game_size)
    fitness_score = 0

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
        horizontal_fitness = 0
        vertical_fitness = 0
        box_fitness = 0
        i = -1
        # check horizontally
        for j in range(game_size):
            empty = [0] * 9
            for d in range(game_size):
                i += 1
                if self.SudokuNumbers[i] not in empty and self.SudokuNumbers[i] != '0':
                    empty.append(self.SudokuNumbers[i])
                    horizontal_fitness += 1
            i += 1
        self.fitness_score = self.fitness_score + horizontal_fitness

        # check vertical
        start = -10
        for j in range(game_size):
            empty = [0] * 9
            for d in range(game_size):
                start += 10
                if self.SudokuNumbers[start] not in empty and self.SudokuNumbers[start] != '0':
                    empty.append(self.SudokuNumbers[start])
                    vertical_fitness += 1
            start -= 89
        self.fitness_score = self.fitness_score + vertical_fitness

        # check boxes
        for totalBoxes in range(game_size):
            box_fitness = box_fitness + self.check_box_fitness(totalBoxes, 0)
        self.fitness_score = self.fitness_score + box_fitness

        print("Fitness Score: ", self.fitness_score)

    def check_box_fitness(self, box_number, box_fitness):
        empty = [0] * 9
        index = get_box_start_index(box_number)
        for j in range(3):
            for i in range(3):
                if self.SudokuNumbers[index] not in empty and self.SudokuNumbers[index] != '0':
                    empty.append(self.SudokuNumbers[index])
                    box_fitness += 1
                index += 1
            index += 7
        return box_fitness