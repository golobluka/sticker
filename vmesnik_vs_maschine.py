# coding=utf-8

import sticker
import time

game = sticker.Sticker()
id_igre = game.new_game()
igra = game.igre[id_igre]


# Writing tools.

STICK = ' |'
SEP = '_______________________________'

def position_show(position):
        offset = 6
        numero = 1

        
        
        print(SEP + '\n')

        for points in position:
            print(str(numero) + ' ' * offset + ' ' + STICK * points)
            if offset > 0:
                offset -= 2
            numero += 1

        print(SEP)

def thinking(rounds):

    while(rounds > 0):
        time.sleep(1)
        print(STICK)
        rounds -= 1
    
    print()
    


#   Here starts the game loop.
game_end = False

while not game_end:
    
    
    position_show(igra.position)

    # while True:
    #     row = input('Vpiši vrstico oduzema:')
    #     num = input('Vpiši še število oduzetih palic:')

    #     stanje = igra.move(row, num)
    #     if stanje == 'Input is valid':
    #         break
    #     elif stanje == 'Game over, winner is {}'.format(igra.player):
    #         game_end = True
    #         break
    #     elif stanje == 'Row invalid':
    #         print('Vnos vrstice je neveljaven!')
    #     elif stanje == 'Num invalid':
    #         print('Vnos števila odvzetih kart je neveljaven!')

    # Now maschine plays against mashine.

    while True and not game_end:
        thinking(3)
        stanje, row_m, num_m = igra.move_maschine('advanced')
        if stanje == 'Input is valid':
            break
        elif stanje == 'Game over, winner is {}'.format(igra.player):
            game_end = True
            break
        elif stanje == 'Row invalid':
            print('Row {} and num {}'.format(row_m, num_m))
            print('Vnos vrstice je neveljaven!')
        elif stanje == 'Num invalid':
            print('Row {} and num {}'.format(row_m, num_m))
            print('Vnos števila odvzetih kart je neveljaven!')
        elif stanje == 'Difficulty invalid':
            print('Težavnostna stopnja je neveljavna!')

    
    position_show(igra.position)



    while True and not game_end:
        thinking(3)
        stanje, row_m, num_m = igra.move_maschine('advenced')
        if stanje == 'Input is valid':
            break
        elif stanje == 'Game over, winner is {}'.format(igra.player):
            game_end = True
            break
        elif stanje == 'Row invalid':
            print('Row {} and num {}'.format(row_m, num_m))
            print('Vnos vrstice je neveljaven!')
        elif stanje == 'Num invalid':
            print('Row {} and num {}'.format(row_m, num_m))
            print('Vnos števila odvzetih kart je neveljaven!')
        elif stanje == 'Difficulty invalid':
            print('Težavnostna stopnja je neveljavna!')

    




print('Konec igre' + '\n' + SEP)
position_show(igra.position)
