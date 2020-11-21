itens_carro = ["Porta", "Pneu", "Estepe", "Maçaneta", "Janela", "Chave", "Motor", "Marcha"]

item_um = input("O que deseja procurar primeiro?")
item_dois = input("O que deseja procurar depois?")

i = 0

while i < len(itens_carro):
  if itens_carro[i] == item_um:
    print("O primeiro objeto foi encontrado antes! %s" % item_um)
    break
  elif itens_carro[i] == item_dois:
    print("O segundo objeto foi encontrado antes! %s" % item_dois)
    break

  i = i + 1