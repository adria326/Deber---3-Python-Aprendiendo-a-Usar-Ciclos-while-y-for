Numeros = [2, 4, 10, 40, 55]
NumeroMenor = Numeros[0]
for Numero in Numeros:
    if Numero < NumeroMenor:
        NumeroMenor = Numero
print("numero menor:", NumeroMenor)