import os

# Configuration dictionary for each new game of connect4/connectk
CONFIG = {
    "game": "",  # ["connect4", "connectk"]
    "rows": 0,
    "columns": 0,
    "win_pieces": 0,  # How many pieces need to be connected in order to win
    "human_players": 0,  # No. of human players
    "cpu_players": 0,  # No. of CPUs
    "cpu_levels": [],  # List of length cpu_players with a difficulty in ["easy", "medium", "hard"] for each cpu
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
