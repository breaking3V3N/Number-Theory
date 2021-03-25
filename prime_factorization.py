import sympy as sym
import math

def factorization(a: int):
    factors = []
    for x in range(2,math.floor(math.sqrt(a)+1)):
        if a % x == 0:
            factors.append(x)
            factors.append(a//x)
    factors.sort()
    return factors

def prime_factors(factors: list):
    prime_f = []
    for x in factors:
        if x == 2:
            prime_f.append(x)
        for j in range(2,math.sqrt(x)):
            if x % j == 0:
                prime_f.append(x)
    return prime_f

def is_prime(x):
    for j in range(2, math.floor(math.sqrt(x)+1)):
        if x % j == 0:
            return False
    return True
print(factorization(30))

print(is_prime(30))
print(is_prime(271))