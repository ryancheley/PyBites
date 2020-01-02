WHITE, BLACK = ' ', '#'


def create_chessboard(size=8):
    """Create a chessboard with of the size passed in.
       Don't return anything, print the output to stdout"""
    board = ''
    for r in range(size):
        for s in range(size):
            if s % 2 == 0 and r % 2 == 0:
                board = board + WHITE
            elif s % 2 == 1 and r % 2 == 1:
                board = board + WHITE
            else:
                board = board + BLACK
        board = board + '\n'
    print(board)




c = create_chessboard(32)