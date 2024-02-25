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


## Deployment Process



## Testing 

All possible cases for a win were tested. These being a win with a vertical line in each column, a win with a horizontal line on each row and finally a win with both diagonal directions. These win cases were tested for both the player and the CPU (with great difficulty as the CPU would randomly select their marker placement).

Invalid board placements were tested such as an already occupied square, a number beyond the scope of the board and non-integers. In all cases, the user was promted to enter again.


### Validator Testing 

- HTML
    - No errors were returned when passing through the official [W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2F12kharris.github.io%2FGeneral-Knowledge-Quiz%2F)
- CSS
    - No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2F12kharris.github.io%2FGeneral-Knowledge-Quiz%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)
- JavaScript
    - Some warnings were found but the vast majority were due to formatting when passing through the official [Jshint validator](https://jshint.com/)
    - There are 12 functions in this file.
    - Function with the largest signature take 7 arguments, while the median is 0.5.
    - Largest function has 35 statements in it, while the median is 7.5.
    - The most complex function has a cyclomatic complexity value of 12 while the median is 1.5
 

## Deployment

- The site was deployed to GitHub pages.

The live link can be found here - https://12kharris.github.io/General-Knowledge-Quiz/


## Credits 

The use of data types for tracking which answer is correct was inspired from the Code Institute Love Maths walkthrough project. 
The use of conditions in CSS styles was taken from https://stackoverflow.com/questions/26754497/css-disable-hover-effect. 

The additional info for each question was taken from Wikipedia and all info sections have a link to the specific source provided.

Some images were taken from the royalty free website Pixabay https://pixabay.com/ . 
The remaining images were taken from the following sites:
- https://stock.adobe.com/uk/search?k=babylon+garden 
- https://www.istockphoto.com/search/2/image-film?phrase=keratin+protein 
- https://www.reddit.com/r/Cyberpunk/comments/f0yxqt/neuromancer_by_william_gibson_pioneer_of_cyberpunk/ 
- https://en.wikipedia.org/wiki/Krypton 
- https://classicalwisdom.com/mythology/athena-in-ancient-literature/ 