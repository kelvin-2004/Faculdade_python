"""
Escreva um programa que pergunte ao usuário algo que tenha como respostas válidas apenas s(sim) e n(não). Caso o usuário digite outra resposta o programa deve perguntar novamente até obter uma resposta válida (s ou n minúsculas)
"""
resposta = ""

while resposta != "s" and resposta != "n":
  resposta = input("você gosta de suco de abaixaqui? (s/n) ")
  if resposta == "s":
    print("eu também")
  elif resposta == "n":
    print("eu gosto")
