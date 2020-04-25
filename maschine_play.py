import random

ZGUBLJENE_POZICIJE = [((1, 1),)]
DOBLJENE_POZICIJE = [((1, 2),)]


def analiza(position):
    
    drevesa_moznosti = {}
    drevo_tockovanja1 = {}
    drevo_moznosti1 = {}

    pos_nabor = zapis_nabor(position)
    if pos_nabor == ((1,1),):
        return ((0,1),)

    drevo_moznosti1 = mozne_poteze(pos_nabor)
    drevesa_moznosti[1] = drevo_moznosti1

    drevo_moznosti1 = {}

    #Iskanje v globino

    for nabor_stopnje_1 in drevesa_moznosti[1]:
        if nabor_stopnje_1 in ZGUBLJENE_POZICIJE:
            return nabor_stopnje_1
        elif nabor_stopnje_1 in DOBLJENE_POZICIJE:
            pass
        else:
            drevo_moznosti1[nabor_stopnje_1] = mozne_poteze(nabor_stopnje_1)
    
    if set(drevo_moznosti1.keys()) == set():
        return random.choice(drevesa_moznosti[1])
    
    drevesa_moznosti[2] = drevo_moznosti1
    drevo_moznosti1 = {}


    for nabor_stopnje_1,  seznam_naborov_stopnje_2 in drevesa_moznosti[2].items():
        drevo_tockovanja1[nabor_stopnje_1] = 0
        for nabor_stopnje_2 in seznam_naborov_stopnje_2:
            if nabor_stopnje_2 in ZGUBLJENE_POZICIJE:
                drevo_tockovanja1[nabor_stopnje_1] -= 16
            elif nabor_stopnje_2 in DOBLJENE_POZICIJE:
                drevo_tockovanja1[nabor_stopnje_1] += 4
            else:
                pass

        if drevo_tockovanja1[nabor_stopnje_1]  == len(seznam_naborov_stopnje_2) * 4:
            return nabor_stopnje_1
        elif drevo_tockovanja1[nabor_stopnje_1] == len(seznam_naborov_stopnje_2) * (-16):
            break
        else:
            break
    
    
    # Točkovanje
    
    maksimum = -100
    for tocke in drevo_tockovanja1.values():
        maksimum = max(maksimum, tocke)

    izbrane_pozicije = []
    for pos_mat, tocke in drevo_tockovanja1.items():
        if tocke >=  maksimum - 4:
            izbrane_pozicije.append(pos_mat)
    
    return random.choice(izbrane_pozicije)

            



def mozne_poteze(pos_nabor):
    pridobljene_pozicije = []

    pos_mat = set(pos_nabor)

    if pos_mat == {(1,1)}:
        return ((0,1),)

    
    for nabor1 in pos_mat:
    
        for st_oduzetih in range(1, nabor1[0]):
            zacasni_nabor = tuple([nabor1[0] - st_oduzetih, 1])
            stikalo = False
            for nabor2 in pos_mat:
                if nabor2[0] == zacasni_nabor[0]:
                    stikalo = True
                    if nabor1[1] == 1:
                        pridobljene_pozicije.append(tuple((pos_mat - {nabor1, nabor2}) | {tuple([nabor2[0], nabor2[1] + 1])}))
                    else:
                        pridobljene_pozicije.append(tuple((pos_mat - {nabor1, nabor2}) | {tuple([nabor2[0], nabor2[1] + 1])    } | {tuple([nabor1[0], nabor1[1] - 1])}))
            if stikalo == False:
                if nabor1[1] == 1:
                    pridobljene_pozicije.append(tuple((pos_mat - {nabor1}) | {tuple([zacasni_nabor[0], 1])}))
                else:
                    pridobljene_pozicije.append(tuple((pos_mat - {nabor1}) | {tuple([zacasni_nabor[0], 1])    } | {tuple([nabor1[0], nabor1[1] - 1])}))
        if len(pos_mat) == 1 and nabor1[1] == 1:
            pass
        else:
            if nabor1[1] == 1:
                pridobljene_pozicije.append(tuple(pos_mat - {nabor1}))
            else:
                pridobljene_pozicije.append(tuple((pos_mat - {nabor1}) | {tuple([nabor1[0], nabor1[1] - 1])}))
    
    return pridobljene_pozicije






def zapis_povezav(position):
    pos_povezav = [] 
    for count in range(1, len(position) + 1):
        if position[count - 1] != 0:
            pos_povezav.append((position[count - 1], count))
    
    return sorted(pos_povezav)

def zapis_mat(position):
    zapis = set()
    
    for st_kart in range(1, max(position) + 1):
        if position.count(st_kart) != 0:
            zapis.add((st_kart, position.count(st_kart)))
    
    return zapis


def zapis_nabor(position):
    return tuple(zapis_mat(position))

def zapis_position(pos_mat):
    position = []
    for nabor in pos_mat:
        for count in range(nabor[1]):
            position.append(nabor[0])
    return position




def maschine(position, difficulty):
    nova_pozicija_nabor = analiza(position)

    pozicija_nabor = zapis_nabor(position)
    seznam_povezav = zapis_povezav(position)
    nova_pozicija_mat = set(nova_pozicija_nabor)
    nova_pozicija = zapis_position(nova_pozicija_mat)
    palice_na_koncu = None

    for stevilo_palic in range(1, max(position) + 1):
        if nova_pozicija.count(stevilo_palic) < position.count(stevilo_palic):
            palice_na_zacetku = stevilo_palic
        elif nova_pozicija.count(stevilo_palic) > position.count(stevilo_palic):
            palice_na_koncu = stevilo_palic

    if palice_na_koncu == None:
        palice_na_koncu = 0
    
    
    for povezava in seznam_povezav:
        if povezava[0] == palice_na_zacetku:
            return (povezava[1], palice_na_zacetku - palice_na_koncu)




