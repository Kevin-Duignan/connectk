import os

# Configuration dictionary for each new game of connect4/connectk
CONFIG = {
    "game": "",  # ["connect4", "connectk"]
    "rows": 0,
    "columns": 0,
    "win_pieces": 0,  # How many pieces need to be connected in order to win
    "human_players": 0,  # No. of human players
    "cpu_players": 0,  # No. of CPUs
    "total_players": 0,
    "cpu_levels": [],  # List of length cpu_players with a difficulty in ["easy", "medium", "hard"] for each cpu
    "first_turn": [],  # ["humans", "cpus", "mix"]
}


def clear_screen():
    # Command for clearing the terminal line
    os.system("cls" if os.name == "nt" else "clear")


def validate_input(prompt, valid_inputs):
    """
    Repeatedly ask user for input until they enter an input
    within a set valid of options.

    :param prompt: The prompt to display to the user, string.
    :param valid_inputs: The range of values to accept, list
    :return: The user's input, string.
    """
    while True:

        user_input = input(prompt)
        if user_input in valid_inputs:
            return user_input
        else:
            print("Invalid inputs, please try again.")
            pass


def print_rules(game):
    """
    Prints the rules of the game.

    :param game: The type of game selected: "connect4" or "connectk"
    :return: None
    """
    if game == "connect4":
        print("================= Rules =================")
        print("Connect 4 is a two-player game where the")
        print("objective is to get four of your pieces")
        print("in a row either horizontally, vertically")
        print("or diagonally. The game is played on a")
        print("6x7 grid. The first player to get four")
        print("pieces in a row wins the game. If the")
        print("grid is filled and no player has won,")
        print("the game is a draw.")
        print("========================================")
    elif game == "connectk":
        print("================= Rules ======================")
        print("** Please read the rules of Connect 4 first **")
        print("Connect K runs on the same basis of connect 4,")
        print("but you get to choose how hard the game is!")
        print("You can choose the:")
        print("- The number of rows of the game board")
        print("- The number of columns of the game board")
        print("- The number of pieces that need to be")
        print("  connected in order to win")
        print("- The number of human players")
        print("- The number and level of CPU players")
        print("=============================================")


def create_board(rows, columns):

    """
    Returns a 2D list of {rows} rows and {columns} columns to represent
    the game board. Default cell value is 0.

    :param rows: The configured number of rows
    :param columns: The configured number of columns
    :return: A 2D list of 6x7 dimensions.
    """
    board = [
        [0 for _ in range(columns)] for _ in range(rows)
    ]  # List of lists filled with 0
    return board


def print_board(board, config):
    """
    Prints the game board to the console.

    :param board: The game board, 2D list of column x row dimensions.
    :param config: The configuration dictionary of the current game.
    :return: None
    """
    rows = config["rows"]
    columns = config["columns"]

    if config["game"] == "connect4":  # 6x7 board
        # Board layout
        print("========== Connect4 =========")
        print("Player 1: X       Player 2: O\n")
        print("  1   2   3   4   5   6   7")
        print(" --- --- --- --- --- --- ---")
        for row in range(rows):
            print("|", end="")
            for col in range(columns):
                if board[row][col] == 1:
                    print(" X |", end="")
                elif board[row][col] == 2:
                    print(" O |", end="")
                elif board[row][col] == 0:
                    print("   |", end="")
            print("\n --- --- --- --- --- --- ---")
        print("=============================")

    else:  # Connect K
        # To keep alignment
        game_name = " ConnectK " if columns % 2 == 1 else " Connect K "
        # Double line is used to compute length of all other lines
        double_line = ""
        player_count = config["human_players"] + config["cpu_players"]
        player_symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i in range(columns):
            if i == 0 and columns % 2 == 1:
                double_line += "====="
            else:
                double_line += "===="
        double_line += "="
        # Always even so always return an int
        partial_line = double_line[: int((len(double_line) / 2) - (len(game_name) / 2))]
        player_line = "| Players: "

        # Use alphabetical letters as symbols for first 26 players and use the player number for the rest
        for i in range(player_count):
            if i < 26:
                player_line += player_symbols[i]
            else:
                player_line += i

            # Add commas if not last player
            if i != player_count - 1:
                player_line += ", "
            else:
                for i in range(len(player_line), len(double_line)):
                    if i == len(double_line) - 1:
                        player_line += "|"
                    else:
                        player_line += " "

        single_line = double_line.replace("=", "-")

        # Start with two spaces to account for left line going down
        column_numbers = "  "
        column = 1
        for i in range(len(double_line)):
            if column > columns:
                break
            elif i % 4 == 0:  # Spacing between numbers necessary
                column_numbers += str(column)
                column += 1
            elif column <= 9:
                column_numbers += " "
            else:  # Double digits
                if (i + 1) % 4 == 0:
                    # Remove last space to account for extra digit
                    continue
                else:
                    column_numbers += " "

        dotted_line = ""
        for i in range(
            len(double_line) - 1
        ):  # -1 because last column should always be 0
            if i == 0 or i % 4 == 0:
                dotted_line += " "
            else:
                dotted_line += "-"

        print(partial_line, end="")
        print(game_name, end="")
        print(partial_line)

        print(player_line)
        print(single_line)
        print(column_numbers)
        print(dotted_line)
        for row in range(rows):
            print("|", end="")
            for column in range(columns):
                if board[row][column] == 0:
                    print("   |", end="")
                elif board[row][column] <= 26:
                    print(f" {player_symbols[board[row][column] - 1]} |", end="")
                else:
                    print(f" {board[row][column]}|", end="")
            print("\n" + dotted_line)
        print(double_line)


def drop_piece(board, player, column):
    """
    Drops a piece into the game board in the given column.
    Please note that this function expects the column index
    to start at 1.

    :param board: The game board, 2D list of rows x columns dimensions.
    :param player: The player dropping the piece, int.
    :param column: The index of column to drop the piece into, int.
    :return: True if piece was successfully dropped, False if not.
    """
    # Iterate through board from bottom up
    if 1 <= column <= len(board[0]):
        for row in reversed(board):
            # Drop player piece in the lowest free space
            if row[column - 1] == 0:  # Column is 1 indexed
                row[column - 1] = player
                return True
    # If all spaces are filled
    return False


def execute_player_turn(player, board):
    """
    Prompts user for a legal move given the current game board
    and executes the move.

    :return: Column that the piece was dropped into, int.
    """
    while True:
        column = int(
            validate_input(
                f"Player {player}, please enter the column that you would like to drop your piece into: ",
                [str(i) for i in range(1, len(board[0]) + 1)],
            )
        )
        if drop_piece(board, player, column):
            return column
        else:
            print("Invalid move, try again.")
