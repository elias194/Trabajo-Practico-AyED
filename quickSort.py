def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivote = lista[0]

    menores = []
    mayores = []

    for i in range(1, len(lista)):
        if lista[i] < pivote:
            menores.append(lista[i])
        else:
            mayores.append(lista[i])

    return quick_sort(menores) + [pivote] + quick_sort(mayores)

n = int(input("Ingrese el tamaño del vector:"))
numeros = [int()] * n
for i in range(n):
    numeros[i] = int(input())
resultado = quick_sort(numeros)

print(resultado)