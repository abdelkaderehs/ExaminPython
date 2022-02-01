def factorial(n):  
    fact = 1  
    for num in range(2, n + 1):  
        fact *= num  
    return fact 

# recursive method

def factorialRecursive(n):
    if n < 2:
        return 1
    else:
        return n * factorialRecursive(n-1)
