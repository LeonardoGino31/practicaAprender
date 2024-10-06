import random as rd

strPrueba = "Hola como esta"
strPrueba2 = "Hi how are you"
count = 3
listaPruba = ["ho"]

while count > 0:
    aleatorio = rd.randint(0, len(strPrueba2) - 1)  # Corregido aquí
    listaPruba.append(strPrueba2[aleatorio])
    count -= 1  # Decrementar el contador para que el bucle termine

for char in listaPruba:
    print(char)
