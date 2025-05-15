import random
import pickle
import os.path

class TicTacToeAI:
    def __init__(self, learning_rate=0.1, exploration_rate=0.3):
        # Initialize Q-learning parameters
        self.learning_rate = learning_rate  # How quickly the AI adapts to new information
        self.exploration_rate = exploration_rate  # Probability of making a random exploratory move
        self.q_values = {}  # Dictionary to store state-action values
        self.last_state = None
        self.last_action = None
        
        # Try to load existing Q-values if available
        self.load_q_values()
    
    def get_q_value(self, state, action):
        # Get the Q-value for a state-action pair, default to 0.0 if not found
        if (state, action) not in self.q_values:
            self.q_values[(state, action)] = 0.0
        return self.q_values[(state, action)]
    
    def choose_action(self, state, available_actions):
        # Choose an action based on the current state
        if random.random() < self.exploration_rate:
            # Exploration: choose a random action
            return random.choice(available_actions)
        else:
            # Exploitation: choose the best action based on Q-values
            q_values = [self.get_q_value(state, action) for action in available_actions]
            max_q = max(q_values)
            # If multiple actions have the same max Q-value, choose randomly among them
            best_actions = [action for i, action in enumerate(available_actions) if q_values[i] == max_q]
            return random.choice(best_actions)
    
    def learn(self, state, action, reward, next_state, next_available_actions):
        # Q-learning update rule
        # If game is over (no next actions), only consider immediate reward
        if not next_available_actions:
            max_next_q = 0
        else:
            # Otherwise, consider the maximum future value
            max_next_q = max([self.get_q_value(next_state, next_action) 
                             for next_action in next_available_actions], default=0)
        
        # Update Q-value for the current state-action pair
        current_q = self.get_q_value(state, action)
        self.q_values[(state, action)] = current_q + self.learning_rate * (reward + max_next_q - current_q)
    
    def make_move(self, board, player):
        # Convert board to tuple for state representation
        state = tuple(board)
        
        # Get available actions (empty cells)
        available_actions = [i for i in range(9) if board[i] == ' ']
        
        if not available_actions:
            return None
        
        # Choose an action
        action = self.choose_action(state, available_actions)
        
        # Store state and action for learning
        self.last_state = state
        self.last_action = action
        
        return action
    
    def reward(self, value, board, available_actions):
        # Provide reward to the AI and allow it to learn
        if self.last_state is not None and self.last_action is not None:
            self.learn(self.last_state, self.last_action, value, tuple(board), available_actions)
    
    def save_q_values(self):
        # Save Q-values to a file
        with open('tictactoe_q_values.pkl', 'wb') as f:
            pickle.dump(self.q_values, f)
    
    def load_q_values(self):
        # Load Q-values from a file if it exists
        if os.path.isfile('tictactoe_q_values.pkl'):
            try:
                with open('tictactoe_q_values.pkl', 'rb') as f:
                    self.q_values = pickle.load(f)
            except:
                # If there's an error loading, start with empty Q-values
                self.q_values = {}

def print_board(board):
    # Display the game board
    print("\n")
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i < 6:
            print("-----------")

def check_win(board, player):
    # Check all possible winning combinations
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    
    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

def check_tie(board):
    # Check if the game is a tie (no empty spaces left)
    return ' ' not in board

def get_human_move(board):
    # Get and validate the human player's move
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1  # Adjust for 0-based indexing
            if 0 <= move < 9 and board[move] == ' ':
                return move
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Please enter a number between 1 and 9.")

def main():
    # Create AI agent
    ai = TicTacToeAI()
    
    print("Welcome to Tic-tac-toe vs. AI!")
    print("The AI will learn as you play.")
    print("Positions are numbered 1-9 from top-left to bottom-right.")
    
    try:
        while True:
            # Initialize game board
            board = [' ' for _ in range(9)]
            
            # Decide who goes first
            current_player = 'X' if random.random() < 0.5 else 'O'
            human_player = input("Choose X or O: ").upper()
            
            while human_player not in ['X', 'O']:
                human_player = input("Invalid choice. Choose X or O: ").upper()
            
            ai_player = 'O' if human_player == 'X' else 'X'
            
            print(f"You are {human_player}, AI is {ai_player}")
            
            # Game loop
            game_over = False
            
            while not game_over:
                print_board(board)
                
                # Current player's turn
                if current_player == human_player:
                    print("Your turn")
                    move = get_human_move(board)
                else:
                    print("AI's turn")
                    available_actions = [i for i in range(9) if board[i] == ' ']
                    move = ai.make_move(board, ai_player)
                
                # Make the move
                board[move] = current_player
                
                # Check game status
                if check_win(board, current_player):
                    print_board(board)
                    print(f"{current_player} wins!")
                    
                    # Reward AI based on outcome
                    if current_player == ai_player:
                        ai.reward(1.0, board, [])  # Positive reward for winning
                    else:
                        ai.reward(-1.0, board, [])  # Negative reward for losing
                    
                    game_over = True
                elif check_tie(board):
                    print_board(board)
                    print("It's a tie!")
                    ai.reward(0.2, board, [])  # Small positive reward for tie
                    game_over = True
                else:
                    # Switch players
                    current_player = ai_player if current_player == human_player else human_player
                    
                    # If it's now the human's turn, the AI should get an intermediate reward
                    if current_player == human_player:
                        available_actions = [i for i in range(9) if board[i] == ' ']
                        ai.reward(0.0, board, available_actions)  # Neutral intermediate reward
            
            # Save AI's learning after each game
            ai.save_q_values()
            
            # Ask to play again
            play_again = input("Play again? (y/n): ").lower()
            if play_again != 'y':
                break
    
    except KeyboardInterrupt:
        print("\nGame interrupted. Saving AI's learning...")
        ai.save_q_values()
        print("Goodbye!")

if __name__ == "__main__":
    main() 