from helpers import clear_screen, validate_input
from game import connect4_inputs, connectk_inputs


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
    else:
        clear_screen()
        exit()


if __name__ == "__main__":
    main()
