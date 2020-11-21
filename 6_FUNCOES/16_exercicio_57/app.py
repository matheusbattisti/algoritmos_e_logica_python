def multiplica_numeros(*numeros):
  resultado = 1
  for num in numeros:
    resultado *= num

  return resultado

print(multiplica_numeros(5,4,2,1))

res = multiplica_numeros(4,45,234,324,56,56,54)

print(res)

res2 = multiplica_numeros(54,45,332,0)

print(res2)