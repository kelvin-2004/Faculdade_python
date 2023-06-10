"""
EXERCÍCIOS DE IF - IF/ELSE - IF/ELIF/ELSE
Escreva um programa que peça três números ao usuário
e mostre o maior deles
"""

num1= float(input("digite o primeiro número: "))
num2= float(input("digite o segundo número: "))
num3= float(input("digite o terceiro número: "))

if num1 > num2 and num1 > num3:
  print(num1, "é maior")
elif num2 > num1 and num2 > num3:
  print(num2, "é maior")
else:
  print(num3, "é maior")
