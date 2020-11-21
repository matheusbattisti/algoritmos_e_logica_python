import random

aleatorio = random.randint(1, 10)

palpite = int(input("Advinhe o número: "))

if aleatorio == palpite:
  print("Parabéns você acertou o número é: %d" % aleatorio)
else:
  print("Você errou! O número era: %d" % aleatorio)