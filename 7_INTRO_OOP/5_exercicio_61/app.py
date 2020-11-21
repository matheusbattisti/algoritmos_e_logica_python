class Carro:
  def __init__(self, marca, valor, numero_de_portas, tanque):
    self.marca = marca
    self.valor = valor
    self.numero_de_portas = numero_de_portas
    self.tanque = tanque

  def abastecer(self, litros):
    if self.tanque >= 100:
      print("Tanque está cheio")
    else:
      self.tanque += litros
      if self.tanque > 100:
        self.tanque = 100

  def dirigir(self, km):
    km_por_litro = 10
    self.tanque -= (km / km_por_litro)

fusca = Carro("VW", 15000, 4, 80)

print(fusca.marca)

fusca.abastecer(100)

print(fusca.tanque)

fusca.dirigir(100)

print(fusca.tanque)

fusca.abastecer(10)

print(fusca.tanque)
