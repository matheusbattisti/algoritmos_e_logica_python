def checa_tamanho_texto(texto):
  
  resposta = ""

  if len(texto) >= 20:
    resposta = "Texto muito longo!"
  else:
    resposta = "Texto curto!"

  return resposta

texto_um = "O Matheus é programador"

resp_texto_um = checa_tamanho_texto(texto_um)

print(resp_texto_um)
print(len(texto_um))

print(checa_tamanho_texto("Olá Mundo!"))

resp_texto_dois = checa_tamanho_texto("O rato roeu a roupa do rei de Roma")

print(resp_texto_dois)