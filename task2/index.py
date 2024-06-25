import random

def generate_code(num_digits, colors):
  """Generates a secret code with specified number of digits and colors."""
  return [random.choice(colors) for _ in range(num_digits)]

def get_guess(num_digits):
  """Gets a guess from the player with specified number of digits."""
  while True:
    guess = input("Enter your guess ({} digits): ".format(num_digits))
    if len(guess) != num_digits or not all(char.isdigit() for char in guess):
      print("Invalid guess. Please enter a {}-digit number.".format(num_digits))
    else:
      return [int(char) for char in guess]

def get_feedback(code, guess):
  """Provides feedback on the guess based on the secret code."""
  black_pegs = 0  # Correct digit in the correct position
  white_pegs = 0  # Correct digit in the wrong position
  used_colors_in_code = set(code)
  for i in range(len(code)):
    if code[i] == guess[i]:
      black_pegs += 1
      used_colors_in_code.remove(code[i])
  for i in range(len(guess)):
    if guess[i] in used_colors_in_code:
      white_pegs += 1
      used_colors_in_code.remove(guess[i])
  return black_pegs, white_pegs

def play_game(num_digits, colors):
  """Manages the gameplay for two players."""
  # Player 1 sets the code
  player1_code = generate_code(num_digits, colors)
  print("Player 1 has set the code. Player 2, guess the code!")

  # Player 2 guesses
  player2_guesses = 0
  while True:
    player2_guess = get_guess(num_digits)
    black_pegs, white_pegs = get_feedback(player1_code, player2_guess)
    player2_guesses += 1
    print("Black pegs: {}, White pegs: {}".format(black_pegs, white_pegs))
    if black_pegs == num_digits:
      print("Player 2 cracked the code in {} guesses! You win!".format(player2_guesses))
      break

  # Swap roles and play again
  print("\nNext round! Player 2 sets the code.")
  player2_code = generate_code(num_digits, colors)
  print("Player 1, guess the code!")

  # Player 1 guesses
  player1_guesses = 0
  while True:
    player1_guess = get_guess(num_digits)
    black_pegs, white_pegs = get_feedback(player2_code, player1_guess)
    player1_guesses += 1
    print("Black pegs: {}, White pegs: {}".format(black_pegs, white_pegs))
    if black_pegs == num_digits:
      print("Player 1 cracked the code in {} guesses! You win!".format(player1_guesses))
      if player1_guesses < player2_guesses:
        print("Player 1 also wins the overall game by cracking the code faster!")
      else:
        print("It's a tie overall!")
      break

# Example usage (modify num_digits and colors as needed)
num_digits = 4
colors = range(1, 7)  # 6 colors (1 to 6)
play_game(num_digits, colors)
