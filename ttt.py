
import display
import data
import random
import sys

def get_copy_of_board(board):
    for i in board:
        data.duplicate_board.append(i)
    return data.duplicate_board

def manage_board(board):
    del board[1:]
    for i in range(1,10):
        board.append(str(i))

def who_goes_first():
    if random.randint(0, 1) == 0:
        return data.players[0]
    else:
        return data.players[1]

def switch_player(players, current_player):
    for index, player in enumerate(players, start=0):
        if players[index] == current_player:
            current_player = players[index + 1]
            return current_player
        elif players[index + 1] == current_player:
            current_player = players[index]
            return current_player

def check_move(board, move):
    move = int(move)
    if is_space_open(board, move):
        return True
    else:
        return False

def determine_mark(current_player):
    player_index = data.players.index(current_player)
    mark = data.player_marks[player_index]
    return mark

def is_space_open(board, move):
    #return board[move] == " "
    move_to_evaluate = str(move)
    #for move_to_evaluate in range(1,10):
        #if board[move] in ('1','2','3','4','5','6','7','8','9'):
    if move_to_evaluate in board[move]:
        return True
    else:
        return False

def update_board(board, move, player_mark):
    move = int(move)
    board[move] = player_mark

def is_game_won(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[1] == mark and board[2] == mark and board[3] == mark) or 
    (board[7] == mark and board[4] == mark and board[1] == mark) or
    (board[8] == mark and board[5] == mark and board[2] == mark) or
    (board[9] == mark and board[6] == mark and board[3] == mark) or
    (board[7] == mark and board[5] == mark and board[3] == mark) or
    (board[9] == mark and board[5] == mark and board[1] == mark))

def is_board_full(board):
    for i in range(1,10):
        if is_space_open(board, i):
            return False
    return True

def increment_winner_totals(players, current_player, tallies):
    for index, player in enumerate(players, start=0):
        if players[index] == current_player:
            total = data.game_tallies[index]
            total += 1
            tallies[index] = total
            return tallies
        elif players[index + 1] == current_player:
            total = data.game_tallies[index + 1]
            total += 1
            tallies[index + 1] = total
            return tallies

def keep_playing():
    choice = input("Do you wish to continue playing? (y or n) ")
    return choice

def audit_moves(current_player, move, game):
    # This is not currently working
    player_index = data.players.index(current_player)
    #data.audit_player_moves[player_index].append(move)
    #data.audit_player_moves[game][player_index].append(move)
    for index, audit in enumerate(data.audit_player_moves,start=0):
        #audit.insert(game-1,game)
        print(f"index = {index} | audit = {audit}")
        data.audit_player_moves[index][index] = move
    print(f"AUDIT {audit}")
    print(f"AUDIT_MOVES = {data.audit_player_moves}")


# Main function
def main():
    display.print_greeting()
    count_playerX_wins = 0
    count_playerO_wins = 0
    total_games = 0
    game_is_playing = True
    continue_game = "n"
    display.get_players(data.players)
    data.current_player = who_goes_first()
    #display.draw_board(data.game_board)
    display.get_started()
    while game_is_playing:
        display.draw_board(data.game_board)
        display.player_control(data.current_player)
        move = display.prompt_move(data.current_player)
        #check_move(data.game_board, move)
        while not check_move(data.game_board, move):
            display.space_taken()
            move = display.prompt_move(data.current_player)
        audit_moves(data.current_player, move, (total_games + 1))  
        mark = determine_mark(data.current_player)
        update_board(data.game_board, move,  mark)
        display.draw_board(data.game_board)
        if is_game_won(data.game_board, mark):
            display.draw_board(data.game_board)
            display.game_winner(data.current_player)
            data.game_tallies = increment_winner_totals(data.players, 
                                                        data.current_player,
                                                        data.game_tallies)
            count_playerX_wins = data.game_tallies[0]
            count_playerO_wins = data.game_tallies[1]
            total_games += 1
            display.game_stats(data.players, 
                               total_games,
                               count_playerX_wins, 
                               count_playerO_wins)
            continue_game = keep_playing()
            if continue_game == "n":
                game_is_playing = False
            else:
                manage_board(data.duplicate_board)
                data.game_board = data.duplicate_board
        else:
            if is_board_full(data.game_board):
                display.draw_board(data.game_board)
                display.tie_game()
                total_games += 1
                continue_playing = keep_playing()
                if continue_playing == "n":
                    game_is_playing = False
                else:
                    manage_board(data.duplicate_board)
                    data.game_board = data.duplicate_board
            else:
                data.current_player = switch_player(data.players, data.current_player)
                display.next_player(data.current_player)

    display.goodbye() # Game Over Man, Game Over!


# Main Program Flow
get_copy_of_board(data.game_board)
main()




# Replaced the below with more readable code 5-September-2019

""" def drawboard(board):
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
 """
""" def get_players():
    playerX = input("Enter the name of player X: ")    
    playerO = input("Enter the name of player O: ") 
    players.append(playerX)
    players.append(playerO)

def t(board):
    while True:
        try:
            x = int(input())
            if x in board:
                return x
            else:
                print("\nSpace already taken. Try again")
        except ValueError:
            print("\nThat's not a number. enter a space 1-9")

def move(win, board, player):
    for left, middle, right in win:
        if board[left] == board[middle] == board[right]:
            return player

    if 9 == sum((pos == "X" or pos == "O") for pos in board):
        #print("The game ends in a tie\n")
        return False

def tic_tac_toe():
    board = [None] + list(range(1, 10))
    win = [(1, 2, 3),(4, 5, 6),(7, 8, 9),
            (1, 4, 7),(2, 5, 8),(3, 6, 9),
            (1, 5, 9),(3, 5, 7)]

    for player in "XO" * 9:
        drawboard(board)
        if player == "X":
            print(f"Player {players[0]}")
        else:
            print(f"Player {players[1]}")
        board[t(board)] = player
        if move(win, board, player):
            return player
        elif move(win, board, player) is False:
            return "Tie"
        print()

def main():
    count_x = 0
    count_o = 0
    total_games = 0

    while True:
        score = tic_tac_toe()
        total_games += 1
        if score == "X":
            count_x += 1
            print(f"\nCongratulations, Player {players[0]} wins!")
        elif score == "O":
            count_o += 1
            print(f"\nCongratulations, Player {players[1]} wins!")
        elif score == "Tie":
            print("The game ends in a tie\n")

        print("The running score in " + str(total_games) + " total games is "
                + "(" + players[0] + ": " + str(count_x) + " " +
                players[1] + ": " + str(count_o) + ")")

        if input("Play again (y/n)\n") != "y":
            break

# Main program
print("Welcome to Tic-Tac-Toe!")   
players = []  
get_players() 

main() """

            