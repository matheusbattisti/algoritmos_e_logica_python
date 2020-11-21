class Banco():
  def __init__(self, nome, saldo):
    self.nome = nome
    self.saldo = saldo
  
  def deposito(self, valor):
    self.saldo += valor

  def saque(self, valor):
    self.saldo -= valor

  def transferencia(self, outra_conta, valor):
    self.saldo -= valor
    outra_conta.saldo += valor

conta_matheus = Banco("Matheus", 1000)

print(conta_matheus.nome)

conta_matheus.deposito(1000)

print(conta_matheus.saldo)

conta_matheus.saque(1500)

print(conta_matheus.saldo)

conta_maria = Banco("Maria", 600)

conta_matheus.transferencia(conta_maria, 200)

print(conta_maria.saldo)

print(conta_matheus.saldo)