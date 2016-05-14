import random
import sys

print("Let's Play Tic-Tac-Toe!")

board = list("+++++++++")

def print_board(board):
    print(''.join(board[0:3]))
    print(''.join(board[3:6]))
    print(''.join(board[6:9]))

def available_moves(board):
    return [move for move, mark in enumerate(board) if mark == '+']

def draw(board):
    return len(available_moves(board)) == 0

def win(board, current_player):
    return (board[0] == current_player and board[0] == board[1] and board[1] == board[2]) or \
           (board[3] == current_player and board[3] == board[4] and board[4] == board[5]) or \
           (board[6] == current_player and board[6] == board[7] and board[7] == board[8]) or \
           (board[0] == current_player and board[0] == board[3] and board[3] == board[6]) or \
           (board[1] == current_player and board[1] == board[4] and board[4] == board[7]) or \
           (board[2] == current_player and board[2] == board[5] and board[5] == board[8]) or \
           (board[0] == current_player and board[0] == board[4] and board[4] == board[8]) or \
           (board[2] == current_player and board[2] == board[4] and board[4] == board[6])

def game_over(board):
    return win(board, 'O') or \
           win(board, 'X') or \
           draw(board)

def score(board, move, current_player):
    board = list(board)
    board[move] = current_player

    if (current_player == 'O'):
        opponent_player = 'X'
    else:
        opponent_player = 'O'

    if (win(board, current_player)):
        return 1 # win score
    elif (win(board, opponent_player)):
        return -1 # lose score
    elif (draw(board)):
        return 0 # draw
    else:
        return 2 # continue

def recursive_score(board, move, current_player):
    current_score = score(board, move, current_player)

    board = list(board)
    board[move] = current_player

    if (current_score == 2):
        if (current_player == 'O'):
            opponent_player = 'X'
        else:
            opponent_player = 'O'
        return -min(recursive_score(board, next_move, opponent_player) for next_move in available_moves(board))
    else:
        return -current_score

def minimax(board, move, current_player):
    current_score = score(board, move, current_player)

    if (current_score < 2):
        return current_score
    else:
        board = list(board)
        board[move] = current_player

        if (current_player == 'O'):
            opponent_player = 'X'
        else:
            opponent_player = 'O'

        return min(recursive_score(board, next_move, opponent_player) for next_move in available_moves(board))

def computer_move(board, current_player):
    scoreboard = [-2] * 9 # -2 is min score
    for move in available_moves(board):
        scoreboard[move] = minimax(board, move, current_player)
    print(scoreboard)
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

print_board(board)

player_1 = 'X'
player_2 = 'O' # Computer
current_player = player_1

while True:
    if (current_player == player_2):
        move = computer_move(board, current_player)
    else:
        move = human_move(board)

    board[move] = current_player
    print_board(board)

    if game_over(board):
        if (current_player == player_1):
            print('Congratulations Player 1! You Won!')
        else:
            print('Congratulations Player 2! You Won!')
        sys.exit()
    else:
        if (current_player == player_1):
            current_player = player_2
        else:
            current_player = player_1

print("Cat's Game")
