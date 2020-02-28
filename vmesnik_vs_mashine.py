# coding=utf-8

import sticker
import time, mashine_play

igraj = sticker.igra()


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

while not igraj.end():
    
    
    position_show(igraj.position)

    while True:
        row = int(input('Vpiši vrstico oduzema:'))
        if igraj.available_row(row):
            break
    
    while True:
        num = int(input('Vpiši še število oduzetih palic:'))
        if igraj.available_number(row, num):
            break
    igraj.poteza(row, num)
    position_show(igraj.position)

    # Part when mashine thinks.

    thinking(3)

    num2, row2 = mashine_play.move(igraj.position)
    igraj.poteza(row2, num2)



print('Konec igre' + '\n' + SEP)
position_show(igraj.position)
