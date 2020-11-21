salario = float(input("Digite o salário: "))
aumento = int(input("Digite a porcentagem de aumento: "))

print(salario)
print(aumento)

novo_salario = salario + (salario * (aumento/100))

print("O novo salário é de R$%.2f" % novo_salario)