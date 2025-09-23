print("Construiremos um triângulo de lados constituídos por valores inteiros.")
x = int(input("Informe o valor do lado 1: "))
y = int(input("Informe o valor do lado 2: "))
z = int(input("Informe o valor do lado 3: "))
if (x + y <= z) or (x + z <= y) or (y + z <= x):
    print("Não é possível construir um triângulo com estes valores.")
else:
    if (x == y == z):
        print("Este triângulo é equilátero.")
    elif (x != y == z) or (y != x == z) or (z != x == y):
        print("Este triângulo é isósceles.")
    else:
        print("Este triângulo é escaleno.")