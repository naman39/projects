# Tic-Tac-Toe AI using Minimax Algorithm

This project implements a Tic-Tac-Toe game where you can play against an AI that uses the Minimax algorithm to make optimal moves.

## Project Structure

* **tictactoe.py:** Contains the game logic and implementations for various functions required to play Tic-Tac-Toe.

* **runner.py:**  Provides the graphical interface to play the game against the implemented AI.

* **requirements.txt:** Lists the Python dependencies required for this project.

## Getting Started
** USE PYTHON3 AND PIP3 WHILE USING ON MACOS OR LINUX **

1. Clone this repository:
```git clone https://github.com/naman39/projects/tree/main/tictactoe```
2. Change the directory to the repo directory
```cd <repository-directory>```
3. Install dependencies:
``` pip install -r requirements.txt```
4. Run the game:
```python runner.py```

## Gameplay Instructions
* The game starts with X making the first move.
* You can make your move by clicking on an empty cell in the graphical interface.
* The AI will then make its move based on the Minimax algorithm.
* The game ends when either a player wins or the board is full (tie game).

## Functions Implemented
* player(board): Determines whose turn it is (X or O).
* actions(board): Returns all possible legal moves for the current player.
* result(board, action): Returns the board that results from making a move.
* winner(board): Determines the winner of the game, if any.
* terminal(board): Checks if the game is over (terminal state).
* utility(board): Returns the utility of the current board from the perspective of the player.

## Minimax Algorithm
* The AI uses the Minimax algorithm to ensure it plays optimally:

* Minimax is a recursive algorithm that considers all possible future moves to choose the best one.
* It assumes that both players play optimally, thus aiming to minimize the maximum possible loss (minimize the opponent's best possible outcome).

![Screenshot 2024-06-16 at 6 17 09 PM](https://github.com/naman39/projects/assets/59209974/05b63425-ffe4-47df-8046-bf2af6cfd4c0)
