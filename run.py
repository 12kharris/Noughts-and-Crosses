
class Board:

    def __init__(self, board_size):
        self.board_size = board_size
        self.board = []
        
        for i in range(board_size):
            board_line = []
            for j in range(board_size):
                board_line.append((i * 3) + j)
            
            self.board.append(board_line)

board = Board(3)
print(board.board)
