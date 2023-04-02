from helpers import drop_piece
from checker import end_of_game
import random


def cpu_player_easy(board, player, config):
    """
    Executes a move for the CPU on easy difficulty. This function
    plays a randomly selected column.

    :param board: The game board, 2D list of RxC dimensions.
    :param player: The player whose turn it is, integer value between 2 and 100.
    :return: Column that the piece was dropped into, int.
    """
    # Implement your solution below
    while True:
        random_column = random.randint(1, config["columns"])
        if drop_piece(board, player, random_column):
            return random_column


def cpu_player_medium(board, cpu_player, config):
    """
    Executes a move for the CPU on medium difficulty.
    It first checks for an immediate win and plays that move if possible.
    If no immediate win is possible, it checks for an immediate win
    for the opponent and blocks that move. If neither of these are
    possible, it plays a random move.

    :param board: The game board, 2D list of RxC dimensions.
    :param player: The player whose turn it is, integer value of 1 or 2.
    :return: Column that the piece was dropped into, int.
    """

    # Check for any possibility of win
    for col_index in range(len(board[0])):
        cpu_move = col_index + 1
        new_board = [row[:] for row in board]
        if drop_piece(new_board, cpu_player, cpu_move):  # Simulate drop for self
            if end_of_game(new_board, config) == cpu_player:
                drop_piece(board, cpu_player, cpu_move)  # Do a real drop
                return cpu_move

    # Check for any possibility of loss
    for opponent in range(1, config["total_players"] + 1):
        for col_index in range(len(board[0])):
            opponent_move = col_index + 1
            new_board = [row[:] for row in board]
            if drop_piece(
                new_board, opponent, opponent_move
            ):  # Simulate drop for opponent
                if (
                    end_of_game(new_board, config) == opponent
                ):  # If that drop wins for the opponent
                    cpu_move = opponent_move
                    drop_piece(
                        board, cpu_player, cpu_move
                    )  # Block that drop with cpu move
                    return cpu_move

    # If no move to block or win
    while True:
        cpu_move = random.randrange(1, config["columns"])  # random place to drop
        if drop_piece(board, cpu_player, cpu_move):
            return cpu_move


def cpu_player_hard(board, player, config):
    # Configure cpu hard to be the same as cpu medium for now
    return cpu_player_medium(board, player, config)
