from helpers import *
from main import main


def connectk_inputs():

    connectk_config = CONFIG
    connectk_config["game"] += "connectk"

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
        print_rules(connectk_config["game"])
        home_input = validate_input(
            "Please select an option [home, exit]: ", ["home", "exit"]
        )
        if home_input == "home":  # Back to main menu
            main()
        else:  # Exit
            clear_screen()
            exit()

    elif connectk_option == "2":  # Configure game
        connectk_config["rows"] = int(
            validate_input(
                "Input the number of rows for your board (max 100, min 2): ",
                [str(i) for i in range(2, 101)],
            )
        )
        connectk_config["columns"] = int(
            validate_input(
                "Input the number of columns for your board (max 100, min 2): ",
                [str(i) for i in range(2, 101)],
            )
        )
        # Calculate the maximum value a user can input while still making the game valid
        max_input = max(connectk_config["rows"], connectk_config["columns"])
        connectk_config["win_pieces"] = int(
            validate_input(
                "Input the number of connected pieces needed to win (can't be larger than row and column number): ",
                [
                    str(i) for i in range(1, max_input + 1)
                ],  # Valid inputs between 1 and the larger of row and column number
            )
        )
        connectk_config["human_players"] = int(
            validate_input(
                "Input the number of human players (total players can't be larger than row and column number, or lower than 2): ",
                [str(i) for i in range(0, max_input + 1)],
            )
        )
        if connectk_config["human_players"] == 0:
            min_cpus = 2
        elif connectk_config["human_players"] == 1:
            min_cpus = 1
        else:
            min_cpus = 0
        connectk_config["cpu_players"] = int(
            validate_input(
                "Input the number of CPU players (total players can't be larger than row and column number, or lower than 2): ",
                [
                    str(i)
                    for i in range(
                        min_cpus, max_input - connectk_config["human_players"] + 1
                    )
                ],  # CPU players + human players cannot exceed max input
            )
        )
        connectk_config["total_players"] = connectk_config["cpu_players"] + connectk_config["human_players"]
        for i in range(connectk_config["cpu_players"]):
            level = validate_input(
                f"Input the difficulty level for CPU no. {i + 1}: ",
                ["easy", "medium", "hard"],
            )
            connectk_config["cpu_levels"].append(level)
        connectk_config["first_turn"] = validate_input(
            "Input which player type you want to begin the game from [humans, cpus, mix]: ",
            ["humans, cpus, mix"],
        )
    else:  # Exit
        clear_screen()
        exit()
    return connectk_config


def connect4_inputs():

    connect4_config = CONFIG
    connect4_config["game"] += "connect4"
    connect4_config["rows"] = 7
    connect4_config["columns"] = 6
    connect4_config["win_pieces"] = 4
    connect4_config["total_players"] = 2

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
