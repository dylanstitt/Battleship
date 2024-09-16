from os import system
from random import choice, randint
from time import sleep


class Ship:

    def __init__(self, length, name):
        self.length = length
        self.name = name
        self.hits = 0

    def __str__(self):
        return self.name


class Map:

    def __init__(self):
        self.blank_space = '🌊'
        self.ship_space = '🟢'
        self.hit = '🟥'
        self.not_hit = '⬜'

        self.p_ships = {}
        self.c_ships = {}

        self.player_map = [[self.blank_space for i in range(10)] for j in range(10)]
        self.opponent_map = [[self.blank_space for i in range(10)] for j in range(10)]
        self.opponent_display_map = [[self.blank_space for i in range(10)] for j in range(10)]

        self.letter_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        self.lens_for_com = [2, 3, 3, 4, 5, 6]
        self.count = 0
        self.c = 0

    def __str__(self):
        system('cls')
        temp_map1 = []
        for row in self.player_map:
            temp_map1.append(' '.join(row))

        temp_map2 = []
        for row in self.opponent_display_map:
            temp_map2.append(' '.join(row))

        print('\t >>>>Opponent Map<<<<<')
        print('\n 1  2  3  4  5  6  7  8  9  10')
        for i in self.letter_list:
            print(f'{i}{temp_map2[self.letter_list.index(i)]}')

        print('\n\t  >>>>Your Map<<<<<')
        print('\n 1  2  3  4  5  6  7  8  9  10')

        for i in self.letter_list:
            print(f'{i}{temp_map1[self.letter_list.index(i)]}')

        print(
            f'\nLegend:\n\nEmpty Space - {self.blank_space}\nShip Space - {self.ship_space}\nHit - {self.hit}\nMiss - {self.not_hit}')

        return ''

    def validate_space(self, shooter, length=None, placing_ships=False):
        l, n, dir = None, None, None
        error = ''

        if shooter == 'player' and placing_ships:
            space = input("Enter the space you want to place a ship at (Letter:Number): ").upper()
            while len(list(space)) < 2 or list(space)[0] not in self.letter_list:
                space = input(
                    "Invalid space format: Enter the space you want to place a ship at (Letter:Number): ").upper()

            l, n = self.convert(space)
            l = self.letter_list[l]

        elif shooter == 'player':
            space = input("Enter the space you want to fire at: ").upper()
            l, n = self.convert(space)
            l = self.letter_list[l]

        else:
            l, n = choice(self.letter_list), choice([i for i in range(10)])
            dir = choice(['n', 's', 'e', 'w'])

        if l not in self.letter_list:
            print('That was an invalid letter')
            return self.validate_space(shooter)

        try:
            if n + 1 < 1 or n + 1 > 10:
                print('That number is not between 1 & 10')
                if placing_ships:
                    return self.validate_space(shooter, length, True)
                return self.validate_space(shooter)

        except:
            print('That was not a numberino')
            if placing_ships:
                return self.validate_space(shooter, length, True)
            return self.validate_space(shooter)

        l = self.letter_list.index(l)

        if placing_ships:
            # Check all ship spaces for other ship spaces (self-ship collision)
            if shooter == 'player':
                dir = input('Enter the direction you want to place the ship (N, S, E, W): ').lower()
                while dir not in ['n', 's', 'e', 'w']:
                    dir = input('Enter the direction you want to place the ship (N, S, E, W): ').lower()

                if dir == 'n':
                    if (l - (length - 1)) < 0:
                        error = 'OoB'

                    else:
                        for i in range(0, length):
                            if self.player_map[l - i][n] == self.ship_space:
                                error = 'ship_col'

                elif dir == 's':
                    if (l + (length - 1)) > 9:
                        error = 'OoB'

                    else:
                        for i in range(0, length):
                            if self.player_map[l + i][n] == self.ship_space:
                                error = 'ship_col'

                elif dir == 'e':
                    if (n + (length - 1)) > 9:
                        error = 'OoB'

                    else:
                        for i in range(0, length):
                            if self.player_map[l][n + i] == self.ship_space:
                                error = 'ship_col'

                elif dir == 'w':
                    if (n - (length - 1)) < 0:
                        error = 'OoB'

                    else:
                        for i in range(0, length):
                            if self.player_map[l][n - i] == self.ship_space:
                                error = 'ship_col'

                if error == 'OoB':
                    print('That space is out of bounds')
                    return self.validate_space(shooter, length, True)

                elif error == 'ship_col':
                    print('You cannot place a ship on top of another one')
                    return self.validate_space(shooter, length, True)

        # Check for if space was already fired at
        else:
            if shooter == 'player':
                if self.opponent_map[l][n] in [self.hit, self.not_hit]:
                    print('That space was already fired at.')
                    self.validate_space(shooter)

                else:
                    self.change_space(f'{self.letter_list[l]}{n + 1}', shooter)

            else:
                if self.player_map[l][n] in [self.hit, self.not_hit]:
                    self.validate_space(shooter)

                else:
                    self.change_space(f'{self.letter_list[l]}{n + 1}', shooter)

        return f'{self.letter_list[l]}{n + 1}', dir

    def check_space(self, space, shooter):
        l, n = self.convert(space)

        if shooter == 'player':
            return self.opponent_map[l][n]
        else:
            return self.player_map[l][n]

    # Place ships and red/white pegs
    def change_space(self, space, shooter, placing_ships=False, dir=None, length=None):
        l, n = self.convert(space)
        spaces_taken = []
        done = False

        if placing_ships:
            if shooter == 'player':
                for i in range(length):
                    if dir == 'n':
                        self.player_map[l - i][n] = self.ship_space
                        spaces_taken.append(f'{self.letter_list[l - i]}{n + 1}')

                    elif dir == 's':
                        self.player_map[l + i][n] = self.ship_space
                        spaces_taken.append(f'{self.letter_list[l + i]}{n + 1}')

                    elif dir == 'e':
                        self.player_map[l][n + i] = self.ship_space
                        spaces_taken.append(f'{self.letter_list[l]}{n + i + 1}')

                    else:
                        self.player_map[l][n - i] = self.ship_space
                        spaces_taken.append(f'{self.letter_list[l]}{n - i + 1}')

            else:
                for i in range(length):
                    if dir == 'n':
                        self.opponent_map[l - i][n] = self.ship_space
                        spaces_taken.append(f'{self.letter_list[l - i]}{n + 1}')

                    elif dir == 's':
                        self.opponent_map[l + i][n] = self.ship_space
                        spaces_taken.append(f'{self.letter_list[l + i]}{n + 1}')

                    elif dir == 'e':
                        self.opponent_map[l][n + i] = self.ship_space
                        spaces_taken.append(f'{self.letter_list[l]}{n + i + 1}')

                    else:
                        self.opponent_map[l][n - i] = self.ship_space
                        spaces_taken.append(f'{self.letter_list[l]}{n - i + 1}')

            return spaces_taken

        else:
            current_space = self.check_space(space, shooter)  # Icon

            if shooter == 'player':
                if current_space == self.ship_space:
                    self.opponent_map[l][n] = self.hit
                    self.opponent_display_map[l][n] = self.hit
                    keys = self.c_ships.keys()

                    for key in keys:
                        space = f'{self.letter_list[l]}{n + 1}'
                        if space in self.c_ships[key]:
                            ind = self.c_ships[key].index(space)
                            print(f'\nYou hit the opponent\'s {key.name}')
                            sleep(2)

                            del self.c_ships[key][ind]
                            key.hits += 1

                            if key.hits == key.length:
                                done = True
                                save_key = key
                                system('cls')
                                print(self)

                                print(f'You sunk the opponents {key.name}')
                                sleep(2)

                    if done:
                        del self.c_ships[save_key]

                elif current_space == self.blank_space:
                    self.opponent_map[l][n] = self.not_hit
                    self.opponent_display_map[l][n] = self.not_hit
                    print('You missed the enemy\'s ships')
                    sleep(2)

            else:
                print('\nThe enemy is thinking...')
                sleep(randint(2, 5))
                if current_space == self.ship_space:
                    self.player_map[l][n] = self.hit
                    keys = self.p_ships.keys()

                    for key in keys:
                        space = f'{self.letter_list[l]}{n + 1}'
                        if space in self.p_ships[key]:
                            ind = self.p_ships[key].index(space)
                            print(f'\nThe opponent hit your {key.name}')

                            del self.p_ships[key][ind]
                            key.hits += 1

                            if key.hits == key.length:
                                done = True
                                save_key = key
                                system('cls')
                                print(self)

                                print(f'The opponent sunk your {key.name}')
                                sleep(2)

                    if done:
                        del self.p_ships[save_key]

                elif current_space == self.blank_space:
                    self.player_map[l][n] = self.not_hit
                    print('The enemy missed your ships')

    def convert(self, space):
        space = list(space)
        l = self.letter_list.index(space[0])

        if len(space) == 2:
            n = space[1]
        elif len(space) == 3:
            n = space[1] + space[2]
        n = int(n) - 1

        return l, n

    # Player Ship Placing and Rules
    def place_ships(self):
        c = 0
        names = [Ship(2, 'Destroyer'), Ship(3, 'Submarine'), Ship(3, 'Cruiser'), Ship(4, 'Battleship'),
                 Ship(5, 'Carrier')]

        for i in [2, 3, 3, 4, 5]:
            print(self)
            print(f'\nYou are now going to place the {names[c].name} (Length-{i})')
            space, dir = self.validate_space('player', i, True)
            self.p_ships[names[c]] = self.change_space(space, 'player', placing_ships=True, dir=dir, length=i)

            c += 1

    def place_com_ship(self):
        space, dir = self.validate_space('com', placing_ships=True)
        l, n = self.convert(space)
        n = int(n)

        names = [Ship(2, 'Destroyer'), Ship(3, 'Submarine'), Ship(3, 'Cruiser'), Ship(4, 'Battleship'),
                 Ship(5, 'Carrier')]

        for length in self.lens_for_com:
            print('\nThe opponent is deciding where to place their ships...')
            if dir == 'n':
                if (l - (length - 1)) < 0:
                    return self.place_com_ship()

                else:
                    for i in range(0, length):
                        if self.opponent_map[l - i][n] == self.ship_space:
                            return self.place_com_ship()

            elif dir == 's':
                if (l + (length - 1)) > 9:
                    return self.place_com_ship()

                else:
                    for i in range(0, length):
                        if self.opponent_map[l + i][n] == self.ship_space:
                            return self.place_com_ship()

            elif dir == 'e':
                if (n + (length - 1)) > 9:
                    return self.place_com_ship()

                else:
                    for i in range(0, length):
                        if self.opponent_map[l][n + i] == self.ship_space:
                            return self.place_com_ship()

            elif dir == 'w':
                if (n - (length - 1)) < 0:
                    return self.place_com_ship()

                else:
                    for i in range(0, length):
                        if self.opponent_map[l][n - i] == self.ship_space:
                            return self.place_com_ship()

            self.c_ships[names[self.c]] = self.change_space(space, 'com', placing_ships=True, dir=dir, length=length)
            self.c += 1

            del self.lens_for_com[0]
            print(self)
