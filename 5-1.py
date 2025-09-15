#Definindo a quantidade de elementos pertencentes à lista
quantidade = int(input("Insira a quantidade de elementos que a lista deve possuir: "))
#Definindo a lista
lista = [] #Colchetes vazios porque, até então, a lista não está definida
for numeros in range(quantidade):
    lista.append(int(input("Insira um elemento à lista: "))) #Momento em que o usuário define os valores da lista
print(f"Lista com {quantidade} números.")
procurado = int(input("O número a ser procurado é: "))
if procurado in lista: #O programa assume que o número procurado está na lista
    print(f"O número {procurado} é um elemento da lista.")
else: #Caso contrário
    print(f"O número {procurado} não é um elemento da lista.")