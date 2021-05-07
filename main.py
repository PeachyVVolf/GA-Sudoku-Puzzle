import Game


def main():
    board1 = Game.SudokuGame()
    board1.create_sudoku_children()
    print("___________BEFORE MUTATE___________")
    for i in range(Game.population_size):
        board1.arr[i].print_fitness()
    print("________MUTATE_________")
    for i in range(Game.population_size):
        board1.mutate_sudoku(i)
    for i in range(int((Game.population_size/60) * 100)):
        board1.crossover(i)

    board1.sort_by_max_fitness()


if __name__ == "__main__":
    main()
