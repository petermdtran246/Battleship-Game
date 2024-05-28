import random

# Global variable for grid size
GRID_SIZE = 10
# Global variable for number of ships to place
NUM_SHIPS = 5

'''Define drawBoard method that takes one parameter'''
def drawBoard(myBoard):
    # Print column headers (Using List Comprehension)
    col_headers = [str(col) for col in range(GRID_SIZE)]

    # Print the top border with column headers
    print(' +' + '-+' * GRID_SIZE)
    print('  ' + ' '.join(col_headers))
    print(' +' + '-+' * GRID_SIZE)

    # Print each row with row number and board content
    for row in range(GRID_SIZE):
        # Print row number
        print(f'{row}|', end='')
        for col in range(GRID_SIZE):
            # Print content of each square
            print(f'{myBoard[row][col]}|', end='')
        print()
    # Print the bottom border
    print(' +' + '-+' * GRID_SIZE)

'''Define isGameOver method that takes on parameter'''
def isGameOver(myBoard):
    # Iterate through each row of the board
    for row in myBoard:
        # If any row contains 'S' (ship), GAME OVER!
        if 'S' in row:
            return False
    # If no ships are found, GAME OVER!
    return True

'''Define setupBoard method'''
def setupBoard():
    # Initialize the board with all squares empty ('.')
    board = [['.'] * GRID_SIZE for _ in range(GRID_SIZE)]
    ships_placed = 0

    # Loop until all ships are placed on the board
    while ships_placed < NUM_SHIPS:
        # Generate random row and column
        randomRow = random.randint(0, GRID_SIZE-1)
        randomCol = random.randint(0, GRID_SIZE-1)

        # Check if the square is empty before placing a ship
        if board[randomRow][randomCol] == '.':
            board[randomRow][randomCol] = 'S'
            # Increment ship counter
            ships_placed += 1
    return board

'''Define checkHitOrMiss method that takes three parameters'''
def checkHitOrMiss(myBoard, row, col):
    # Check if the shot hits a ship ('S')
    if myBoard[row][col] == 'S':
        # Mark the sunk ship with 'X'
        myBoard[row][col] = 'X'
        return 'HIT'

    # Check if the shot misses on empty square ('.')
    elif myBoard[row][col] == '.':
        # Mark the miss with 'O'
        myBoard[row][col] = 'O'
        return 'MISS'

    # Check if player shoots the same square again
    elif myBoard[row][col] == 'X':
        return 'HIT'
    elif myBoard[row][col] == 'O':
        return 'MISS'



