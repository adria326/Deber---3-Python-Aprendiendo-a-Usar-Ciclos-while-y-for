Altura = int(input("Ingresa la altura de la pirámide: "))

for i in range(1, Altura + 1):
    print(' ' * (Altura - i), end='')
    print('*' * (2 * i - 1))