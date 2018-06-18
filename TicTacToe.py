from IPython.display import clear_output

def print_index_table():
    print("_1_|_2_|_3_\n_4_|_5_|_6_\n_7_|_8_|_9_\n")

def print_rules():
    print("WELCOME TO TIC TAC TOE!\n")
    print("Below you have Tic Tac Toe # with intex numbers:")
    print_index_table()
    print("You can place your symbol by giving an index of desired field.")

def print_board(board):
    for i in range(0,9,3):
        print('_{}_|_{}_|_{}_'.format(board[i], board[i+1], board[i+2]))

def get_player_input():
    while True:
        try:
            answer = int(input("{} your move. Where you want to put '{}'? ".format(players_name[marker], marker)))
            if answer in range(1,10) and board[answer-1] == '_':
                return answer
            else:
                print("Answer should be a number of a free spot(in range 1-9)")
        except ValueError:
            print("Answer should be a number in range 1-9.")

def place_marker(board, move, marker):  
    board[move-1] = marker
    return board

def decide_on_marker():
    if x_player_turn:
        return 'X'
    else:
        return 'O'

def check_win(index, mark, board):  
    # array = [[],[],[]]
    array = [board[:3], board[3:6], board[6:]]
    
    row = (index-1) // 3 
    column = (index-1) % 3
    
    #check row
    if array[row][0] == array[row][1] == array[row][2] == mark:
        return True
    #check column
    if array[0][column] == array[1][column] == array[2][column] == mark:
        return True
    #check diagonals
    if index in range(1,10,2):
        if array[0][0] == array[1][1] == array[2][2] == mark or array[0][2] == array[1][1] == array[2][0] == mark:
               return True
    return False

def who_is_the_winner(players_points, players_name):
    if players_points['X'] > players_points['O']:
        print('Congratulation {} you win whole game!'.format((players_name['X'])))
    elif players_points['X'] < players_points['O']:
        print('Congratulation {} you win whole game!'.format((players_name['O'])))
    else:
        print("It's a tie!")


x_player_turn = True
still_playing = True
players_name = {'X':'', 'O':''}
players_points = {'X':0, 'O':0}
print_rules()

players_name['X'] = input("Please give me a name of player 1 (X)")
players_name['O'] = input("Please give me a name of player 2 (O)")

while still_playing:
    board = ['_','_','_','_','_','_','_','_','_']
    for x in range(9):
        marker = decide_on_marker()
        move = get_player_input()
        board = place_marker(board, move, marker)
        clear_output()
        print("TIC TAC TOE index:")
        print_index_table()
        print_board(board)
    
        if x>=4:
            player_won = check_win(move, marker, board)
            if player_won:
                print('{} you win!'.format((players_name[marker])))
                players_points[marker] += 1
                break
        if x == 9 and not player_won:
            print('It\'s a draw!')
        x_player_turn = not x_player_turn
    while True:
        next_play_answer = input("Do you want to play again? Y/N ")
        if next_play_answer.upper() == 'N':
            who_is_the_winner(players_points, players_name)
            still_playing = False
            break
        elif next_play_answer.upper() == 'Y':
            x_player_turn = not x_player_turn  #next game will start looser
            break