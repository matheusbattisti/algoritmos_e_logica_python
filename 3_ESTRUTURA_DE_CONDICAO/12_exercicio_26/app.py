categoria = int(input("Qual o número da categoria? "))

print(categoria)

if categoria == 1:
  print("Este produto é da categoria BOLSA")
elif categoria == 2:
  print("Este produto é da categoria TÊNIS")
elif categoria == 3:
  print("Este produto é da categoria MOCHILA")
else:
  print("Categoria não encontrada!")