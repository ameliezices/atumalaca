quantidade = 3
lista = []

for i in range(quantidade):
    valor = int(input(f"Digite o {i+1}º valor: "))
    lista.append(valor)
    print(f"i vale: {i}, valor digitado: {valor}")

print(f"Lista final: {lista}")