# Project Statement

## Problem Statement

Simple beginner games can be used to understand programming concepts such as input, conditions, loops, functions, lists, collision checking and score calculation. The purpose of Mouse Hunt is to create a small interactive Python game that demonstrates these concepts in a practical way.

## Scope

The project focuses on a single-player snake-style game. The player controls a snake, catches randomly placed mice, earns points, and tries to avoid the game boundaries and the snake's own body.

The project does not use a database, online services or external game engines.

## Target Users

The project is intended for:

- Beginner Python learners
- First-year engineering students
- Users who want a simple keyboard-controlled game

## High-Level Features

1. Snake movement using arrow keys.
2. Random mouse placement.
3. Score and high-score tracking.
4. Snake growth after catching a mouse.
5. Wall collision detection.
6. Self-collision detection.
7. Game-over display.
8. Restart using the SPACE key.

## Functional Modules

### 1. Player Control
Takes keyboard input and changes the snake's direction.

### 2. Mouse and Scoring
Creates the mouse at a random position and increases the score when the snake catches it.

### 3. Collision and Game State
Checks wall and self collision and displays Game Over when necessary.

## Inputs

- Arrow keys for movement
- SPACE key for restart

## Outputs

- Snake movement
- Mouse position
- Current score
- High score
- Game Over message

## Non-Functional Requirements

- Usability: Controls should be simple and easy to understand.
- Performance: The game should respond smoothly to keyboard input.
- Reliability: Collision and scoring rules should work consistently.
- Maintainability: The code should use simple functions and clear comments.
- Resource Efficiency: The project uses only Python built-in modules.

## Future Enhancements

- Sound effects
- Multiple difficulty levels
- More obstacles
- Pause option
- Additional game themes
