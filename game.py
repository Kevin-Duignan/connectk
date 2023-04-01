import random
from helpers import *
from checker import end_of_game
from cpus import *

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
                f"Input the difficulty level for CPU no. {i + 1} from [easy, medium, hard]: ",
                ["easy", "medium", "hard"],
            )
            connectk_config["cpu_levels"].append(level)
        connectk_config["first_turn"] = validate_input(
            "Input which player type you want to begin the game from [humans, cpus, randomized]: ",
            ["humans", "cpus", "randomized"],
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
        connect4_config["first_turn"] = validate_input("Please choose which player type will go first from [humans, cpus, randomized]: ", ["humans, cpus, randomized"])

    else:  # Exit
        clear_screen()
        exit()
    return connect4_config

def run_game(config):
    """
    Executes the logic needed to run a game of ConnectK
    """
    board = create_board(config["rows"], config["columns"])
    
    if config["game"] == "connect4":
        pass # Much easier to implement
    elif config["game"] == "connectk":
        # Order of players and player type
        order = {}
        
        if config["first_turn"] == "humans":
            for turn in range(1, config["total_players"] + 1):
                if turn <= config["human_players"]: # Turns starting at 1
                    order[turn] = "human"
                else: # For cpu turns
                    cpu_turn = turn - config["human_players"] # Starting from 0 to compute difficulty for each cpu
                    order[turn] = config["cpu_levels"][cpu_turn]
        elif config["first_turn"] == "cpus":
            for turn in range(config["total_players"]):
                if turn <= config["cpu_players"]:
                    order[turn] = config["cpu_levels"][cpu_turn] # Each turn that is a cpu will have a difficulty attached to it
                else: # Human cpus
                    order[turn] = "human"
        else: # Randomized order
            cpu_turn = 0
            human_turn = 0
            for turn in range(1, config["total_players"] + 1):
                is_human_turn = random.randint(1,2)
                if is_human_turn and human_turn < config["human_players"]:
                    order[turn] = "human"
                    human_turn += 1
                elif cpu_turn < config["cpu_players"]: # CPU turn
                    order[turn] = config["cpu_levels"][cpu_turn]
                    cpu_turn += 1
                else: # Human turn anyway if cpus all cpus are assigned a turn
                    order[turn] = "human"
                    cpu_turn += 1
            
            # Go through order
            while True:
                clear_screen()
                print_board(board)
                game_status = end_of_game(board, config)
                if game_status == 0:
                    for turn in range(1, config["total_players"]):
                        if order[turn] == "human":
                            print(f"Your move, Player {turn}!")
                            move = execute_player_turn(turn, board)
                        elif order[turn] == "easy":
                            print(f"It's Player {turn}'s turn, this one might get lucky...")
                            move = cpu_player_easy(board, turn, config)
                        elif order[turn] == "medium":
                            print(f"It's Player {turn}'s turn, don't underestimate them!")
                            move = cpu_player_medium(board, turn, config)
                        else: # cpu hard
                            print(f"It's Player {turn}'s turn, think you can beat them? Think again")
                            move = cpu_player_hard(board, turn, config)
                        print(f"Player {turn}'s move was {move}")    
                # If game is over
                else:
                    break
            if game_status == 101:
                print("It's a draw!")
            else:
                print(f"Player {game_status} wins!")
                