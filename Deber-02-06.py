Numero = int(input("tabla de multiplicar: "))
print(f"Tabla de multiplicar del {Numero}:")
for i in range(1, 11):
    respuesta = Numero * i
    print(f"{Numero} x {i} = {respuesta}")