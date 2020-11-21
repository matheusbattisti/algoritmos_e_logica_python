idade = int(input("Qual é a sua idade? "))

if idade >= 18:
  print("Você pode entrar na balada.")

  metodo_de_pagamento = input("Como você vai pagar a entrada? ")

  if metodo_de_pagamento == "dinheiro":
    print("A fila do dinheiro é a número 1")
  else:
    print("A fila de cartão é a número 2")

else:
  print("Você NÃO pode entrar na balada.")