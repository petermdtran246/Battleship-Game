# Battleship Game

This project implements a text-based variation of the classic Battleship game. Your opponent is simulated by the program, randomly firing shots at your board until all your ships are sunk.

## Gameplay:

  -  A 10x10 grid represents the game board.
  -  You (the player) have 5 ships randomly placed on the board (represented by 'S').
  -  The program simulates your opponent, firing shots based on user-entered coordinates (column and row).
  -  The game provides feedback on whether each shot is a HIT ('X') or MISS ('O').
  -  The game ends when all your ships are sunk (defeat!) or the program runs out of valid shots (victory!).

## Code Structure:

The code consists of several methods:

  -  drawBoard(board): Displays the current state of the game board, including column and row labels.
  -  isGameOver(board): Checks if all ships on the board have been sunk ('X').
  -  setupBoard(): Creates a new game board with randomly placed ships ('S').
  -  checkHitOrMiss(board, col, row): Determines the outcome of a shot based on coordinates and updates the board.
  -  main(): Manages the game loop, user interaction, and calls other functions.
