import Sudoku_Storage

game = Sudoku_Storage.Sudoku()  # create Sudoku
game.read_from_file()   # read from file and populate array
game.print()    # print Sudoku
game.fitness()  # caluculate and print fitness score, 100% fitness would be 243