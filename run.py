import random as rand


class Board:
    """
    Initialise the size of the board depending on user input
    """
    def __init__(self, board_size):
        self.board_size = board_size
        self.board = []

        # loop through the rows
        for i in range(board_size):
            board_line = []
            # loop through the columns
            for j in range(board_size):
                board_line.append((i * board_size) + j)

            self.board.append(board_line)


def draw_board(board, board_size):
    """
    Draw the current state of the board
    """
    for i in range(board_size):
        print("     |"*board_size)
        for j in range(board_size):
            # If the number in the board has 1 digit
            if (len(str(board[i][j])) < 2):
                print(f"  {board[i][j]}  |", end="")
            else:
                print(f"  {board[i][j]} |", end="")
        print("\n" + "     |"*board_size)
        if(i != board_size - 1):
            print("-----|"*board_size)


def validate_board_size(board_input):
    """
    Validate that the desired board size is between 3x3 and 9x9
    """
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
    """
    Check if a counter can be placed in the chosen position
    """
    try:
        user_pos = int(marker_pos)
        board_row = user_pos // board.board_size
        board_col = user_pos % board.board_size

        if (user_pos < 0):
            print(
                "Please enter a whole number on the board"
                "where you want to place your marker")
            return False

        if (
            board.board[board_row][board_col] != "O" and
                board.board[board_row][board_col] != "X"):
                    board.board[board_row][board_col] = player_symbol
                    return True
        else:
            if (player_1):
                print(
                    "Chosen selection is already occupied. "
                    "Please choose an unnoccupied number")
            return False
    except:
        print(
            "Please enter a whole number on the board "
            "where you want to place your marker")
        return False


def check_winner(board, board_size):
    """
    Check the current state of the board and if one of the players has won
    """
    # credit to
    # https://stackoverflow.com/questions/12897374/get-unique-values-from-a-list-in-python
    # for using a set for unique counts

    # horizontal check
    for i in range(board_size):
        horizontal_values = set()
        for j in range(board_size):
            horizontal_values.add(board[i][j])
        # a set contains unique values.
        # if there is only 1 value, the line is complete
        if (len(horizontal_values) == 1):
            return True

    # vertical check
    for i in range(board_size):
        vertical_values = set()
        for j in range(board_size):
            vertical_values.add(board[j][i])
        if (len(vertical_values) == 1):
            return True

    # diagonal check top L to bottom R
    diagonal_LR_values = set()
    for i in range(board_size):
        diagonal_LR_values.add(board[i][i])
    if(len(diagonal_LR_values) == 1):
        return True

    # diagonal check top R to bottom L
    diagonal_RL_values = set()
    for i in range(board_size):
        diagonal_RL_values.add(board[i][board_size - 1 - i])
    if(len(diagonal_RL_values) == 1):
        return True

    return False


def run_game_loop(board):
    """
    The main game loop. Runs until win condition met or board filled
    """
    player = True
    counters_placed = 0

    # While there are still unnoccupied spaces on the board
    while (counters_placed < board.board_size**2):
        player_symbol = ""
        valid_placement = False

        if (player):
            player_symbol = "O"
            while (not valid_placement):
                marker_pos = input(
                    "\nPlease choose the number on the board "
                    "where you want your marker to be placed - \n")
                valid_placement = validate_and_place_counter(
                    marker_pos, board, player_symbol, player)
        else:
            player_symbol = "X"
            while (not valid_placement):
                marker_pos = rand.randint(0, board.board_size**2 - 1)
                valid_placement = validate_and_place_counter(
                    marker_pos, board, player_symbol, player)

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

    # fall out of loop when no more spaces on board
    draw_board(board.board, board.board_size)
    print("No more spaces on the board. It's a draw!")


def main():
    print("Welcome to Noughts and Crosses!\n")
    valid_board = False
    while(not valid_board):
        board_input = input(
            "Please enter how large you want the board "
            "to be (minimum 3, maximum 9) - \n")
        valid_board = validate_board_size(board_input)

    board = Board(int(board_input))
    draw_board(board.board, board.board_size)

    run_game_loop(board)


main()
