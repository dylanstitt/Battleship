# Dylan Stitt
# Battleship Review
# 8/28/23

from BoardItems import Map
from Extras import *
from os import system
from time import sleep
from random import choice


def playAgain():
    again = input('\n\nWould you like to play again (y, n): ').lower()
    while again not in ['y', 'n']:
        again = input('Would you like to play again (y, n): ').lower()

    if again == 'y':
        main()

    else:
        system('cls')
        print(goodbye)


def main():
    system('cls')
    print(title)
    input('\nPRESS ANY KEY TO PLAY')
    system('cls')

    map = Map()
    playing = True

    yn = input('Do you want to read the rules (y, n): ').lower()
    while yn not in ['y', 'n']:
        yn = input('Invalid response. Do you want to read the rules (y, n): ').lower()

    if yn == 'y':
        print(rules)
        input('PRESS ANY BUTTON TO CONTINUE')

    map.place_ships()
    map.place_com_ship()

    # True = Player, False = Computer
    shooter = choice([True, False])

    while playing:
        shooter = not shooter
        sleep(2)
        system('cls')
        print(map)

        if shooter:
            print('It is your turn\n\n')

            print(map.c_ships)

            sleep(3)
            space, dir = map.validate_space('player')
            map.change_space(space, 'player')

            if len(map.c_ships) == 0:
                system('cls')
                print(win)
                print('\nYou have defeated the opponent!!')
                playAgain()

        else:
            print('It is the computer\'s turn\n\n')
            space, dir = map.validate_space('com')
            map.change_space(space, 'com')

            if len(map.p_ships) == 0:
                system('cls')
                print(loss)
                print('\nYou have been defeated by your opponent')
                playAgain()


if __name__ == '__main__':
    main()
