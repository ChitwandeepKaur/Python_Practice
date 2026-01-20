# Car Game

A simple interactive Python command-line game that simulates car engine operations. Control a virtual car by starting and stopping its engine using text commands.

## How to Play

1. Run the program with `python main.py`
2. Enter commands to interact with the car
3. Available commands:
   - **start** - Start the car engine (only works if car is stopped)
   - **stop** - Stop the car engine (only works if car is already started)
   - **help** - Display all available commands
   - **exit** - Exit the game

## Game Features

- Interactive command-line interface
- Car state management (started/stopped)
- Input validation with user-friendly error messages
- Help command to display available actions
- Prevents invalid state transitions (e.g., can't start an already running car)

## Requirements

- Python 3.x

## Skills Learned/Acquired

- Understanding and implementing basic Python syntax
- Handling user input and output in a command-line interface
- Managing program state using variables and conditional logic
- Writing user-friendly error messages and input validation
- Structuring a simple interactive program
- Using loops to maintain program flow