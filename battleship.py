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

if board[guess_row][guess_col] == "X":
    print("You already guessed that one")
elif guess_row == ship_row and guess_col == ship_col:
    print("Argh! You sank my battleship!")
else: 
    if guess_row not in range(5) or guess_col not in range(5):
        print("That spot isn't in the ocean! What are you playing at? Try again.")
    else:
        print("Ha! You missed my battleship!")
        board[guess_row][guess_col] = "X"
        print_board(board)