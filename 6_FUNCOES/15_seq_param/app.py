def soma_todos(*nums):
  soma = 0
  for num in nums:
    soma += num

  return soma

s = soma_todos(5,4,3,2,66,5,34)

print(s)

s2 = soma_todos(1,2,3)

print(s2)