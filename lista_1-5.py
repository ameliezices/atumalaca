temperatura = float(input("Insira o valor númerico da temperatura: "))
FouC = str(input("Digite 'F' para Fahrenheit ou 'C' para Celsius: ")).upper()
print(f"A temperatura é de {temperatura} {FouC}.")
print("Convertendo-a para a outra unidade de medida...")
if FouC == "C":
    conversao = (5/9) * (temperatura - 32)
    print(f"A nova temperatura é de {conversao} F.")
elif FouC == "F":
    conversao = (temperatura * (9/5)) + 32
    print(f"A nova temperatura é de {conversao} C.")
else:
    print("Usuário informou os dados incorretamente. Programa finalizado.")