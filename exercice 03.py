def FibRecursion(n):
if n <= 1:
return n
else:
return(FibRecursion(n-1) + FibRecursion(n-2))
nterms = int(input("Entrer le terme ")) 

if nterms <= 0: # tester si le nombre est valide
print("Entrer un integer positive")
else:
print("qequence de Fibonacci:")
for i in range(nterms):
print(FibRecursion(i))