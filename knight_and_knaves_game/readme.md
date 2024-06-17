# Knights and Knaves Puzzles

Knights and Knaves puzzles are logical puzzles where characters (either knights or knaves) make statements. Knights always tell the truth, while knaves always lie. The objective is to determine the nature (knight or knave) of each character based on their statements.

## Background

In 1978, Raymond Smullyan introduced Knights and Knaves puzzles in his book "What is the name of this book?". Each puzzle involves characters who make statements about themselves or others. The challenge is to use propositional logic to deduce which characters are knights and which are knaves based on their statements.

## Getting Started

1. **Download the Distribution Code**: Clone or download the distribution code from https://github.com/naman39/projects/tree/main/knight_and_knaves_game 

2. **Understanding the Code**:
   - **logic.py**: Defines logical connectives (`And`, `Or`, `Not`, etc.) and includes a `model_check` function for checking entailment using model checking.
   - **puzzle.py**: Contains four puzzles (`puzzle0`, `puzzle1`, `puzzle2`, `puzzle3`) where you'll add knowledge bases to deduce the characters' roles.

## Implementation Details

- **Propositional Symbols**: Each character is represented as a propositional symbol (`AKnight`, `AKnave`, etc.), where `AKnight` signifies "A is a knight" and `AKnave` signifies "A is a knave".
  
- **Knowledge Bases**: For each puzzle (`knowledge0`, `knowledge1`, `knowledge2`, `knowledge3`), you'll add logical statements that represent the structure of the problem and the statements made by each character.

- **Logical Reasoning**: Using the `model_check` function from `logic.py`, the program checks if a given knowledge base entails the query (the truth of each propositional symbol).

## Specifications

- **Puzzle Descriptions**:
  - **Puzzle 0**: A single character A says "I am both a knight and a knave."
  - **Puzzle 1**: Characters A and B; A says "We are both knaves" and B says nothing.
  - **Puzzle 2**: Characters A and B; A says "We are the same kind" and B says "We are of different kinds."
  - **Puzzle 3**: Characters A, B, and C; A says either "I am a knight" or "I am a knave", B then makes two statements, and C makes one statement.

- **Knowledge Base Construction**: You'll construct logical statements for each puzzle that capture the truthfulness of the statements made by the characters and the constraints of Knights and Knaves logic.

## Example Usage
![Screenshot 2024-06-17 at 4 09 42 AM](https://github.com/naman39/projects/assets/59209974/0d22b708-8e32-49f0-abf9-bf8c982fac40)
