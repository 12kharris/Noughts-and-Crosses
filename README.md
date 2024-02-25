# Noughts and Crosses

Noughts and Crosses is a python command line interface (CLI) program where a user can play against a computer at the classic game of the same name. The aim of the game is to take turns placing your symbol (either an 'O' or 'X') on the board with the aim of creating a whole line on the board (including diagonal) with your symbol. The game is normally played on a 3x3 grid but the user can choose a grid size between 3x3 and 9x9.


![Responsive Mockup]()

## Features 

### Existing Features

- __Choose a Board Size__

  - The user can choose a board size between 3x3 and 9x9.
  - The board will be created and displayed with the given dimensions using only one function in the code. 
  ![different board sizes]()

- __Validate User Input__
  - The user must enter an integer which corresponds to the square on the board where they would like their symbol to be placed. 
  - If the user inputs an invalid placement (such as a number off the board or a non-numeric) or the place the user has chosen is already occupied, a message will display describing the issue and the user will be prompted to try again.
  ![invalid user input]()

- __The Computer Player__
  - The user plays against the computer (or CPU)
  - The CPU has no strategy, and operates by selecting a random place on the board to place their marker. This is an area which could be improved in the future.

- __The End Condition__
  - If one of the players creates a line of the board of their markers then they are the winner.
  - A win message displays for the victorious player in the event there is a winner
  - The game can also end when both players have filled up the entire board and no one managed to create a line of their marker. 
  - In the above case, a draw message will be displayed, as well as the final state of the board.
  ![various end conditions]()


### Features Left to Implement

- Currently, the game is only 1 player. Allowing for 2 human players would be the next step for development.
- The CPU player is very unsophisticated. Having some scoring system where the CPU can look at all possible marker placements and rank them based off of which is the most advantageous would give the player some more challenge.
- The CPU player also is not aware of the win condition which is shown blatently to the player in the event they have 2 markers in a line and the CPU does not block their line completion. Programming the CPU player to be more aware of the current state of the board, in combination with the previous point, would make the game more engaging.
- Instead of using the CLI, a graphical display would allow for better differentiation between the player markers and the board square numbers. This would also open the door for using the mouse to select where to place a marker.


## Development Process
- Before beginning the development process, a flow chart of the application flow and key logical steps was created to provide a clear structure for the program.
- The first step of development was getting a 3x3 board to display in the terminal and then adding the functionality to make a board of any size display without having to hard code different board sizes into the print statements.
- The next step was adding the ability to choose a number on the board and have the board update the display with the chosen square now containing the counter.
- After this was successful, validating the user input was the next step.
- Once a single user could only choose valid placements, the CPU player was added.
- The final major development step was to create the logic to check if one of the players had one the game, or if it was a draw.
- Beyond this, various refactoring and comments were the final steps in development.


## Deployment Process

The site was deployed using Heroku. The live link can be found here - https://noughts-and-crosses-204025256cf6.herokuapp.com/


### Deployment Steps
- Use the command "pip3 freeze > requirements.txt" to add all dependencies to the requirements.txt file.
- Push all changes to GitHub.
Create a new app on Heroku and on the settings tab, add a config var with the key "PORT" and the value "8000".
- Deploy the desired branch.


## Testing 

All possible cases for a win were tested. These being a win with a vertical line in each column, a win with a horizontal line on each row and finally a win with both diagonal directions. These win cases were tested for both the player and the CPU (with great difficulty as the CPU would randomly select their marker placement).

Invalid board placements were tested such as an already occupied square, a number beyond the scope of the board and non-integers. In all cases, the user was promted to enter again.


### Validator Testing 



## Credits 

- Using a set to get the unique characters on a line on the board was influenced by the following Stack Overflow post - https://stackoverflow.com/questions/12897374/get-unique-values-from-a-list-in-python
- The Code Institute Python Essentials Template was used for this project - https://github.com/Code-Institute-Org/p3-template