import os

# Configuration dictionary for each new game of connect4/connectk
CONFIG = {
    "rows": None,
    "columns": None,
    "win_pieces": None,  # How many pieces need to be connected in order to win
    "human_players": None,  # No. of human players
    "cpu_players": None,  # No. of CPUs
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
        print("=========================================")
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
    pass


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
    if connect4_option == "1":  # Rules
        clear_screen()
        print_rules("4")
        home_input = validate_input(
            "Please select an option [home, exit]: ", ["home", "exit"]
        )
        if home_input == "home":  # Back to main menu
            main()
        elif home_input == "exit":  # Exit
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
    print("1. Play Connect K")
    print("2. Play Connect 4")
    print("3. Exit")
    print("=====================================")

    menu_option = validate_input("Please select an option [1, 2, 3]: ", ["1", "2", "3"])

    if menu_option == "1":
        # connectk_config = connectk_inputs()
        pass

    elif menu_option == "2":
        clear_screen()
        connect4_config = connect4_inputs()
        print(connect4_config)


if __name__ == "__main__":
    main()