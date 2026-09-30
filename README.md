# Mouse Hunt 🐭

## Overview

Mouse Hunt is a simple Python Turtle game based on the snake-game concept. The player controls a green snake and tries to catch the mouse. Each mouse gives 10 points. The game ends when the snake hits the boundary or its own body.

## Features

- Arrow-key controls
- Mouse as the target
- Score and high score
- Snake body grows after catching a mouse
- Wall collision
- Self collision
- Space key to restart
- Simple Turtle graphics
- No external game engine required

## Technology Used

- Python 3
- Turtle module
- Random module
- Time module

## Requirements

Python 3 must be installed on the computer.

The project uses Python's built-in modules, so no external package installation is required.

## How to Run

1. Download or clone this repository.
2. Open the project folder in VS Code or another Python editor.
3. Open `main.py`.
4. Run:

```text
python main.py
```

5. Use the Arrow Keys to move the snake.
6. Press SPACE after Game Over to restart.

## Controls

| Key | Action |
|---|---|
| ↑ | Move Up |
| ↓ | Move Down |
| ← | Move Left |
| → | Move Right |
| SPACE | Restart |

## Testing

Open the terminal in the project folder and run:

```text
python test_game.py
```

If the tests pass, the terminal displays:

```text
All Mouse Hunt tests passed.
```

## Project Workflow

Player input → Snake movement → Mouse collision check → Score update → Wall/self collision check → Continue or Game Over.

## Project Structure

```text
Mouse-Hunt/
├── main.py
├── test_game.py
├── README.md
└── statement.md
```

## Note

The game is intentionally kept simple and uses the Python concepts learned in the course, including variables, functions, conditions, loops, lists, random numbers and basic algorithmic problem solving.
