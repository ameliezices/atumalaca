sequencia = input("Insira uma sequência de valores inteiros, separando-os por espaços: ")
numeros = sequencia.split( )
lista = []
for i in numeros:
    lista.append(int(i))
    media = sum(lista) / len(lista)
print(f"A média da sequência é: {media}")