ano = int(input("Insira um valor inteiro para representar o ano: "))
if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
    print("Este ano é bissexto.")
else:
    print("Este ano não é bissexto.")