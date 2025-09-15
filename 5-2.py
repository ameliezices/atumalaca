#Definindo a quantidade de elementos pertencentes à lista
quantidade = int(input("Insira a quantidade de elementos que a lista deve possuir: "))
#Definindo a lista
lista = []
for elementos in range(quantidade):
    lista.append(int(input("Insira um elemento à lista: ")))
    if (elementos%2==0):
    lista.remove(elementos)
print(Gerando nova lista...)
print(lista)