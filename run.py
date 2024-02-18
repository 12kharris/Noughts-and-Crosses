
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


def validate_board_size(board_input):
    try:
        board_size = int(board_input)
        return True
    except:
        print("Please enter a whole number")
        return False


print("Welcome to Noughts and Crosses!\n")

valid_board = False
while(not valid_board):
    board_input = input("Please enter how large you want the board to be (minimum 3) - ")
    valid_board = validate_board_size(board_input)

board = Board(5)
print(board.board)
