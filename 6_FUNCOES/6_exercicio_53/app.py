def retorna_lista_par(l):
  nova_lista = []

  for numero in l:
    if numero % 2 == 0:
      nova_lista.append(numero)

  return nova_lista

lista = [1,2,3,4,5,6,7,8]

lista_par = retorna_lista_par(lista)

print(lista_par)

lista2 = [1,3,23,43,54,65,5234,3,445,54,34213,76,8,45,23]

print(retorna_lista_par(lista2))