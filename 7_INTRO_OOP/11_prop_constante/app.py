class Carro:

  rodas = 4

  def __init__(self, marca):
    self.marca = marca

ferrari = Carro("Ferrari")

print(ferrari.marca)
print(ferrari.rodas)