# coding=utf-8

import random

def move(position):
    pos = changed_write(position)

    if len(pos) == 1:
        return (pos[0][0] - 1, pos[0][1])
    
    elif len(pos) == 2:
        if pos[0][0] == pos[1][0]:
            return (1, pos[0][1])
        elif pos[0][0] == 1:
            return (pos[1][0], pos[1][1])
        elif pos[0][0] < pos[1][0]:
            return (pos[1][0] - pos[0][0], pos[1][1])
        else:
            return (pos[0][0] - pos[1][0], pos[0][1])
    elif len(pos) == 3:
        dic_pos = {}
        for counter in range(1, 10):
            dic_pos[counter] = position.count(counter)

         # Možnosti pri zasedenih treh vrsticah.

        if dic_pos[1] == 1:
            if pos[1][0] == pos[2][0]:
                return (1, pos[0][1])           
            
            elif pos[1][0] % 2 == 0:
                if pos[1][0] + 1 == pos[2][0]:
                    return random.choice([(1, pos[1][1]), (2, pos[2][1])])
                else:
                    return (pos[2][0] - pos[1][0] - 1, pos[2][1])
            
            elif pos[1][0] % 2 == 1:
                return (pos[2][0] - pos[1][0] + 1, pos[2][1])

        elif dic_pos[1] == 2:
            return (pos[2][0] - 1 , pos[2][1])
        
        elif dic_pos[1] == 3: 
            return (1, pos[1][0])

        elif dic_pos[2] == 1:
            if pos[1][0] == pos[2][0]:
                return (pos[0][0], pos[0][1])
            
            elif pos[1][0] == 3:
                return (pos[2][0] - 1, pos[2][1])
            
            elif pos[1][0] == 4 and pos[2][0] == 5:
                return (1, pos[0][1])
            elif pos[1][0] == 4 and pos[2][0] == 6:
                return random.choice([(1, pos[0][1]), (1, pos[2][1]) ])
            
        elif dic_pos[2] == 2 or dic_pos[2] == 3:
            return (pos[2][0], pos[2][1])
        else:
            pozicija = random.choice([x[1] for x in pos])
            stevilo = random.choice([x[0] for x in pos])
            delez = random.choice(range(1, stevilo + 1))
            return (delez, pozicija)
        
    else:
        pozicija = random.choice([x[1] for x in pos])
        stevilo = random.choice([x[0] for x in pos])
        delez = random.choice(range(1, stevilo + 1))
        return (delez, pozicija)

        









def changed_write(position):
    new_pos = [] 
    for count in range(1, len(position) + 1):
        if position[count - 1] != 0:
            new_pos.append([position[count - 1], count])
    
    return sorted(new_pos)
