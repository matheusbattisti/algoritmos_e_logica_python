carro_a = ["BMW", 50000]
carro_b = ["Ferrari", 60000]
carro_c = ["VW", 45000]

carros = [carro_a, carro_b, carro_c]

print(carros)

print(carros[0][0])

print(carros[0][1])

print(carros[2][0])

for carro in carros:
  print("A marca do carro é: %s" % carro[0])