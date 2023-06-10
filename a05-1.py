"""
Crie um programa que peça um número ao usuário e
retorne a soma de todos os números entre 1 e esse número
"""

número = int(input("digite um número inteiro: "))
soma = 0
for i in range(número+1):
  soma = soma + i
print("a soma de todos os números até",número,"é =",soma)
