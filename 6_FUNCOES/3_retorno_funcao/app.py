def saudacao(nome):
  return "Olá %s" % nome

sds = saudacao("Matheus")

print(sds + ". Tudo bem?")

def soma(a, b):
  return a + b

s = soma(5, 7)
d = soma(2, 3)

print(s)

print(s + 5)

print(s + d)

def profissao(nome):

  p = ""

  if nome == "Matheus":
    p = "Programador"
  else:
    p = "Não identificado"
  
  return p

prof = profissao("João")

print(prof)

prof_m = profissao("Matheus")

print(prof_m)