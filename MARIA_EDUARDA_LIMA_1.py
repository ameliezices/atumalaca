n = int(input("Entre com um número inteiro positivo n: "))
soma = 0
for i in range(1, n + 1):
    if n - (i - 1) != 0:
        soma += n - (i - 1) / i
    else:
        soma += 1
print(f"O valor da soma é {soma}")