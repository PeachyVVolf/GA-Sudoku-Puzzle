import Game


def main():
    board1 = Game.SudokuGame()
    index = 0

    while index <= 3000:

        board1.create_sudoku_children()
        for i in range(Game.population_size):
            board1.mutate_sudoku(i)
        board1.merge_sort(0, Game.population_size - 1)

        for i in range(int((Game.population_size/100) * 60)):
            board1.crossover(i)

        board1.merge_sort(0, Game.population_size - 1)

        print("__________BEST___________")
        board1.arr[0].print_fitness()
        print(index)
        index += 1

        board1.set_game(board1.arr[0])

    board1.arr[0].print()
    board1.arr[0].print_fitness()

if __name__ == "__main__":
    main()
