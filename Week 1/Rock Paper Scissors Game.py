import random

def play_rock_paper_scissors():
    """
    Plays a game of Rock, Paper, Scissors between a user and the computer.
    """
    # Define the possible choices
    choices = ["rock", "paper", "scissors"]
    
    # Display welcome message and rules
    print("\n=== ROCK, PAPER, SCISSORS ===")
    print("Rules: Rock crushes Scissors, Scissors cuts Paper, Paper covers Rock\n")
    
    while True:
        # Get the user's choice
        user_choice = input("Enter your choice (rock/paper/scissors) or 'quit' to exit: ").lower().strip()
        
        # Check if the user wants to quit
        if user_choice == 'quit':
            print("Thanks for playing!")
            break
        
        # Validate user input
        if user_choice not in choices:
            print("Invalid choice! Please enter rock, paper, or scissors.")
            continue
        
        # Generate a random choice for the computer
        computer_choice = random.choice(choices)
        
        # Display both choices
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        # Determine the winner
        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            result = "You win!"
        else:
            result = "Computer wins!"
        
        print(result + "\n")
        
        # Ask to play again
        play_again = input("Play again? (yes/no): ").lower().strip()
        if play_again != "yes":
            print("Thanks for playing!")
            break

# Run the game
if __name__ == "__main__":
    play_rock_paper_scissors()