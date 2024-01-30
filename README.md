# River Crossing Puzzle Algorithm

## Description
River Crossing Puzzle is a type of puzzle where the objective is to transport items from one bank to the other, usually in the fewest possible trips. This project is the algorithm to solve this using Python and OOP.

## Installation
1. Clone the repository.
   ```bash
   git clone https://github.com/JuanPabloGomezHaroCabrera/River-Crossing-Puzzle.git

## Navigate to the project directory
cd River-Crossing-Puzzle

## Run the game
python River-Crossing-Puzzle.py

## Project Structure
1. `River-Crossing-Puzzle.py`: Contains the main function instantiating a game controller.
2. `GameController.py`: Class for managing the algorithm, including points, the boat, and items.
3. `Item.py`: Class for item information, including name, id and eat.
4. `Point.py`: Class for point, the items in it and some functios such as add, remove, search.
5. `Boat.py`: Class for boat information and functions such as get an item in the boat and get out an item of the boat.
6. `README.md`: Project documentation.

## Dependencies
This project uses the following standard Python libraries:

* `os`: For interacting with the operating system and clearing the terminal.
* `time`: For introducing pauses in the game execution.