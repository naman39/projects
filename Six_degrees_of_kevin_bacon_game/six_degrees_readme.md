# Six Degrees of Kevin Bacon
This project determines the "degrees of separation" between two actors using breadth-first search to find the shortest path through shared movies.

## Overview
The concept is inspired by the Six Degrees of Kevin Bacon game, where actors are connected through the movies they have starred in. The task is to find the shortest path of movies connecting any two actors using IMDb data.

## Getting Started
1. **Download the Distribution Code:** Clone or download the distribution code from here and unzip it.
```git clone https://github.com/naman39/projects/tree/main/Six_degrees_of_kevin_bacon_game```
2. **Change the directory:** cd <repository-directory>
3. **Understanding the Data:** Explore the CSV files provided:
  * people.csv: Contains IDs, names, and birth years of people (actors).
  * movies.csv: Includes IDs, titles, and release years of movies.
  * stars.csv: Establishes relationships between people and movies they starred in.
4. **Exploring degrees.py:** This file manages the loading of data into dictionaries (names, people, movies) and implements the main logic to find the shortest path between two actors using the breadth-first search algorithm.
5. **Test**: ```python degrees.py small```

## Implementation Details
* **Shortest Path Calculation:** The core of the project is the shortest_path function in degrees.py. This function computes the shortest path between two actors using breadth-first search (BFS), treating actors as nodes and movies as edges connecting them.

* **Input and Output:** Users specify two actor names via command-line arguments. The program resolves these names to unique IDs using the person_id_for_name function. The BFS algorithm then finds the shortest path (sequence of movies) connecting these two actors.

* **Output Format:** If a path exists, the program prints the number of degrees of separation and details each movie connection in the path. If no path exists, it notifies the user accordingly.

## Example Usage
![Screenshot 2024-06-17 at 3 52 01 AM](https://github.com/naman39/projects/assets/59209974/597684a7-cd9c-413b-9626-f033e8d101d5)
