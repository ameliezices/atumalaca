n = int(input("Insira a quantidade de elementos que a lista deverá possuir (2 ou mais!): "))
lista = []
if n <= 1:
  print("Usuário inseriu uma quantidade inválida.")
else:
  for i in range(n):
    lista.append(int(input(f"Insira o valor {i + 1}: ")))
  i = 0
  while i < len(lista):
    if lista[i] % 2 == 0:
      del lista[i]
    else:
      i += 1
  print(lista)
