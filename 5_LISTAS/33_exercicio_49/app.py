carro = {
  "pneus": 4,
  "portas": 2,
  "motor": 1,
  "janelas": 4
}

print(carro)

carro["teto solar"] = 1

print(carro)

print(carro["teto solar"])

del carro["motor"]
del carro["janelas"]

print(carro)