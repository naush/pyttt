import random
import sys

print("Let's Play Tic-Tac-Toe!")

board = list("+++++++++")

def print_board(board):
    print(''.join(board[0:3]))
    print(''.join(board[3:6]))
    print(''.join(board[6:9]))

def available_moves(board):
    return [index for index, mark in enumerate(board) if mark == '+']

def empty_board(board):
    return len(available_moves(board)) == 0

def game_over(board):
    return (board[0] is not '+' and board[0] == board[1] and board[1] == board[2]) or \
           (board[3] is not '+' and board[3] == board[4] and board[4] == board[5]) or \
           (board[6] is not '+' and board[6] == board[7] and board[7] == board[8]) or \
           (board[0] is not '+' and board[0] == board[3] and board[3] == board[6]) or \
           (board[1] is not '+' and board[1] == board[4] and board[4] == board[7]) or \
           (board[2] is not '+' and board[2] == board[5] and board[5] == board[8]) or \
           (board[0] is not '+' and board[0] == board[4] and board[4] == board[8]) or \
           (board[2] is not '+' and board[2] == board[4] and board[4] == board[6])

def computer_move(board):
    moves = available_moves(board)
    return random.choice(moves)

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

while (empty_board(board) == False):
    if (current_player == player_2):
        move = computer_move(board)
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
