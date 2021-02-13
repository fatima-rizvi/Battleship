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
    all_turns = { 1: [25, "Fun"], 2: [10, "Easy"], 3: [5, "Normal"], 4: [3, "Hard"], 5: [1, "Expert"] }
    
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
            print(f"\nSelected: {all_turns[choice][1]}")
            return all_turns[choice][0]
        else:
            print("Sorry, that is not an option. Please try again.")

wins = 0
losses = 0
playing = ""
while playing.lower() != "n":
    turns = select_diff() # Allow the player 4 turns to hit the ship. Create an input to select ifficulty level with more or less turns.
    for turn in range(turns):
        print(f"\nTurn #{turn + 1}")

        guess_row = int(input("Guess row (1 - 5): ")) - 1 # Minus one accounts for index position starting at 0
        guess_col = int(input("Guess col (1 - 5): ")) - 1


        if guess_row in range(5) and guess_col in range(5):
            if board[guess_row][guess_col] == "X":
                print("You already guessed that one")
            elif guess_row == ship_row and guess_col == ship_col:
                wins += 1
                print("Argh! You sank my battleship! You win!")
                break
            else: 
                print("Ha! You missed my battleship!")
                board[guess_row][guess_col] = "X"
                print_board(board)

        else:
            print("That spot isn't in the ocean! What are you playing at?")
        
        if (turn + 1) == turns: # beause we get turns from range(turns)
            losses += 1
            print("You lost! Better luck next time!\n")
            choice = ""
            while choice.lower() not in ["n", "y"]:
                choice = input("Would you like to play again? (y/n): ")
                if choice.lower() == 'y':
                    print("Okay, let's play!")
                elif choice.lower() == 'n':
                    playing = choice
                    print("Okay, see you around!")
                else:
                    print("Sorry, that is not an option.")
    
    print(f"""
                SCORE:        
    ----------------------------
            PLAYER: {wins} 
            CPU:    {losses} 
    ----------------------------
    """)

