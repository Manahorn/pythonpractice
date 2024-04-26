import os 
import sys

art = r"""

░░░░░░░░▄▄▄▀▀▀▄▄███▄░░░░░░░░░░░░░░
░░░░░▄▀▀░░░░░░░▐░▀██▌░░░░░░░░░░░░░
░░░▄▀░░░░▄▄███░▌▀▀░▀█░░░░░░░░░░░░░
░░▄█░░▄▀▀▒▒▒▒▒▄▐░░░░█▌░░░░░░░░░░░░
░▐█▀▄▀▄▄▄▄▀▀▀▀▌░░░░░▐█▄░░░░░░░░░░░
░▌▄▄▀▀░░░░░░░░▌░░░░▄███████▄░░░░░░
░░░░░░░░░░░░░▐░░░░▐███████████▄░░░
░░░░░le░░░░░░░▐░░░░▐█████████████▄
░░░░toucan░░░░░░▀▄░░░▐█████████████▄
░░░░░░has░░░░░░░░▀▄▄███████████████
░░░░░arrived░░░░░░░░░░░░█▀██████░░

"""
print(art)
print("The toucan says to you: 'Let's play a game, shall we?' It's tic-tac-toe!")

game_board = ["_","_","_","_","_","_","_","_","_"]

def show_game_board():

    print(game_board[0:3])
    print(game_board[3:6])
    print(game_board[6:9])

show_game_board()

def select_player1():

    while True:
        try:
            player1_character_select = str(input("Atkárium, select between X or O "))
            if player1_character_select == "X" or player1_character_select == "O":
                return player1_character_select
            else:
                print("Please select either X or O")
        except ValueError:
            print("Please select either X or O")

player1_character = select_player1()
print("Atkárium's character is: " + player1_character)


def select_player2():

    if player1_character == "X":
        player2_character_select = "O"
    else:
        player2_character_select = "X"    
    return player2_character_select

player2_character = select_player2()
print("Poszat's character is: " + player2_character)

def player1_make_a_move():

    choice = ""
    acceptable_range = range(0,9)
    within_range = False

    while choice.isdigit() == False or within_range == False:
        
        choice = input("Atkárium, where would you like to place your marker on the board? (0-8): ")

        if choice.isdigit() == False:
            print("Waiiit a minute, thats not a digit!")

        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print("You are out of range, buckoo, quack!")
                within_range = False

    return int(choice)

""" player1_move = player1_make_a_move() """

def player1_move_resolution(game_board,player1_move):

    character = player1_character

    game_board[player1_move] = character

    return game_board


def player2_make_a_move():

    choice = ""
    acceptable_range = range(0,9)
    within_range = False

    while choice.isdigit() == False or within_range == False:
        
        choice = input("Poszat, where would you like to place your marker on the board? (0-8): ")

        if choice.isdigit() == False:
            print("Waiiit a minute, thats not a digit!")

        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print("You are out of range, buckoo, quack!")
                within_range = False

    return int(choice)

""" player2_move = player2_make_a_move() """

def player2_move_resolution(game_board,player2_move):

    character = player2_character

    game_board[player2_move] = character

    return game_board

def game_state_check():

    state_check = "_"

    if iswinner_player1(game_board, player1_character) == True:
        print("Player 1 wins!")
        restart = str(input("Would you like to play again? Y or N "))
        if restart == "Y":
            return str(restart)
        else:
            return False
    elif iswinner_player2(game_board, player2_character) == True:
        print("Player 2 wins!")
        restart = str(input("Would you like to play again? Y or N "))
        if restart == "Y":
            return str(restart)
        else:
            return False
    elif state_check not in game_board:
        print("Game ovaaah, quack! Restart the gaaameeee!!")
        restart = str(input("Would you like to play again? Y or N "))
        if restart == "Y":
            return str(restart)
        else:
            return False
    else:
        return True

def iswinner_player1(game_board, player1_character):
    return any(player1_character==game_board[a]==game_board[b]==game_board[c]
                for a,b,c in [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)])

def iswinner_player2(game_board, player2_character):
    return any(player2_character==game_board[a]==game_board[b]==game_board[c]
                for a,b,c in [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)])

game_on = game_state_check()
game_board = ["_","_","_","_","_","_","_","_","_"]

while game_on:

    # player1_make_a_move()
    player1_move = player1_make_a_move()
    player1_move_resolution(game_board, player1_move)

    show_game_board()

    game_on = game_state_check()
    if game_on == "Y":
        sys.stdout.flush()
        os.execv(sys.executable, [sys.executable] + sys.argv)

    win_condition_player1 = iswinner_player1(game_board, player1_character)
    print(win_condition_player1)
    # player2_make_a_move()
    player2_move = player2_make_a_move()
    player2_move_resolution(game_board, player2_move)

    show_game_board()

    game_on = game_state_check()
    win_condition_player2 = iswinner_player2(game_board, player2_character)
    print(win_condition_player2)

    if game_on == "Y":
        sys.stdout.flush()
        os.execv(sys.executable, [sys.executable] + sys.argv)
