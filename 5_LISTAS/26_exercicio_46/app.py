lista = [10, 1, 50, 35, -14]

menor_valor = lista[0]

for i in lista:
  if i < menor_valor:
    menor_valor = i

print("O menor valor é o %d" % menor_valor)