#Lendo um número inteiro positivo n
n = int(input("Entre com o número inteiro positivo n: "))
'''
É possível reescrever a soma como:
    (2 + 4 + 6 + ... + n) - (1 + 3 + 5 + ... + (n - 1)), se n for par.
    (2 + 4 + 6 + ... + (n - 1)) - (1 + 3 + 5 + ... + n), se n for ímpar.
    
Além disso, cada termo i contribui com (-1)**i * i. Isto é:
    Se i é ímpar = -i
    Se i é par = +i
'''
soma = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        soma += i
    else:
        soma -= i
#Mostrando o resultado
print(f"Soma: {soma}")