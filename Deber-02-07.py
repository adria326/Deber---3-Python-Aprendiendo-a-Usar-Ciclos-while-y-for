VocalAcento = input("Ingresa una cadena de texto: ")
vocales = "aeiouáéíóú"
contador = 0
for char in VocalAcento.lower():
    if char in vocales:
        contador += 1
print("vocales (acentuadas):", contador)