# Tic Tac Toe- Python Zelle Graphics
## What is this?

This is a fully interactive Tic Tac Toe game using Python and John Zelle's graphics library. This game includes full mouse interaction, interactive buttons for restart and end game, win detection, tie game handling, and a win tracker which keeps scores for ties and Player 1 and Player 2 wins. 

## Features

### Interactive game board
- 3x3 grid board
- Click based gameplay
- X's and O's are centered upon click

### Win detection
- Searches vertically, horizontally, and diaganolly for win using loops
- Decorative color flashing of the grid
- Victory displayed above game board

### Restart and quit buttons
- Restart button clears:
    * X's and O's
    * Victory message
- Quit button closes game window

### Score tracking
- Updates each player's score and ties on screen after each game

### Graphic design
- Neat grid and text
- Cohesive colors used
- Buttons moving when clicked


## Requirements

### Make sure you have:
- Python 3.x
- graphics.py in the same folder

## Running the game
- Clone or download the repository

- Place tictactoe.py and graphics.py in the same folder

- Run:

```python
python3 tictactoe.py

```
- A 1000×1000 game window will open.


## How it works
- **window()**  
  Creates the main game window and sets the background.

- **draw_grid()**  
  Draws the 3×3 Tic Tac Toe board using four line objects.

- **check_vic()**  
  Checks rows, columns, and diagonals to detect a win.

- **victory()**  
  Displays the “Victory!” message at the top of the screen.

- **counterWIN()**  
  Draws and updates the scoreboard for Player 1, Player 2, and Ties.

- **button() / quitB()**  
  Creates animated Restart and Quit buttons.

- **tictactoe()**  
  Main game loop:
  - handles mouse clicks  
  - places X and O  
  - prevents overwriting cells  
  - checks for win/tie  
  - updates counters  
  - manages game-over state  
  - handles restart/quit  

- **main()**  
  Starts the game


## License
  - MIT license- free to use, modify and share


