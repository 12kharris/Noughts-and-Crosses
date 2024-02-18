
class Board:
    """
    Initialise the size of the board depending on user input
    """
    def __init__(self, board_size):
        self.board_size = board_size
        self.board = []
        
        #loop through the rows
        for i in range(board_size):
            board_line = []
            #loop through the columns
            for j in range(board_size):
                board_line.append((i * board_size) + j)
            
            self.board.append(board_line)

def draw_board(board, board_size):
    for i in range(board_size):
        print("     |"*board_size)
        for j in range(board_size):
            if (board[i][j] < 10):
                print(f"  {board[i][j]}  |", end="")
            else:
                print(f"  {board[i][j]} |", end="")
        print("\n" + "     |"*board_size)
        if(i != board_size - 1):
            print("-----|"*board_size)
    
def validate_board_size(board_input):
    try:
        board_size = int(board_input)
        if (board_size > 9):
            print("Maximum board size is 9x9. Be sensible")
            return False
        elif(board_size < 3):
            print("Minimum board size is 3x3.")
            return False
        return True
    except:
        print("Please enter a whole number")
        return False


print("Welcome to Noughts and Crosses!\n")

valid_board = False
while(not valid_board):
    board_input = input("Please enter how large you want the board to be (minimum 3, maximum 9) - ")
    valid_board = validate_board_size(board_input)

board = Board(int(board_input))
draw_board(board.board, board.board_size)
