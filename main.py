import Game


def main():
    board1 = Game.SudokuGame()

    while(True):

        board1.create_sudoku_children()
        # print("___________BEFORE MUTATE___________")
        # for i in range(Game.population_size):
        #     board1.arr[i].print_fitness()
        # print("________MUTATE_________")
        for i in range(Game.population_size):
            board1.mutate_sudoku(i)

        board1.sort_by_max_fitness()

        for i in range(int((Game.population_size/100) * 60)):
            board1.crossover(i)

        board1.sort_by_max_fitness()

        print("__________BEST___________")
        board1.arr[0].print_fitness()

        board1.set_game(board1.arr[0])


if __name__ == "__main__":
    main()
