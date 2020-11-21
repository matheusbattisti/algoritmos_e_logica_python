numero = int(input("Digite um número: "))

divisoes = 0

contador = numero

while contador > 0:

  if numero % contador == 0:
    divisoes = divisoes + 1

  contador = contador - 1 

if divisoes == 2:
  print("O número %d é primo!" % numero)
else:
  print("O número %d NÃO é primo" % numero)