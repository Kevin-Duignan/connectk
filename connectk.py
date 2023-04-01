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
		enter = input(prompt)
		if enter in valid_inputs:
			return enter
		else:
			print("Invalid inputs, please try again.")
			pass

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
	pass