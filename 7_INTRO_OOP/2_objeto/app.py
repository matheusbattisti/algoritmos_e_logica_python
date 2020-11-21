class Pessoa:
  def __init__(self, nome, idade, profissao):
    self.nome = nome
    self.idade = idade
    self.profissao = profissao

matheus = Pessoa("Matheus", 29, "Programador")

print(matheus)

print(type(matheus))

print(matheus.nome)
print(matheus.idade)
print(matheus.profissao)

if matheus.nome == "Matheus":
  print("O nome é Matheus")

nome = matheus.nome

print(nome)