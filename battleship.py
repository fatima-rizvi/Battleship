from random import randint

board = []

for x in range(0, 5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print(" ".join(row))

def random_row(board):
    return randint(0, len(board) -1)

def random_col(board):
    return randint(0, len(board) -1)

ship_row = random_row(board)
ship_col = random_col(board)

guess_row = int(input("Guess row: "))
guess_col = int(input("Guess col: "))

print(ship_col)
print(ship_row)

if guess_row == ship_row and guess_col == ship_col:
    print("Argh! You sank my battleship!")
else: 
    print("Ha! You missed my battleship!")