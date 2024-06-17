# Crossword Puzzle Generator using Constraint Satisfaction

This project implements a crossword puzzle generator that uses Constraint Satisfaction Problem (CSP) techniques to fill in a given crossword structure with words from a provided vocabulary.

## Project Structure
* **crossword.py:** Contains the definition of the Crossword and Variable classes, which represent the structure and variables of the crossword puzzle.
* **generate.py:** Includes functions to enforce constraints and solve the crossword puzzle using CSP techniques.
* data/:
    *  **structure1.txt:** Example structure file defining the layout of a crossword puzzle.
    *  **words1.txt:** Example file containing a list of words that can be used to fill in the crossword puzzle.
* **requirements.txt:** Lists the Python dependencies required for this project.

## Getting Started
1. Clone this repository:
```git clone <repository-url>```
2. Change the directory
```cd <repository-directory>```
3. Install dependencies:
```pip install -r requirements.txt```
4. To generate a crossword puzzle, run:
```python generate.py data/structure1.txt data/words1.txt output.png```
Replace data/structure1.txt and data/words1.txt with your own structure and word files as needed.

**FOR EXPERIMENTATION I HAVE INCLUDED THREE DIFFERENT SAMPLES OF EACH**

## How It Works
* The crossword puzzle is represented by a grid structure where some squares are blank and need to be filled with letters.
* The generator uses CSP techniques to ensure that each word fits its corresponding variable based on length and overlaps with neighboring variables.
* The program enforces node consistency to ensure that all words in a variable's domain have the correct length.
* Arc consistency is enforced to ensure that there are no conflicts between neighboring variables.
* Backtracking search is used to find a solution that satisfies all constraints and fills the crossword puzzle completely.
  
## Functions Implemented
* **enforce_node_consistency:** Ensures all words in a variable's domain have the correct length.
* **revise:** Makes a variable arc consistent with its neighbor.
* **ac3:** Enforces arc consistency across all variables.
* **assignment_complete:** Checks if a given assignment fills all variables in the crossword.
* **consistent:** Checks if a given assignment satisfies all constraints.
* **order_domain_values:** Orders domain values based on the least-constraining values heuristic.
* **select_unassigned_variable:** Selects an unassigned variable based on the minimum remaining values and degree heuristic.
* **backtrack:** Uses backtracking search to find a complete and satisfactory assignment of variables to values.

![Screenshot 2024-06-16 at 7 17 36 PM](https://github.com/naman39/projects/assets/59209974/f1e22f21-6b7a-4131-94cb-7308ec61f54b)
