print("Vamos montar um triângulo.")
a = float(input("Digite o valor correspondente ao seu lado 'a': "))
b = float(input("Digite o valor correspondente ao seu lado 'b': "))
c = float(input("Digite o valor correspondente ao seu lado 'c': "))
if a == b == c:
    print("Estamos trabalhando com um triângulo equilátero.")
elif (a == b != c) or (a == c != b) or (b == c != a):
    print("Estamos trabalhando com um triângulo isósceles.")
else:
    print("Estamos trabalhando com um triângulo escaleno.")
s = (a + b + c)/2
area = (s * (s - a) * (s - b) * (s - c)) ** (1/2)
print(f"A área deste triângulo é {area}.")