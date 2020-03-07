# coding=utf-8

import sticker

igraj = sticker.igra()


# Writing tools.

STICK = ' |'
SEP = '_______________________________'

def position_show(position):
        offset = 6

        
        print( '\n' + str(igraj.player))
        print(SEP + '\n')

        for points in position:
            print(' ' * offset + ' ' + STICK * points)
            if offset > 0:
                offset -= 2

        print(SEP)

# Here starts the game loop.

while not igraj.end():
    igraj.change_player()
    position_show(igraj.position)

    while True:
        row = input('Vpiši vrstico oduzema:')
        num = input('Vpiši še število oduzetih palic:')
       
        if igraj.move(row, num) == 'Input is valid':
            break
        elif igraj.move(row, num) == 'Row invalid':
            print('Vnos vrstice je neveljaven!')
        elif igraj.move(row, num) == 'Num invalid':
            print('Vnos števila odvzetih kart je neveljaven!')




position_show(igraj.position)
igraj.change_player()
print('\nKonec igre! Zmagovalec je:' + igraj.player + '\n' + SEP)




