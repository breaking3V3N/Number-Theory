import modulo_class
import prime_factorization
import sympy as sym

def fermats_little_theorem(a: int, n: int):
    n_res = modulo_class.modulo_n(n)
    val = n_res.power(a,n-1)
    print(val)
    if val != 1:
        return "Composite"
    elif val == 1:
        if prime_factorization.is_prime(n) == False:
            return "Fermat-PseudoPrime; unknown if Carmichael"
        else:
            return "inconclusive"
def carmichael_test(n:int):
    n_res = modulo_class.modulo_n(n)
    for a in range(1,n):
        if fermats_little_theorem(a,n) != "Fermat-PseudoPrime; unknown if Carmichael":
            return "Not Carmichael"
        #add in specifics^
        else:
            return "carmichael"

def euler_pseudoprimes(a:int,n:int):
    n_res = modulo_class.modulo_n(n)
    val = n_res.power(a, (n - 1)/2)
    print(n_res.residue_classes)
    if val != n_res.residue_classes[1] and val != n_res.residue_classes[-1]:
        return "n is composite"
    elif val == n_res.residue_classes[1] or val == n_res.residue_classes[-1]:
        return "Euler psuedoprime"

def solve_k(n:int):
    a = n-1
    b = 1
    while a % 2 == 0:
        b*=2
    return b,a/b

def rabin_miller(a:int,n:int):
    c,k = solve_k(n)

'''
def Fermat_test_for_primality(n:int,num_it):
    n_res = modulo_class.modulo_n(n)
    for a in range
randomize^
'''
print(fermats_little_theorem(2,341))
print(carmichael_test(561))
print(euler_pseudoprimes(2,341))