# coding=utf-8

class igra:
    def __init__(self, position = [1, 3, 5, 7]):
        self.position = position
        self.player = None
    
    def move(self, row, num):
        '''Funkcija z validacijskimi metodami preveri pravilnost vnesenih podatkov. Če so podatki pravilni vrne 'Input is valid', sprejme vrstico in število oduzetih palic iz taiste vratice ter nato spremeni pozicijo na plošči. '''
        
        if self.validation_row(row) == 'Row invalid':
            return 'Row invalid'
        elif self.validation_num(row, num) == 'Num invalid':
            return 'Num invalid'
        
        self.position[int(row) - 1] = int(self.position[int(row) - 1]) - int(num)

        return 'Input is valid'


    def end(self):
        '''Funkcija se zažene na začetku vsakega kroga kjer preveri ali je na plošči ostala le še ena palica in je torej igra končana. Ča je slednje res vrne True, v nasprotnem primeru pa False.  '''
        
        sum = 0
        for points in self.position:
            sum += points
        
        if sum == 1:
            return True
        else:
            return False

    def change_player(self):
        '''Funkcija ničesar ne sprejme ali vrne. Spremeni igralca na vrsti, v kolikor pa ta še ni določen (na začetku igre) ga nastavi na 'player1'.'''
        
        if self.player == 'player1':
            self.player = 'player2'
        elif self.player == 'player2':
            self.player = 'player1'
        elif self.player == None:
            self.player = 'player1'

    # validacijske funkcije

    def validation_row(self, row):
        try:
            float(row)
        except:
            return 'Row invalid'

        row = float(row)

        if row.is_integer():
            if 0 < row and row <= len(self.position) and self.position[int(row) - 1] != 0:
                return 'Row is valid'
            else:
                return 'Row invalid'
        else:
            return 'Row invalid'
    
    def validation_num(self, row, num):
        try:
            float(num)
        except:
            return 'Num invalid'

        num = float(num)
        row = int(row)

        if num.is_integer():
            if num > 0 and num <= self.position[row - 1]:
                return 'Num is valid'
            else:
                return 'Num invalid'
        else:
            return 'Num invalid'

       

