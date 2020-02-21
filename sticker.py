


class igra:
    def __init__(self, position = [1, 3, 5, 7]):
        self.position = position
        self.player = 1
    
    def poteza(self, row, num):
        self.position[int(row) - 1] = int(self.position[int(row) - 1]) - int(num)

        if self.player == 1:
            self.player = 2
        elif self.player == 2:
            self.player = 1

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
        sum = 0
        for points in self.position:
            sum += points
        
        if sum == 1:
            return True
        else:
            return False
