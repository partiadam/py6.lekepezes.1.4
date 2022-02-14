'''
1.4 Feladat
Készíts egy programot, amely sztringeket tartalmazó listaelemek leképezését valósítja meg.  
A program írja ki az eredeti és a generált listát is a képernyőre!
'''


lista1 = ['alma', 'kutya', 'leves', 'zsiraf']

lista2 = [szo.ljust(6, 'f')for szo in lista1]
print(lista2)