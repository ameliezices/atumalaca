n = int(input("Insira a quantidade de elemento que a lista deverá possuir (2 ou mais!): "))
lista = []
if n <= 1:
    print("Usuário inseriu uma quantidade inválida. Programa encerrado.")
else:
    for i in range(n):
        lista.append(int(input(f"Insira o valor {i + 1}: ")))
    if % 2 == 0:
        lista.remove()
    print(lista)