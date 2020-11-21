def calc_media(lista):
  media = 0
  soma = 0

  for n in lista:
    soma += n

  media = soma / len(lista)

  return media

notas = [9,8,7]

media_provas = calc_media(notas)

print(media_provas)

numeros = [3,4,4534,312,43,4,23,3,5,65,12]

media_numeros = calc_media(numeros)

print(media_numeros)