a) Implémenter la fonction polynomiale ci-dessous :
def polynomial(n):
    poly = pow(n, 3)-( 1.5 * pow(n,2)) - (6*pow(n,1)) + pow(n,0)
    return poly


b) Implémenter la fonction factorielle (Approche récursive ou classique) :

def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact
   
or a recursive approach:

def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)