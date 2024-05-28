from Battleship import drawBoard, isGameOver, setupBoard, checkHitOrMiss

def main():
    # Create a new game board
    board = setupBoard()

    # Loop the game until GAME OVER
    while True:
        drawBoard(board)

        # Prompt user for column input
        while True:
            try:
                col = int(input('Enter a column (X): '))
                # Check for valid column range (0-9)
                if col < 0 or col >= 10:
                    print('Invalid column.')
                else:
                    break
            # Throw exception if user inputs a character or invalid input.
            except ValueError:
                print('Invalid input. Please enter a number.')

        # Prompt user for row input
        while True:
            try:
                row = int(input('Enter a row (Y): '))
                # Check for valid row range (0-9)
                if row < 0 or row >= 10:
                    print('Invalid row.')
                else:
                    break
            # Throw exception if user inputs a character or invalid input.
            except ValueError:
                print('Invalid input. Please enter a number.')

        # Check if the shot is HIT or MISS
        result = checkHitOrMiss(board,row,col)
        print(result)

        # Check if game is over
        if isGameOver(board):
            drawBoard(board)
            print('GAME OVER!')
            break

# Run the main function
if __name__ == '__main__':
    main()
