renda = float(input("Digite a sua renda: "))

print(renda)

limite = 0

if renda < 2000:
  limite = 1000
elif renda < 4000:
  limite = 2000
elif renda < 10000:
  limite = 3000
elif renda > 10000:
  print("Você precisa falar com o nosso gerente")
  limite = 3000

print("O seu cartão foi aprovado, e o limite é de R$%d" % limite)