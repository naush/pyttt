import random
import sys

BOARD = "+++++++++"
PLAYER_1 = 'X'
PLAYER_2 = 'O' # Computer
SCORE_WIN = 1
SCORE_LOSE = -1
SCORE_DRAW = 0

def print_board(board):
    print('.' * 3)
    print(''.join(board[0:3]))
    print(''.join(board[3:6]))
    print(''.join(board[6:9]))

def available_moves(board):
    return [move for move, mark in enumerate(board) if mark == '+']

def draw(board):
    return len(available_moves(board)) == 0

def win(board, player):
    combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    return any((board[one] == player and
                board[one] == board[two] and
                board[two] == board[three]) for one, two, three in combinations)

def game_over(board):
    return win(board, PLAYER_1) or \
           win(board, PLAYER_2) or \
           draw(board)

def opponent(player):
    if (player == PLAYER_1):
        return PLAYER_2
    else:
        return PLAYER_1

def score(board, move, player):
    if win(board, player):
        return SCORE_WIN
    elif win(board, opponent(player)):
        return SCORE_LOSE
    else:
        return SCORE_DRAW

def minimax(board, move, player):
    board = play_move(board, move, player)

    if game_over(board):
        return score(board, move, player)
    else:
        return -max(minimax(board, move, opponent(player)) \
                    for move in available_moves(board))

def computer_move(board, player):
    scoreboard = [-2] * 9
    for move in available_moves(board):
        scoreboard[move] = minimax(board, move, player)
    return scoreboard.index(max(scoreboard))

def human_move(board):
    while True:
        try:
            move = int(input('Please enter move: '))
            if move in available_moves(board):
                break
            else:
                print('Invalid move')
        except ValueError:
            print('Invalid move')
    return move

def play_move(board, move, player):
    board = list(board)
    board[move] = player
    return board

board = list(BOARD)
player = PLAYER_1

print("Let's Play Tic-Tac-Toe!")
print_board(board)

while not game_over(board):
    if (player == PLAYER_1):
        move = human_move(board)
    else:
        move = computer_move(board, player)
    board = play_move(board, move, player)
    player = opponent(player)
    print_board(board)

if draw(board):
    print("Cat's Game")
elif win(board, PLAYER_1):
    print('Congratulations Player 1! You Won!')
else:
    print('Congratulations Player 2! You Won!')
