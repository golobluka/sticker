Sticker
=======

Opis razreda igra
--------------------

V razredu igra so naslednje funkcije:  

1. move(vrstica v kateri so bile kate oduzete (int), število oduzetih kart (int)) vrne: 'Input is valid', če sta vrstica in število veljavna sicer pa 'Row invalid' ob naveljavni vrstici in 'Num invalid' ob neveljavnem številu oduzetih kart
2. move_maschine(difficulty ('biginner' oz. 'advanced')) - Vrne: Trimestni nabor. Na prvem mestu je opisni string (glej move() z dodatkom 'Difficulty invalid') na drugem vrstica premika in tretjem število oduzetih palic.
3. end() - vrne:(če je igra končana True sicer pa False (boolean))
4. change_player() - zamenja igralca in ne vrne ničesar  

Razredne spremenjivke:  

1. position (list) - po vrsti število kart v posamezni vrstici
2. player (str) - 'player1' oz. 'player2'

Validacijske funkcije:

1. validation_num(row, num) -  Preveri ali je vnos številski, če ga lahko brez krajšanj pretvorimo v celo število (int) in če je v pravilnih mejah. Vrne stringa 'Num is valid' oz. 'Num invalid'
2. validation_row(row) -  Preveri ali je vnos številski, če ga lahko brez krajšanj pretvorimo v celo število (int) in če je v pravilnih mejah. Vrne stringa 'Row is valid' oz. 'Row invalid'
3. validation_difficulty(difficulty) - Preveri ali je vnos težavnosti pravilno zapisan. Če ni, vrne 'Difficulty invalid' sicer pa 'Difficulty is valid'




