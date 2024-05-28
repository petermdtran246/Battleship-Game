from Battleship import isGameOver

def test_isGameOver():
    # Test case 1: All ships sunk (True)
    board = [['X'] * 10 for _ in range(10)]  # All squares are ('X')
    assert isGameOver(board) == True

    # Test case 2: Ships remaining (False)
    board = [['.'] * 10 for _ in range(10)]  # All squares are empty ('.')
    board[0][0] = 'S'
    assert isGameOver(board) == False

# Run tests if script is run directly
if __name__ == '__main__':
  test_isGameOver()
  print("Unit tests passed!")