import random
import sys

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
    return win(board, 'O') or \
           win(board, 'X') or \
           draw(board)

def opponent(player):
    if (player == 'O'):
        return 'X'
    else:
        return 'O'

def score(board, move, player):
    if win(board, player):
        return  1 # win score
    elif win(board, opponent(player)):
        return -1 # lose score
    else:
        return  0 # draw

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

print("Let's Play Tic-Tac-Toe!")

board = list("+++++++++")
player_1 = 'X'
player_2 = 'O' # Computer
player = player_1
print_board(board)

while not game_over(board):
    if (player == player_2):
        move = computer_move(board, player)
    else:
        move = human_move(board)
    board = play_move(board, move, player)
    player = opponent(player)
    print_board(board)

if draw(board):
    print("Cat's Game")
elif win(board, player_1):
    print('Congratulations Player 1! You Won!')
else:
    print('Congratulations Player 2! You Won!')
