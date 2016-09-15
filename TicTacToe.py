gameover = False
turn_count = 0
#XO = 'X'

#who goes first?
from random import randint
XO = randint(0,1)
if XO == 0:
    XO = 'O'
    print 'Player \'O\' goes first'
else:
    XO = 'X'
    print 'Player \'X\' goes first'

#printing the board creation
def print_board(board):
    for row in board:
        print ' '.join(row)

#board creation
board = []
for row in range(0, 3):
    board.append(['-'] * 3)
print_board(board)


#board win conditions 8 combinations
def check_winner(XO):
    if board[0][0] == XO and board[0][1] == XO and board[0][2] == XO:
        return True
    elif board[1][0] == XO and board[1][1] == XO and board[1][2] == XO:
        return True
    elif board[2][0] == XO and board[2][1] == XO and board[2][2] == XO:
        return True
    elif board[0][0] == XO and board[1][0] == XO and board[2][0] == XO:
        return True
    elif board[0][1] == XO and board[1][1] == XO and board[1][1] == XO:
        return True
    elif board[0][2] == XO and board[1][2] == XO and board[2][2] == XO:
        return True
    elif board[0][0] == XO and board[1][1] == XO and board[2][2] == XO:
        return True
    elif board[2][0] == XO and board[1][1] == XO and board[0][2] == XO:
        return True


#player selecting
def select_loc():
    global player_row
    global player_col
    player_row = int(raw_input('Pick a row 0 - 2:'))
    while player_row > 2 or player_row < 0:
        player_row = int(raw_input('Not in range, please pick a row 0 - 2:'))
    player_col = int(raw_input('Pick a col 0 - 2:'))
    while player_col > 2 or player_col < 0:
        player_col = int(raw_input('Not in range, please pick a col 0 - 2:'))


#player turn
while gameover != True:
    print 'Player %s\'s turn' % XO
    if turn_count == 9:
        print 'Game Over! Draw!'
        break
    else:
        select_loc()
        if board[player_row][player_col] == 'X' or board[player_row][player_col] == 'O':
            print "Whoops, someone already went there"
            select_loc()
        board[player_row][player_col] = XO
        print_board(board)
        if check_winner(XO):
            gameover = True
            print 'Game Over! %s wins' % XO
        #print 'gameover after turn: ', gameover
        turn_count += 1
        if XO == 'X':
            XO = 'O'
        elif XO == 'O':
            XO = 'X'