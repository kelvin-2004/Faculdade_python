frutas = ["maçã", "banana", "melancia"]
frutas[2] = "cereja" #substitui na lista 
frutas.append("pera") #adiciona um item no final
frutas.insert(1,"laranja") #adiciona um item onde quiser
tropical = ["manga", "abacaxi", "mamão"]
frutas.extend(tropical) #junta as duas listas
frutas.remove("banana") #remove algum item (palavra)
frutas.pop() #remove o último item da lista
frutas.pop(3) #remove um item da lista (índice)
del frutas[1] #faz a mesma coisa que o pop
#frutas.clear() #deleta toda a lista
frutas.sort() #coloca em ordem alfabética
frutas.sort(reverse = True) #coloca em ordem alfabética invertida
print(frutas)
if "melancia" in frutas:
  print("Tem melancia na lista!") 
else:
  print("Não tem melancia")
