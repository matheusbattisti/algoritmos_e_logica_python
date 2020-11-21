class Carro:
  def __init__(self, portas, motor, teto_solar, marca, preco):
    self.portas = portas
    self.motor = motor
    self.teto_solar = teto_solar
    self.marca = marca
    self.preco = preco

polo = Carro(4, 1.0, True, "VW", 70000)

print(polo.preco)
print(polo.marca)

ferrari = Carro(2, 3.0, True, "Ferrari", 250000)

print(ferrari.marca)
print(ferrari.teto_solar)