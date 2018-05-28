from IPython.display import clear_output

def print_index_table():
    print("_1_|_2_|_3_\n_4_|_5_|_6_\n_7_|_8_|_9_\n")

def print_rules():
    print("WELCOME TO TIC TAC TOE!\n")
    print("Below you have Tic Tac Toe # with intex numbers:")
    print_index_table()
    print("You can place your symbol by giving an index of desired field.")

def print_board():
#    clear_output()
#    player_move()
    for i in range(0,9,3):
        print('_{}_|_{}_|_{}_'.format(board[i], board[i+1], board[i+2]))

def get_player_input():
    while True:
        try:
            answer = int(input("{} your move. Where you want to put '{}'? ".format(players_name[marker],marker)))
            if answer in range(1,10) and board[answer-1] == '_':
                return answer
            else:
                print("Answer should be a number of a free spot(in range 1-9)")
        except ValueError:
            print("Answer should be a number in range 1-9.")

def place_marker(table, position):
    table[position-1] = marker
    return table

def decide_on_marker():
    if x_player_turn:
        return 'X'
    else:
        return 'O'

def check_win(index,marker):
    array = [[],[],[]]
    for i in range(3):
        array[i] = board[3*i : 3*i+3]
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
        

free_spots_left = list(range(1,10))
board = ['_','_','_','_','_','_','_','_','_']
x_player_turn = True
players_name = {'X':'Alex', 'O':'Basia'}
print_rules()

# players_name[x] = input("Please give me a name of player 1 (X)")
# players_name[o] = input("Please give me a name of player 2 (O)")

for x in range(9):
    #clear_output()
    marker = decide_on_marker()
    
    
    #print_board()
    move = get_player_input()
    board = place_marker(board,move)
    #clear_output()
    print("TIC TAC TOE index:")
    print_index_table()
    print_board()
    if x>=4:
        if check_win(move,marker):
            print('{} you win!'.format((players_name[marker])))
            print(board)
            print(move)
            print(marker)
            break
        else:
            print('nope', board, move, marker)
    x_player_turn = not x_player_turn
