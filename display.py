import data

# Greeting
def print_greeting():
    print("Welcome to the Game of Tic-Tac-Toe\n")

# Store the names of the players
def get_players(players):
    player_x = input("Please enter the name of Player X: ")
    player_o = input("Please enter the name of Player O: ")
    players.append(player_x)
    players.append(player_o)

# Draw the playing board
def draw_board(board):
    print()
    print("   |   |")
    print(" " + str(board[7]) + " | " +str( board[8]) + " | " + str(board[9]))
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" " + str(board[4]) + " | " + str(board[5]) + " | " + str(board[6]))
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" " + str(board[1]) + " | " + str(board[2]) + " | " + str(board[3]))
    print("   |   |")
    print()   

# Kick-off
def get_started():
    print("Let's Play!\n")

# Notify player when it is their turn to play
def player_control(player_name):
    print(f"It's your turn, {player_name}\n")

# Prompt for next move
def prompt_move(player_name):
    move = input(f"Okay, {player_name}, what is your move? ")
    return move

# Space Already Taken
def space_taken():
    print("\nSpace is already taken!  Please try again.")
    
# Switch players
def next_player(new_player):
    print(f"The new player is " + new_player)

# Tie Game
def tie_game():
    print("The game is a tie!\n")

# Message for Game Winner
def game_winner(current_player):
    print(f"Congratulations, " + current_player + ", you have won the game!\n")

# Game Statistics
def game_stats(players, games, x, o):
    text1 = "The running score in"
    text2 = "total games is"
    print(f"{text1} {games} {text2} {players[0]} - {x} | {players[1]} - {o}\n")

# Goodbye message
def goodbye():
    print("\nUntil next time. Good-bye.\n")