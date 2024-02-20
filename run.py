import random as rand

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
            #If the number in the board has 1 digit
            if (len(str(board[i][j])) < 2):
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

def validate_and_place_counter(marker_pos, board, player_symbol, player_1):
    try:
        user_pos = int(marker_pos)
        board_row = user_pos // board.board_size
        board_col = user_pos % board.board_size

        if (board.board[board_row][board_col] != "O" and board.board[board_row][board_col] != "X"):
            board.board[board_row][board_col] = player_symbol
            return True
        else:
            if (player_1):
                print("Chosen selection is already occupied. Please choose an unnoccupied number")
            return False
    except:
        print("Please enter a whole number on the board where you would like to place your marker")
        return False

def check_winner(board, board_size):
    #credit to https://stackoverflow.com/questions/12897374/get-unique-values-from-a-list-in-python
    #for how to get unique items in a list

    #horizontal check   
    for i in range(board_size):
        horizontal_values = []
        for j in range(board_size):
            horizontal_values.append(board[i][j])
        horizontal_unq = set(horizontal_values)
        if (len(horizontal_unq) == 1): # a set contains unique values. So if there is only 1 value, the line is complete
            return True

    #vertical check    
    for i in range(board_size):
        vertical_values = []
        for j in range(board_size):
            vertical_values.append(board[j][i])
        vertical_unq = set(vertical_values)
        if (len(vertical_unq) == 1):
            return True

    #diagonal check top L to bottom R
    diagonal_LR_values = []
    for i in range(board_size):
        diagonal_LR_values.append(board[i][i])
    diagonal_LR_unq = set(diagonal_LR_values)
    if(len(diagonal_LR_unq) == 1):
        return True

    #diagonal check top R to bottom L
    diagonal_RL_values = []
    for i in range(board_size):
        diagonal_RL_values.append(board[i][board_size - 1 - i])
    diagonal_RL_unq = set(diagonal_RL_values)
    if(len(diagonal_RL_unq) == 1):
        return True

    return False

def main():

    print("Welcome to Noughts and Crosses!\n")
    valid_board = False
    while(not valid_board):
        board_input = input("Please enter how large you want the board to be (minimum 3, maximum 9) - ")
        valid_board = validate_board_size(board_input)
    board = Board(int(board_input))  
    draw_board(board.board, board.board_size)

    player = True
    counters_placed = 0

    #While there are still unnoccupied spaces on the board
    while (counters_placed < board.board_size**2):
        player_symbol = ""
        valid_placement = False
        
        if (player):
            player_symbol = "O"
            while (not valid_placement):
                marker_pos = input("\nPlease choose the number on the board where you want your marker to be placed - ")
                valid_placement = validate_and_place_counter(marker_pos, board, player_symbol, player)
        else:
            player_symbol = "X"
            while (not valid_placement):
                marker_pos = rand.randint(0, board.board_size**2 - 1)
                valid_placement = validate_and_place_counter(marker_pos, board, player_symbol, player)
            draw_board(board.board, board.board_size)
            print(f"\nComputer chose - {marker_pos}")
            
        if(check_winner(board.board, board.board_size)):
            draw_board(board.board, board.board_size)
            if (player):
                print("\nCongratulations! You win!")
            else:
                print("\nComputer wins!")
            return
        
        player = not player
        counters_placed += 1

    draw_board(board.board, board.board_size)
    print("No more spaces on the board. It's a draw!")
            

        
    


     


main()
