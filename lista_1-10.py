print("Montaremos uma lista e observaremos se ela está sendo apresentada em ordem crescente ou decrescente.")
numero = int(input("Insira a quantidade de elementos da lista: "))
lista = []
for i in range(numero):
    lista.append = float(input(f"Defina o elemento {i + 1}: "))
print(f"A lista foi definida como {lista}.")
crescente = True
for i in range(len(lista) - 1):
    if lista[i] > lista[i + 1]:
        crescente = False
if crescente:
    print("A lista está ordenada em ordem crescente.")
else:
    print("A lista não está ordenada em ordem crescente.")