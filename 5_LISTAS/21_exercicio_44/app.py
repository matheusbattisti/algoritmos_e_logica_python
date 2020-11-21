numeros = [100, 200, 400, 500, 700]

qual_numero_quer_encontrar = int(input("Que número deseja buscar? "))

encontrado = False

for n in numeros:
  if n == qual_numero_quer_encontrar:
    print("O número %d foi encontrado!" % n)
    encontrado = True


if encontrado == False:
  print("Não encontramos o número %d" % qual_numero_quer_encontrar)