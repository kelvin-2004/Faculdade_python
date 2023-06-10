"""
Escreva um programa que pergunte ao usuário
em que turno ele(a) estuda
matutino = "m";
vespertino = "v";
noturno = "n";
escreva "bom dia", "boa tarde" ou "boa noite"
de acordo com a resposta
"""

turno = input("Em qual turno você estuda? ")
if turno == "matutino":
  print("Bom dia!")
elif turno == "vespertino":
  print("Boa tarde!")
elif turno == "noturno":
  print("Boa Noite!")
else:
  print("ERRO: tente matutino, vespertino ou noturno")
