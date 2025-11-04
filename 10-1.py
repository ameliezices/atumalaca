a = int(input("Digite um valor inteiro positivo: "))
b = int(input("Digite um segundo valor inteiro positivo: "))

def mdc(a, b):
    if a <= 0 or b <= 0:
        print("Ambos os números devem ser inteiros positivos!")

    while b != 0:
        a, b = b, a % b
    return a

print(f"O MDC entre {a} e {b} é {mdc(a, b)}")