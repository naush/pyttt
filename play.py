import random

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

board[1] = 'X'
print_board(board)

board[3] = 'O'
print_board(board)

moves = available_moves(board)
random_move = random.choice(moves)
board[random_move] = 'X'
print_board(board)

player_1 = 'X'
player_2 = 'O' # Computer
current_player = player_1

while (empty_board(board) == False):
    if (current_player == player_1):
        current_player = player_2
    else:
        current_player = player_1
    if (current_player == player_2):
        move = computer_move(board)
    else:
        move = human_move(board)
    board[move] = current_player
    print_board(board)
