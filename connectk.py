import os

# Configuration dictionary for each new game of connect4/connectk
CONFIG = {
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

    :param game: The type of game selected: "4" or "k"
    :return: None
    """
    if game == "4":
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
    elif game == "k":
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


def connectk_inputs():
    connectk_config = CONFIG
    print("=============== Connect K ===============")
    print("1. View Rules")
    print("2. Play Connect K")
    print("3. Exit")
    print("=========================================")
    connectk_option = validate_input(
        "Please select an option [1, 2, 3]: ", ["1", "2", "3"]
    )
    clear_screen()
    if connectk_option == "1":  # Rules
        print_rules("k")
        home_input = validate_input(
            "Please select an option [home, exit]: ", ["home", "exit"]
        )
        if home_input == "home":  # Back to main menu
            main()
        else:  # Exit
            clear_screen()
            exit()
    elif connectk_option == "2":  # Configure game
        connectk_config["rows"] = int(validate_input(
            "Input the number of rows for your board (max 1000): ",
            [str(i) for i in range(1, 1001)],
        ))
        connectk_config["columns"] = int(validate_input(
            "Input the number of columns for your board (max 1000): ",
            [str(i) for i in range(1, 1001)],
        ))
        # Calculate the maximum value a user can input while still making the game valid
        max_input = max(connectk_config["rows"], connectk_config["columns"])
        connectk_config["win_pieces"] = int(validate_input(
            "Input the number of connected pieces needed to win (can't be larger than row and column number): ",
            [
                str(i) for i in range(1, max_input + 1)
            ],  # Valid inputs between 1 and the larger of row and column number
        ))
        connectk_config["human_players"] = int(validate_input(
            "Input the number of human players (total players can't be larger than row and column number): ",
            [str(i) for i in range(0, max_input + 1)],
        ))
        connectk_config["cpu_players"] = int(validate_input(
            "Input the number of CPU players (total players can't be larger than row and column number): ",
            [
                str(i)
                for i in range(0, max_input - connectk_config["human_players"] + 1)
            ],  # CPU players + human players cannot exceed max input
        ))
        for i in range(connectk_config["cpu_players"]):
            level = validate_input(
                f"Input the difficulty level for CPU no. {i + 1}: ",
                ["easy", "medium", "hard"],
            )
            connectk_config["cpu_levels"].append(level)
    else:  # Exit
        clear_screen()
        exit()
    return connectk_config


def connect4_inputs():

    connect4_config = CONFIG
    connect4_config["rows"] = 7
    connect4_config["columns"] = 6
    connect4_config["win_pieces"] = 4

    print("=============== Connect 4 ===============")
    print("1. View Rules")
    print("2. Play a local 2 player game")
    print("3. Play a game against the computer")
    print("4. Exit")
    print("=========================================")

    connect4_option = validate_input(
        "Please select an option [1, 2, 3, 4]: ", ["1", "2", "3", "4"]
    )
    clear_screen()
    if connect4_option == "1":  # Rules
        print_rules("4")
        home_input = validate_input(
            "Please select an option [home, exit]: ", ["home", "exit"]
        )
        if home_input == "home":  # Back to main menu
            main()
        else:  # Exit
            clear_screen()
            exit()
    elif connect4_option == "2":  # Local game
        connect4_config["human_players"] = 2
        connect4_config["cpu_players"] = 0
    elif connect4_option == "3":  # Human vs CPU
        connect4_config["human_players"] = 1
        connect4_config["cpu_players"] = 1
        difficulty = validate_input(
            "Please select a difficulty from [easy, medium, hard]: ",
            ["easy", "medium", "hard"],
        )
        connect4_config["cpu_levels"].append(difficulty)
    else:  # Exit
        clear_screen()
        exit()
    return connect4_config


def main():
    """
    At the start of a game of Connectk, the user inputs:
            - The number of rows of the game board,
            - The number of columns of the game board,
            - The number k of tokens that need to be connected in order to win,
            - The number of human players,
            - The number and level of CPU players.
    :return: None
    """
    clear_screen()

    print("============= Main Menu =============")
    print("1. Connect K")
    print("2. Connect 4")
    print("3. Exit")
    print("=====================================")

    menu_option = validate_input("Please select an option [1, 2, 3]: ", ["1", "2", "3"])
    clear_screen()
    if menu_option == "1":
        connectk_config = connectk_inputs()
        print(connectk_config)
    elif menu_option == "2":
        connect4_config = connect4_inputs()
        print(connect4_config)

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
    ] # List of lists filled with 0
    return board
if __name__ == "__main__":
    main()
