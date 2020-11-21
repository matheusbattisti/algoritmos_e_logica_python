escopo_global = "Tchau"
numero = 10

def teste():
  teste = "Olá"
  numero = 10
  print(teste)
  print(escopo_global)
  if numero == 10:
    print("Você ganhou!")

teste()

escopo_global = "Até logo"
numero = 12

teste()

print(numero)

def testando():
  numero = 50
  print(numero)

testando()
teste()
