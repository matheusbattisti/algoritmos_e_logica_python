class Carro:
  def __init__(self, marca, preco):
    self.marca = marca
    self.preco = preco

  def ligar(self):
    print("Vrummmm")

  def mudar_preco(self, novo_preco):
    self.preco = novo_preco

polo = Carro("VW", 60000)

print(polo.marca)

polo.ligar()

polo.mudar_preco(90000)

print(polo.preco)