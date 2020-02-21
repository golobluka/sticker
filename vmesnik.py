
import sticker

igraj = sticker.igra()


# Writing tools.

STICK = ' |'
SEP = '_______________________________'

def position_show(position):
        offset = 6

        
        print( '\n' + str(igraj.player) + '. igralec')
        print(SEP + '\n')

        for points in position:
            print(' ' * offset + ' ' + STICK * points)
            if offset > 0:
                offset -= 2

        print(SEP)

# Here starts the game loop.

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


print('Konec igre' + '\n' + SEP)
position_show(igraj.position)




