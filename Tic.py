from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])
def player_input():
    while True:
        pl=input("please pick a marker 'X' or 'O':  " )
        if pl=='X':
            return ('X','O')
        else:
            return ('O','X')
def place_marker(board, marker, position):
    board[position]=marker
def win_check(board,mark):
    for i in [1,4,7]:
        if board[i]==mark and board[i+1]==mark and board[i+2]==mark:
            return True
    for e in [1,2,3]:
        if board[e]==mark and board[e+3]==mark and board[e+6]==mark:
            return True
    if board[1]==mark and board[5]==mark and board[9]==mark:
    	return True
    if board[3]==mark and board[5]==mark and board[7]==mark:
    	return True  
    return False
from random import randint
def choose_first():
    if randint(0,2)==1:
        return 'Player 1'
    else:
        return 'Player 2'
def space_check(board, position):
    if board[position]==' ':
        return True
    return False
def full_board_check(board):
    for i in range(1,10):
        if board[i]==' ':
            return True
    return False
def player_choice(board):
    position=int(input("Your next position?"))
    if space_check(board, position):
        return position
    return False
def replay():
    response=input("Do you want to play again Y/N? ")
    if response=='Y':
        return True
    else:
        return False
print('Welcome to Tic Tac Toe!')
while True:
    # Set the game up here
    #pass
    board = [' '] * 10
    display_board(board)
    turn=choose_first()
    print(turn+" will play first")
    mark1,mark2=player_input()
    if turn=="Player 1":
    	player_1_mark=mark1
    	player_2_mark=mark2
    else:
    	player_2_mark=mark1
    	player_1_mark=mark2
    print(f"{turn} has choosen {mark1}")
    play=input(("Are you ready to play or not? press 'Y' or 'N'  "))
    if play=='Y':
        play=True
    else:
        play=False
    while play:
        if turn=='Player 1':
            display_board(board)
            position = player_choice(board)
            if position:
                place_marker(board,player_1_mark,position)
                display_board(board)
                if win_check(board,player_1_mark):
                    print('Conratulations! Player 1 Win the Game')
                    break
                if full_board_check(board):
                    print("Player 2 Turn: ")
                    turn='Player 2'
                else:
                    print('This game is Draw!!')
                    break
            else:
                while not position:
                    print("That position is Already occupied\n please select the number again")
                    position = player_choice(board)
                place_marker(board,player_1_mark,position)
                display_board(board)
        else:
            position = player_choice(board)
            if position:
                place_marker(board,player_2_mark,position)
                display_board(board)
                if win_check(board,player_2_mark):
                    print('Conratulations! Player 2 Win the Game')
                    break
                if full_board_check(board):
                    print("Player 1 Turn: ")
                    turn='Player 1'
                else:
                    print('This game is Draw!!')
                    break
            else:
                while not position:
                    print("That position is Already occupied\n please select the number again")
            
        
    if not replay():
        break