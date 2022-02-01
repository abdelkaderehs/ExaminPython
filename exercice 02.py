c) Implémenter la suite de Fibonnaci

nterms = int(input("Entrez un nombre: "))
 
n1 = 0
n2 = 1
 
print("\n la suite fibonacci est :")
print(n1, ",", n2, end=", ")
 
for i in range(2, nterms):
  suivant = n1 + n2
  print(suivant, end=", ")
 
  n1 = n2
  n2 = suivant
  
  Cet exemple montrera la suite de Fibonacci du nombre 10.

Entrez un nombre: 10

la suite fibonacci est :
0 , 1, 1, 2, 3, 5, 8, 13, 21, 34,