# Data for Tic-Tac-Toe
players = []
player_marks = ['X', 'O']
current_player = ""

game_board = [' ','1','2','3','4','5','6','7','8','9']
duplicate_board = []

game_tallies = [0, 0]

# Audit Player Moves to keep track of all game moves in an active session
# per game.  First list will be a game number, i.e. Game 1, with the inner
# lists recording the moves of the individual players for that game.
audit_player_moves = [
    [
        [],
        []
    ],
    [
        [],
        []
    ]
]



