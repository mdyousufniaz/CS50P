from sudoku import Sudoku
from random import randint

while (diff := int(input("Enter a difficulty: "))) != -1:
    seed = randint(1, 1000)
    print(seed, diff)
    Sudoku(3, seed=seed).difficulty(diff / 10).show()