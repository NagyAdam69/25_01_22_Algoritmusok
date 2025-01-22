'''
Az ELDÖNTÉS esetében azt vizsgáljuk,
hogy szerepel-e egy bizonyos tulajdonságú elem az adatsorban (itt a listában).

A program azt vizsgálja, hogy van-e hárommal osztható szám a listában.
'''
lista = [2, 5, 4, 8, 9, 11, 10, 12]

osztaho_harommal = []
index = 0
while index < len(lista):
    if lista[index] % 3 == 0:
        oszthato_harommal.append(lista[index])
    index = index + 1

if len(oszhato_harommal) > 0:
    print(f'Van a listában hárommal osztható szám, amik a {oszhato_harommal}.')
else:
    print('Nincs a listában hárommal osztható szám.')
    
    
    