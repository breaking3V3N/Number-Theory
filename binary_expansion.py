import sympy as sym

def binary_expansion(base_10:int):
    binary_expan = []
    a = base_10 // 2
    c = base_10 % 2
    binary_expan.append(c)
    while a != 0:
        base_10 = a
        a = base_10 // 2
        c = base_10 % 2
        binary_expan.append(c)
    return binary_expan[::-1]


print(binary_expansion(61))
#works just need to add computation reveal

'''
def decimal_expansion(base_2:int):
    s = str(base_2)
    sum = []
    for j in s:
        sum.append(j) * (2**(len(s)-1))


def binarry_expansion(rb10:float):
    k = sym.symbols('k')
    return sym.solve(2**(k+1)-1 - rb10,)

'''