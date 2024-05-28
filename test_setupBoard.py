from Battleship import setupBoard

# Global variable for grid size
GRID_SIZE = 10
# Global variable for number of ships to place
NUM_SHIPS = 5

def test_setupBoard():
    # Create a new game board using setupBoard
    board = setupBoard()
    num_ships = 0
    for row in board:
        for col in row:
            if col == 'S':
                num_ships += 1
    assert num_ships == NUM_SHIPS

if __name__ == "__main__":
    test_setupBoard()
    print("Unit Tests Passed!")