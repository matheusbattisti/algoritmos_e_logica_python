class Pessoa:
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade

  def falar(self):
    print("Olá galera!")

class Superheroi(Pessoa):
  def __init__(self, nome, idade, super_poder):
    super().__init__(nome, idade)
    self.super_poder = super_poder

  def utilizar_super_poder(self):
    print("O herói utilizou o %s" % self.super_poder)


joao = Pessoa("João", 21)

joao.falar()

matheus = Superheroi("Matheus", 29, "Raio laser")

matheus.falar()

matheus.utilizar_super_poder()

print(joao.idade)

print(matheus.idade)