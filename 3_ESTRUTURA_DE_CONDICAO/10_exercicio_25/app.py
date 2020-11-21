numero = int(input("Digite um número: "))

print(numero)

if numero > 10:

  if numero > 20:
    print("Número maior que 20")
    print(numero * 2)
  else:
    print("Número menor que 20")
    print(numero * 5)

else:
  print("O número precisa maior que 10!")