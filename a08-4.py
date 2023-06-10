#exemplo testa se o número é par

n = int(input("Digite o número: "))

def testa_par(a):
  return a%2 == 0

if testa_par(n):
  print(n, "é par")
else:
  print(n, "é ímpar")
