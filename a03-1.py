"""
EXERCÍCIOS DE IF - IF/ELSE - IF/ELIF/ELSE
Escreva um programa que peça ao usuário
para digitar uma letra.
Diga ao usuário se essa letra
é uma vogal ou uma consoante
"""

letra = input("Digite uma letra ")
print(letra)
if letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u":
  print("a letra é um vogal")
else:
  print("a letra é uma consoante")

if True:
  print("Fim do programa.")
