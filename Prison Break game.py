import random

# Step 1: Create the game board
board = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
]

# Step 2: Place the player and the guard on the game board
player_row, player_col = random.randint(1, 8), random.randint(1, 8)
board[player_row][player_col] = 'P'

guard_row, guard_col = random.randint(1, 8), random.randint(1, 8)
while guard_row == player_row and guard_col == player_col:
    guard_row, guard_col = random.randint(1, 8), random.randint(1, 8)
board[guard_row][guard_col] = 'G'

# Step 3-6: Move the player and check if they've escaped or been caught
while True:
    # Print the game board
    for row in board:
        print(' '.join(row))

    # Ask the user for the direction they want to move in
    direction = input("Which direction do you want to move in? (up/down/left/right) ")

    # Move the player in the specified direction
    if direction == 'up':
        if player_row == 1:
            print("You can't move up any further!")
        else:
            board[player_row][player_col] = ' '
            player_row -= 1
            board[player_row][player_col] = 'P'
    elif direction == 'down':
        if player_row == 8:
            print("You can't move down any further!")
        else:
            board[player_row][player_col] = ' '
            player_row += 1
            board[player_row][player_col] = 'P'
    elif direction == 'left':
        if player_col == 1:
            print("You can't move left any further!")
        else:
            board[player_row][player_col] = ' '
            player_col -= 1
            board[player_row][player_col] = 'P'
    elif direction == 'right':
        if player_col == 8:
            print("You can't move right any further!")
        else:
            board[player_row][player_col] = ' '
           
