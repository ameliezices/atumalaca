#Usuário deve inserir dois números inteiros nas váriaveis x e y
x = int(input("Insira um valor inteiro para x: "))
y = int(input("Insira um valor inteiro para y: "))
#Trocar o valor de x por y e vice-versa
x, y = y, x
print(f"O novo valor de x é {x}.")
print(f"O novo valor de y é {y}.")