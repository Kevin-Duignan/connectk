from helpers import *
from checker import end_of_game
from cpus import *


def run_game(board, config):
    """
    Executes the logic needed to run a game of ConnectK
    """

    if config["game"] == "connect4":
        pass  # Much easier to implement
    elif config["game"] == "connectk":
        # Order of players and player type
        order = {}

        if config["first_turn"] == "humans":
            for turn in range(1, config["total_players"] + 1):
                if turn <= config["human_players"]:  # Turns starting at 1
                    order[turn] = "human"
                else:  # For cpu turns
                    cpu_turn = (
                        turn - config["human_players"] - 1
                    )  # Starting from 0 to compute difficulty for each cpu
                    order[turn] = config["cpu_levels"][cpu_turn]
        elif config["first_turn"] == "cpus":
            for turn in range(1, config["total_players"] + 1):
                if turn <= config["cpu_players"]:
                    order[turn] = config["cpu_levels"][
                        turn - 1
                    ]  # Each turn that is a cpu will have a difficulty attached to it
                else:  # Human cpus
                    order[turn] = "human"
        else:  # Randomized order
            cpu_turn = 0
            human_turn = 0
            for turn in range(1, config["total_players"] + 1):
                is_human_turn = random.choice([True, False])
                if is_human_turn and human_turn < config["human_players"]:
                    order[turn] = "human"
                    human_turn += 1
                elif cpu_turn < config["cpu_players"]:  # CPU turn
                    order[turn] = config["cpu_levels"][cpu_turn]
                    cpu_turn += 1
                else:  # Human turn anyway if cpus all cpus are assigned a turn
                    order[turn] = "human"
                    cpu_turn += 1

        # Go through order
        while True:
            clear_screen()
            game_status = end_of_game(board, config)
            if game_status == 0:
                for turn in range(1, config["total_players"]):
                    print_board(board, config)
                    if order[turn] == "human":
                        print(f"Your move, Player {turn}!")
                        move = execute_player_turn(turn, board)
                    elif order[turn] == "easy":
                        print(
                            f"It's Player {turn}'s turn, this one might get lucky..."
                        )
                        move = cpu_player_easy(board, turn, config)
                    elif order[turn] == "medium":
                        print(
                            f"It's Player {turn}'s turn, don't underestimate them!"
                        )
                        move = cpu_player_medium(board, turn, config)
                    else:  # cpu hard
                        print(
                            f"It's Player {turn}'s turn, think you can beat them? Think again"
                        )
                        move = cpu_player_hard(board, turn, config)
                    # drop_piece(board, turn, move)
                    print(f"Player {turn}'s move was {move}")
            # If game is over
            else:
                break
        if game_status == 101:
            print("It's a draw!")
        else:
            print(f"Player {game_status} wins!")

board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

run_game(config={
    "game": "connectk",  # ["connect4", "connectk"]
    "rows": 9,
    "columns": 10,
    "win_pieces": 5,  # How many pieces need to be connected in order to win
    "human_players": 3,  # No. of human players
    "cpu_players": 3,  # No. of CPUs
    "total_players": 6,
    "cpu_levels": ["easy", "medium", "hard"],  # List of length cpu_players with a difficulty in ["easy", "medium", "hard"] for each cpu
    "first_turn": ["humans"],
})