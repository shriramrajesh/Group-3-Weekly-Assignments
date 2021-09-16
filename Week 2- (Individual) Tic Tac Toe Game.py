def display_board(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player : Do you want to be X or O? ').upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
def place_marker(board, marker, position):
    board[position] = marker
def win_check(board, mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[7] == mark and board[8] == mark and board[9] == mark) or  # across the bottom
            (board[1] == mark and board[4] == mark and board[7] == mark) or  # down the middle
            (board[2] == mark and board[5] == mark and board[8] == mark) or  # down the middle
            (board[3] == mark and board[6] == mark and board[9] == mark) or  # down the right side
            (board[1] == mark and board[5] == mark and board[9] == mark) or  # diagonal
            (board[3] == mark and board[5] == mark and board[7] == mark))  # diagonal
import random
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Computer'
    else:
        return 'Player'
def space_check(board, position):
    return board[position] == ' '
def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True
def player_choice(board):
    p1 = 0
    while p1 not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, p1):
        p1 = int(input('Choose your next position: (1-9) '))
    return p1
def computer_choice(board):
    p2 = random.randint(1, 9)
    while not space_check(board, p2):
        p2 = random.randint(1, 9)
    return p2
def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')
print('Welcome to Tic Tac Toe!')
while True:
    # Reset the board
    theBoard = [' '] * 10
    player_marker, computer_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    play_game = input('Are you ready to play? Enter Yes or No.')
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
    while game_on:
        if turn == 'Player':
            # Player's turn.
            display_board(theBoard)
            p1 = player_choice(theBoard)
            place_marker(theBoard, player_marker, p1)

            if win_check(theBoard, player_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Computer'
        else:
            # Player2's turn.
            display_board(theBoard)
            p2 = computer_choice(theBoard)
            place_marker(theBoard, computer_marker, p2)
            if win_check(theBoard, computer_marker):
                display_board(theBoard)
                print('Computer has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player'
    if not replay():
        break
