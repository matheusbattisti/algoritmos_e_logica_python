nome = input("Digite o seu nome: ")

if nome == "Matheus":
  print("Olá, você é um admin!")

  if 5 > 10:
    print("Testando")
  elif 10 > 5:
    print("Caiu aqui!")

elif nome == "João":
  print("Olá, você um produtor de conteúdo!")
else:
  print("Você é um usuário comum!")


numero = int(input("Digite um número: "))

if numero > 0 and numero <= 5:
  print("Maior que 0")
elif numero > 5 and numero <= 10:
  print("Maior que 5")
elif numero > 10 and numero <= 20:
  print("Maior que 10")
elif numero > 20:
  print("Maior que 20")
else:
  print("Numero negativo")