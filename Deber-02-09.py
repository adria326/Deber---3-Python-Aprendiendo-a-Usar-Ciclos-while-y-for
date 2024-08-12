NumeroTerminos = int(input("número de términos en la serie de Fibonacci: "))
def fibonacci(N):
    serie = []
    a, b = 0, 1
    while len(serie) < N:
        serie.append(a)
        a, b = b, a + b
    return serie
serieFibonacci = fibonacci(NumeroTerminos)
print("serie de Fibonacci ", NumeroTerminos, "términos es:", serieFibonacci)