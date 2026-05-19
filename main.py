import random
board = [" "  for _ in range(9)]
#print(board)
#create a function to form the grid 
current_player = "X"
def print_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])   
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()
    #one mistake that i made here is by not adhering to the indentation rule , i ended up calling the function inside itself.
#print_board()
def player_input():
    while True:
        try:
            choice = int(input("choose a position (1-9): ")) - 1
            #checks range
            if choice  < 0 or choice > 8:
                print("Invalid number. Please enter a number between 1 and 9.")
                continue
            #checks if the position is already taken
            if board[choice] != " ":
                print("Choice already taken. Please choose another choice.")
                continue
            #valid move
            board[choice] = current_player
            break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
def switch_player():
    global current_player
    
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"
        #determining the winner by checking all the winning conditions
def check_winner():
    winning_positions = [
        [0,1,2], [3,4,5], [6,7,8],#rows
        [0,3,6], [1,4,7], [2,5,8],#columns  
        [0,4,8], [2,4,6]#diagonals 
    ]

    for condition in winning_positions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != " ":
            return True

    return False
# incase there is no win and no win and the board is full then that is a draw
def check_draw():
    return " " not in board
#computer oponent 
def computer_move(): 
    winning_positions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for line in winning_positions:
        values = [board[i] for i in line]
        if values.count("O") == 2 and values.count(" ") == 1:
            move = line[values.index(" ")]
            board[move] = "O"
            return

    for line in winning_positions:
        values = [board[i] for i in line]
        if values.count("X") == 2 and values.count(" ") == 1:
            move = line[values.index(" ")]
            board[move] = "O"
            return

    if board[4] == " ":
        board[4] = "O"
        return

    corners = [0, 2, 6, 8]
    available_corners = [i for i in corners if board[i] == " "]

    if available_corners:
        import random
        board[random.choice(available_corners)] = "O"
        return

    sides = [1, 3, 5, 7]
    available_sides = [i for i in sides if board[i] == " "]

    if available_sides:
        import random
        board[random.choice(available_sides)] = "O"
        return

    empty_positions = [i for i in range(9) if board[i] == " "]
    import random
    board[random.choice(empty_positions)] = "O"
   
  


# where the program run
while True:   # 🔁 OUTER LOOP (controls replay)

    board = [" " for _ in range(9)]
    current_player = "X"

    # 🎮 INNER GAME LOOP
    while True:
        print_board()

        if current_player == "X":
            player_input()
        else:
            computer_move()

        if check_winner():
            print_board()
            if current_player == "X":
                print("🎉 You win!")
            else:
                print("💻 Computer wins!")
            break

        if check_draw():
            print_board()
            print("🤝 It's a draw!")
            break

        switch_player()

    # 🔁 REPLAY LOGIC (MUST be inside OUTER loop)
    replay = input("Play again? (yes/no): ").lower()

    if replay == "yes":
        print("Restarting the game...")
        continue   # goes back to OUTER loop start
    else:
        print("Bye!")
        break
