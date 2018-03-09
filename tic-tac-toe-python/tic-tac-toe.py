import random
import sys
import os

play_field = [0,1,2,3,4,5,6,7,8]
player_1 = 'X'
player_2 = 'O'

def draw():
    print (play_field[0] , '|', play_field[1] , '|', play_field[2])
    print (play_field[3] , '|', play_field[4] , '|', play_field[5])
    print (play_field[6] , '|', play_field[7] , '|', play_field[8])

while True:

    draw()
    try:
        chosen_spot = int(input("Choose a spot: "))

        if play_field[chosen_spot] != player_1 and play_field[chosen_spot] != player_2:
            play_field[chosen_spot] = player_1

        else:
            print ('This spot is taken')

    except IndexError:
        print ('DOES NOT EXIST')

        if(play_field[0] == player_1 and playfield[1] == player_1 and playfield[2] == player_1) or\
          (play_field[3] == player_1 and playfield[4] == player_1 and playfield[5] == player_1) or\
          (play_field[6] == player_1 and playfield[7] == player_1 and playfield[8] == player_1) or\
          (play_field[0] == player_1 and playfield[4] == player_1 and playfield[9] == player_1) or\
          (play_field[6] == player_1 and playfield[4] == player_1 and playfield[2] == player_1) or\
          (play_field[0] == player_1 and playfield[3] == player_1 and playfield[6] == player_1) or\
          (play_field[1] == player_1 and playfield[4] == player_1 and playfield[7] == player_1) or\
          (play_field[2] == player_1 and playfield[5] == player_1 and playfield[8] == player_1):
            print("Player 1 wins")

    draw()
    try:
        chosen_spot = int(input("Choose a spot: "))

        if play_field[chosen_spot] != player_2 and play_field[chosen_spot] != player_1:
            play_field[chosen_spot] = player_2

        else:
            print ('This spot is taken')

    except IndexError:
        print ('DOES NOT EXIST')

        if(play_field[0] == player_2 and playfield[1] == player_2 and playfield[2] == player_2) or\
           (play_field[3] == player_2 and playfield[4] == player_2 and playfield[5] == player_2) or\
           (play_field[6] == player_2 and playfield[7] == player_2 and playfield[8] == player_2) or\
           (play_field[0] == player_2 and playfield[4] == player_2 and playfield[9] == player_2) or\
           (play_field[6] == player_2 and playfield[4] == player_2 and playfield[2] == player_2) or\
           (play_field[0] == player_2 and playfield[3] == player_2 and playfield[6] == player_2) or\
           (play_field[1] == player_2 and playfield[4] == player_2 and playfield[7] == player_2) or\
           (play_field[2] == player_2 and playfield[5] == player_2 and playfield[8] == player_2):
             print("Player 1 wins")
