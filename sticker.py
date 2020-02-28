


class igra:
    def __init__(self, position = [1, 3, 5, 7]):
        self.position = position
        self.player = None
    
    def poteza(self, row, num):
        '''Funkcija sprejme vrstico in število oduzetih palic iz taiste vratice ter nato spremeni pozicijo na plošči. '''
        self.position[int(row) - 1] = int(self.position[int(row) - 1]) - int(num)

       
    def available_row(self, row):

        if row > len(self.position):
            print('Vrstica je izven obsega!')
            return False
        elif self.position[row -1] == 0:
            print('Vrstica je že prazna!')
            return False
        else:
            return True
    def available_number(self, row, num):
        if num > self.position[row -1]:
            print('V tej vrsti ni toliko vžigalic!')
            return False
        else:
            return True

    def end(self):
        '''Funkcija se zažene na začetku vsakega kroga kjer najprej določi igralca, ki je na vrsti.Nato preveri ali je na plošči ostala le še ena palica in je torej igra končana. Ča je slednje res vrne True in igralca, ki je izgubil, v nasprotnem primeru pa False in igralca, ki bo na vrsti v nasledni potezi.  '''
        
        self.change_player()
        
        sum = 0
        for points in self.position:
            sum += points
        
        if sum == 1:
            return (True, self.player)
        else:
            return (False, self.player)

    def change_player(self):
        '''Funkcija ničesar ne sprejme ali vrne. Spremeni igralca na vrsti, v kolikor pa ta še ni določen (na začetku igre) ga nastavi na 'player1'.'''
        if self.player == 'player1':
            self.player = 'player2'
        elif self.player == 'player2':
            self.player = 'player1'
        elif self.player == None:
            self.player = 'player1'
