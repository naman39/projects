# Minesweeper AI

Minesweeper is a classic puzzle game where the objective is to flag all the mines on a grid without detonating any of them. Each cell on the grid either contains a hidden mine or is safe. The numbers displayed in revealed cells indicate how many neighboring cells contain mines.

## Background

In Minesweeper, the player makes decisions based on the numbers revealed on safe cells and tries to deduce the locations of mines logically. For instance, if a cell displays "1", indicating it has one neighboring mine, adjacent cells can be logically deduced to be safe or mines.

## Propositional Logic Approach

The AI in this project employs propositional logic to reason about the Minesweeper board state:
- Each cell is represented as a propositional variable indicating whether it contains a mine (`True`) or not (`False`).
- Logical sentences are constructed to represent knowledge about the board, where each sentence includes a set of cells and a count of neighboring mines.

## Knowledge Representation

Instead of exhaustively checking each possible model (which is infeasible for larger grids), the AI uses a set-based representation:
- Each logical sentence `{A, B, C} = 1` means exactly one of cells A, B, or C is a mine.
- Inferences are made based on subsets: if `{A, B} = 2` and `{A} = 1`, then `{B} = 1` can be inferred.

## Getting Started

1. **Download the Distribution Code**: Clone or download the distribution code from ```git clone https://github.com/naman39/projects/tree/main/minesweeper%20game ```
   
2. **Install Dependencies**: Navigate to the project directory and run `pip3 install -r requirements.txt` to install the required Python package (pygame).

3. **Understanding the Code**:
   - **minesweeper_game.py**: Contains logic for Minesweeper gameplay and the MinesweeperAI class.
   - **minesweeper_runner.py**: Provides a graphical interface for playing Minesweeper or letting the AI play.

## Implementation Details

- **Minesweeper Class**: Manages the game board and processes user moves.
- **Sentence Class**: Represents logical sentences about the board state, handling known mines, known safes, and updating sentences based on new information.
- **MinesweeperAI Class**: Implements an AI agent that makes logical inferences to play Minesweeper effectively.

## Specifications

- **Tasks**:
  - Complete the implementations of `Sentence` methods (`known_mines`, `known_safes`, `mark_mine`, `mark_safe`).
  - Implement `MinesweeperAI` methods (`add_knowledge`, `make_safe_move`, `make_random_move`) to enable the AI to play the game.

- **Knowledge Base**: Each logical move updates the AI’s knowledge base, enabling it to deduce new safe moves or mine locations.

## Usage

To run the Minesweeper game or let the AI play:
```python minesweepeer_runner.py```
This command starts the graphical interface. Click “AI Move” to let the AI make a move based on its current knowledge.

![Screenshot 2024-06-17 at 4 21 12 AM](https://github.com/naman39/projects/assets/59209974/479a5f9f-f1d7-4469-9b85-276c6a3f794e)
