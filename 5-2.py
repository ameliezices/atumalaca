#Definindo a quantidade de elementos pertencentes à lista
quantidade = int(input("Insira a quantidade de elementos que a lista deve possuir: "))
#Definindo a lista
lista = []
for i in range(quantidade):
    elemento = int(input("Insira um elemento à lista: "))
    lista.append(elemento)
    if elemento % 2 == 0:
        lista.remove(elemento)
print("Gerando nova lista...")
print(lista)
