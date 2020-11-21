numero_um = int(input("Digite o primeiro número: "))
numero_dois = int(input("Digite o segundo número: "))

multiplicacao = numero_um * numero_dois

if multiplicacao <= 100:
  print("O número é baixo, o número é %d" % multiplicacao)
else:
  print("O número é alto, o número é %d" % multiplicacao)