'''
4. Feladat
Írj egy programot, amely a felhasználótól bekér 3 szót, ezeket egy listában tárolja, és egy eljárás segítségével meghatározza, és a képernyőre kiírja, melyik a legrövidebb szó!
'''
lista=[]
for i in range(3):
    lista.append(input('szo: '))

def rovidebb():
    print(min((szo for szo in lista if szo), key=len))

rovidebb()