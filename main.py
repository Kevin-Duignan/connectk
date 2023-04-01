from helpers import clear_screen, validate_input
from game import connect4_inputs, connectk_inputs


def main():
    """
    Start program, displays menu which leads to other functions.

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
