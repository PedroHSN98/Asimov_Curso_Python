#Desafio1
#Converta o loop abaixo para uma comprrensão de lista:

valores = [30, 50, 100, 120]

#triplos = [valor * 3 for valor in valores]

triplos = []
for valor in valores:
    triplo = valor * 3
    triplos.append(triplo)

print(triplos)