print("com base na lista, Faca um codigo usando lacos que identifique e remova todos os numeros desta lista que sao divisiveis por 3")
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 19, 11, 12]
 
for a in range(len(lista)):
  if lista[a] % 3 == 0:
    lista.pop(a)
  print(lista)