import random
import numpy as np

def display_board(board):
    print('   |   | \n' ' ' + board[0][0] + ' | ' + board[0][1] + ' | ' + board[0][2])
    print('   |   | \n -----------',
          '\n   |   | \n ' + board[1][0] + ' | ' + board[1][1] + ' | ' + board[1][2],
          '\n   |   | \n ----------- \n',
          ' ' ' |   | \n' + board[2][0] + '  | ' + board[2][1] + ' | ' + board[2][2],
          '\n   |   |  ')

def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player : Do you want to be X or O? ').upper()
    if marker == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'

def place_marker(board, marker, position):
    board[int(position[0])][int(position[1])] = marker

def win_check(board, mark):
    out_comes_row = [[0, 0, 0], [1, 1, 1], [2, 2, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2]]
    out_comes_col = [[0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 0, 0], [1, 1, 1], [2, 2, 2], [0, 1, 2], [2, 1, 0]]
    for row, col in zip(out_comes_row, out_comes_col):
        if board[row[0]][col[0]] == board[row[1]][col[1]] == board[row[2]][col[2]] == mark:
            return True
    return False

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Computer'
    else:
        return 'Player'

def space_check(board, position):
    return board [int(position[0])][int(position[1])] == ' '

def full_board_check(board):
    if(f==[]):
        return True
    else:
        return False

def player_choice(board):
    p1 ='0'
    while p1 not in f or not space_check(board, p1):
        p1 = input('Choose your next position:')
    f.remove(p1)
    return p1

def computer_choice(board):
    p2 = f[random.randint(0,len(f)-1)]
    while not space_check(board, p2):
        p2 = f[random.randint(0,len(f)-1)]
    f.remove(p2)
    return p2

b = 1
d = {}
e = 'y'
print('Welcome to Tic Tac Toe!')
while b <= 3:
    a = []
    f=['00', '01', '02', '10', '11', '12', '20', '21', '22']
    theBoard = np.array([[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]])
    player_marker, computer_marker = player_input()
    a.append(player_marker)
    a.append(computer_marker)
    turn = choose_first()
    a.append(turn)
    print(turn + ' will go first.')
    play_game = input('Are you ready to play? Enter Yes or No.')
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
    while game_on:
        if turn == 'Player':
            display_board(theBoard)
            p1 = player_choice(theBoard)
            a.append(p1)
            place_marker(theBoard, player_marker, p1)
            if win_check(theBoard, player_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                a.append('Player won')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    a.append('It is a tie')
                    break
                else:
                    turn = 'Computer'
        else:
            display_board(theBoard)
            p2 = computer_choice(theBoard)
            a.append(p2)
            place_marker(theBoard, computer_marker, p2)
            if win_check(theBoard, computer_marker):
                display_board(theBoard)
                print('Computer has won!')
                a.append('Computer won')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    a.append('It is a tie')
                    break
                else:
                    turn = 'Player'
    d[b] = a
    b = b + 1
while e == 'y':
    try:
        c = int(input("Enter the game no. for the desired information"))
        if d[c][2] == 'Player':
            theBoard = np.array([[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]])
            for i in range(3, len(d[c])-1, 2):
                place_marker(theBoard, d[c][0], d[c][i])
                display_board(theBoard)
                place_marker(theBoard, d[c][1], (d[c][i + 1]))
                display_board(theBoard)
        else:
            theBoard = np.array([[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]])
            for i in range(3, len(d[c])-1, 2):
                place_marker(theBoard, d[c][1], d[c][i])
                display_board(theBoard)
                place_marker(theBoard, d[c][0], d[c][i + 1])
                display_board(theBoard)
        print(d[c][-1])
    except KeyError:
        print("Value should be of given range (1-10)")
    except ValueError:
        print("Value should be of correct type (integer)")
    finally:
        e = input("Would you like to try again? Press y for yes and any other key for no")
