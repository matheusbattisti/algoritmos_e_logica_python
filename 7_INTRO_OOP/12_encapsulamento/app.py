class Aviao:
  __asas = 2

  def __init__(self, marca):
    self.marca = marca

  def mostrar_asas(self):
    print("O avisão tem %d asas" % self.__asas)


aviao = Aviao("Aviões Hora de Codar")

print(aviao.marca)

aviao.mostrar_asas()

