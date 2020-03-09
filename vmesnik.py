# coding=utf-8

import sticker

game = sticker.Sticker()
id_igre = game.new_game()
igra = game.igre[id_igre]


# Writing tools.

STICK = ' |'
SEP = '_______________________________'

def position_show(position):
        offset = 6

        
        print( '\n' + str(igra.player))
        print(SEP + '\n')

        for points in position:
            print(' ' * offset + ' ' + STICK * points)
            if offset > 0:
                offset -= 2

        print(SEP)

# Here starts the game loop.
game_end = False

while not game_end:
    position_show(igra.position)

    while True:
        row = input('Vpiši vrstico oduzema:')
        num = input('Vpiši še število oduzetih palic:')

        stanje = igra.move(row, num)
        if stanje == 'Input is valid':
            break
        elif stanje == 'Game over, winner is {}'.format(igra.player):
            game_end = True
            break
        elif stanje == 'Row invalid':
            print('Vnos vrstice je neveljaven!')
        elif stanje == 'Num invalid':
            print('Vnos števila odvzetih kart je neveljaven!')




position_show(igra.position)
print('\nKonec igre! Zmagovalec je:' + igra.player + '\n' + SEP)




