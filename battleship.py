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

print(f"Row num: {ship_row + 1}")
print(f"Col num: {ship_col + 1}")

def select_diff():    # Function to select difficulty level, which affects number of turns
    all_turns = { 1: 25, 2: 10, 3: 5, 4: 3, 5: 1 }
    
    choice = " "
    while choice not in all_turns:
        choice = int(input("""
        ----------------------------
                BATTLESHIP                

            Select difficulty:        

        1. Fun      (25 turns) 
        2. Easy     (10 turns)
        3. Normal    (5 turns)
        4. Hard      (3 turns) 
        5. Expert     (1 turn)    
        ----------------------------
        Difficulty (1/2/3/4/5): """))
        if choice in all_turns:
            return all_turns[choice]
        else:
            print("Sorry, that is not an option. Please try again.")



turns = select_diff() # Allow the player 4 turns to hit the ship. Create an input to select ifficulty level with more or less turns.
for turn in range(turns):
    print(f"\nTurn #{turn + 1}")

    guess_row = int(input("Guess row (1 - 5): ")) - 1 # Minus one accounts for index position starting at 0
    guess_col = int(input("Guess col (1 - 5): ")) - 1


    if guess_row in range(5) and guess_col in range(5):
        if board[guess_row][guess_col] == "X":
            print("You already guessed that one")
        elif guess_row == ship_row and guess_col == ship_col:
            print("Argh! You sank my battleship! You win!")
            break
        else: 
            print("Ha! You missed my battleship!")
            board[guess_row][guess_col] = "X"
            print_board(board)

            if turn == turns:
                print("You lost! Better luck next time!")
    else:
        print("That spot isn't in the ocean! What are you playing at?")

