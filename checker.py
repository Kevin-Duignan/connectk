from helpers import *


def end_of_game(board, config):
    """
    Checks if the game has ended with a winner
    or a draw.

    :param board: The game board, 2D list of a rows x b columns.
    :return: 0 if game is not over, the turn of the player that wins, or 101 if it's a draw.
    """

    # * Win Check
    def win(string):
        win_string = ""
        for player in range(1, config["total_players"] + 1):
            for _ in range(config["columns"]):
                if len(win_string) < config["win_pieces"]:
                    win_string += str(player)
            if win_string in string:
                return player

    # * Rows -> Strings
    for row in board:
        row_str = "".join([str(i) for i in row])
        # If there's a win return the winner
        exists = win(row_str)
        if exists:
            return exists

    # To check for draw further down
    filled_slots = True
    # * Columns -> Strings
    for i in range(len(board[0])):  # Length of each row in original board
        column_str = ""
        # Concatenate elements of ith index from each row into a string
        for row in board:
            column_str += str(row[i])
            # If empty spaces then won't be a draw
            if row[i] == 0:
                filled_slots = False
        exists = win(column_str)
        if exists:
            return exists

    # * Diagonals -> Strings
    def diagonal_check(board):
        for col in range(3, len(board[0])):  # 3-6
            # Second half from right-most column down
            if col == 6:
                for row in range(3):  # 0-2
                    diagonal_str = ""
                    i = row
                    j = col
                    while i < col and j >= row:
                        try:
                            diagonal_str += str(board[i][j])
                        except IndexError:
                            pass
                        i += 1
                        j -= 1
                    exists = win(diagonal_str)
                    if exists:
                        return exists
            # First half from left most relevant column
            else:
                diagonal_str = ""
                row = 0
                i = row
                j = col
                # Do this until row and column number are switched
                while i <= col and j >= row:
                    try:
                        diagonal_str += str(board[i][j])
                    except IndexError:
                        pass
                    j -= 1
                    i += 1
                exists = win(diagonal_str)
                if exists:
                    return exists

    # Diagonal /
    exists = diagonal_check(board)
    if exists:
        return exists  # Returning the value from win() to main
    # Diagonal \
    flipped_board = [row for row in reversed(board)]
    exists = diagonal_check(flipped_board)
    if exists:
        return exists

    # * Keep Playing or Draw
    if filled_slots:
        return 101  # All slots are filled so draw
    else:
        return 0  # There are empty slots left so keep playing
