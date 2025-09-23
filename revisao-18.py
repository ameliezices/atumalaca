#Lendo um número inteiro positivo n
n = int(input("Entre com um número inteiro positivo n: "))
#Determinando fórmulas fechadas para os somatórios
soma_quadrados = n * (n + 1) * (2*n + 1) / 6
soma_cubos = (n * (n + 1) / 2) ** 2
soma_quarta = n * (n + 1) * (2*n + 1) * (3*n**2 + 3*n - 1) / 30
#Calculando o resultado
resultado = 2 * soma_quadrados + 3 * soma_cubos + 4 * soma_quarta
print(f"O resultado do somatório é: {resultado}")