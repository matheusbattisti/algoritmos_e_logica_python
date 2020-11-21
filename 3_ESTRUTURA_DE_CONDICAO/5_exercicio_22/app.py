numero_um = int(input("Digite um número: "))
numero_dois = int(input("Digite outro número: "))

print(numero_um)
print(numero_dois)

if(numero_um > numero_dois):
  print("O número %d é maior que o número %d" % (numero_um, numero_dois))

if(numero_dois > numero_um):
  print("O número %d é maior que o número %d" % (numero_dois, numero_um))

if(numero_dois == numero_um):
  print("Os números são iguais!")