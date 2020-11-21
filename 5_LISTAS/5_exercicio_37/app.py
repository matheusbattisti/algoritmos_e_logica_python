lista = [0, 0, 0, 0, 0]

print(lista)

i = 0

while i < 5:
  numero = int(input("Digite um número %d: " % i))
  lista[i] = numero
  i = i + 1

print(lista)