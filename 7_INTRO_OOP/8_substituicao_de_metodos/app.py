class Pessoa:
  def falar(self):
    print("Olá pessoal!")

class Matheus(Pessoa):
  def falar(self):
    print("Olá pessoal, eu sou o Matheus!")

class Roberto(Pessoa):
  pass


matheus = Matheus()

matheus.falar()

roberto = Roberto()

roberto.falar()