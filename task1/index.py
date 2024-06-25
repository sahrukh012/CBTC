import random

def play_rock_paper_scissors():
  """
  Plays a round of rock-paper-scissors against the computer.

  Returns:
      str: A message indicating the winner or a tie.
  """

  # Get user input (ensure case-insensitive)
  while True:
    user_choice = input("Choose Rock, Paper, or Scissors (case-insensitive): ").lower()
    if user_choice in ("rock", "paper", "scissors"):
      break
    else:
      print("Invalid choice. Please try again.")

  # Generate computer's choice
  computer_choice = random.choice(["rock", "paper", "scissors"])

  # Determine winner
  if user_choice == computer_choice:
    return f"It's a tie! Both players chose {user_choice}."
  elif (user_choice == "rock" and computer_choice == "scissors") or \
       (user_choice == "paper" and computer_choice == "rock") or \
       (user_choice == "scissors" and computer_choice == "paper"):
    return f"You win! {user_choice.capitalize()} beats {computer_choice}."
  else:
    return f"You lose! {computer_choice.capitalize()} beats {user_choice}."

# Play the game
print(play_rock_paper_scissors())

# Optionally, ask if the user wants to play again
while True:
  play_again = input("Do you want to play again? (y/n): ").lower()
  if play_again in ("y", "yes"):
    print(play_rock_paper_scissors())
  elif play_again in ("n", "no"):
    print("Thanks for playing!")
    break
  else:
    print("Invalid input. Please enter 'y' or 'n'.")
