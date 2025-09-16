#Programa que imprima o desenho de um triângulo retângulo isósceles, com catetos de tamanho dado.
cateto = int(input("Entre com o tamanho dos catetos que são iguais: "))
caractere = str(input("Entre com o caractere a ser utilizado: "))
for i in range(cateto + 1):
    print(caractere * i)
