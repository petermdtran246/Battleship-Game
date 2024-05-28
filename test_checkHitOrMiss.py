from Battleship import checkHitOrMiss

def test_checkHitOrMiss_hit():
    # Create a board where all squares are ships ('S')
    board = [['S'] * 10 for _ in range(10)]
    row = 0
    col = 0
    result = checkHitOrMiss(board, col, row)
    assert result == 'HIT'

def test_checkHitOrMiss_miss():
    # Create a board where all squares are empty ('.')
    board = [['.'] * 10 for _ in range(10)]  # All squares are empty
    row = 0
    col = 0
    result = checkHitOrMiss(board, col, row)
    assert result == 'MISS'

if __name__ == "__main__":
    test_checkHitOrMiss_miss()
    test_checkHitOrMiss_hit()
    print('Unit Test Passed!')

