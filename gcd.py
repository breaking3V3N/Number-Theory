import sympy as sym
from sympy import symbols,functions

import typing
from typing import List

A = 0
Q = 1
B = 2
R = 3
x,y = symbols('x y')

def Euclid_express_rewrite(exp: List[symbols]) -> str:
    print(str(exp[R]) + " = " + str(exp[A]) + " - " +  "(" + str(exp[Q]) + ")" + str(exp[B]))

def list_check(l,e):
    for element in l:
        if element not in e:
            return False
    return True

def Euclid_express_rewrite_l(exp: List[symbols]) -> str:
    return [exp[R],exp[A],exp[Q],exp[B]]


def list_check(l,e):
    for element in l:
        if element not in e:
            return [False,element]
    return [True]

class linear_diophantine:

    def __init__(self, a,b,c: int = 0):
        self.num_a = min(a,b)
        self.num_b = max(a,b)
        self.num_c = c
        self.euclid_divisor_list = self.Euclid_division_algorithm()
        self.val_dict = self.express_val_d()

    def Euclid_division_algorithm(self):
        b = self.num_b
        a = self.num_a
        euclid_lines = []
        while b:
            a, b = b, a % b
            if b != 0:
                q = a // b
                r = a - (a // b) * b
                # think of this as:
                """
                [bignumber,q,b]
                we need to incorporate r.
                """
                euclid_lines.append([a, q, b, r])
        return euclid_lines



    """
    make into dict, key being val, value veuig expression(RHS)
    """
    def express_val_str(self):
        for x in range(-1,-len(self.euclid_divisor_list)-1,-1):
            Euclid_express_rewrite(self.euclid_divisor_list[x])

    """
    NOTE -
    """
    def express_val_d(self):
        new_d = {}
        for x in range(-1, -len(self.euclid_divisor_list) - 1, -1):
            new_d[Euclid_express_rewrite_l(self.euclid_divisor_list[x])[0]] = Euclid_express_rewrite_l(self.euclid_divisor_list[x])[1:]
        return new_d

    def express_gcd_base(self):

        eq_root = self.euclid_divisor_list[-2]

        x_scalars = [1]
        x_factors = [[eq_root[A]]]
        y_scalars = [eq_root[Q]]
        y_factors = [eq_root[B]]

        x_express = [x_scalars, x_factors]
        y_express = (y_scalars, y_factors)

        tot_express = [x_express, y_express]

        tot_express = [x_express, y_express]
        l_t = list_check(x_factors, [self.num_a, self.num_b])
        while l_t != True:
            for item in x_factors:
                for x in item:
                    if x in self.val_dict:
                        tot_express[0][1].append(self.val_dict[x])

            break
        return tot_express


def check_item(lst:list, elements:list):
    for item in lst:
        if item not in list:
            return False
    return True

r = linear_diophantine(1260,978,24)
print(r.express_gcd_base())
print(r.num_c)

print(r.express_val_d())


Euclid_express_rewrite([132,7,18, 6])

def eq_rewrite(funct: functions, var: symbols):
    return sym.solve(funct,var)
print(eq_rewrite(y-x**2,x))



def Euclid_express(exp: List[symbols])->str:
    return  str(exp[A]) + " = " + "(" + str(exp[Q]) + ")" +str(exp[B]) + " + " + str(exp[R])


def Euclid_division_algorithm(a:symbols, b:symbols):
    b = max(a,b)
    a = min(a,b)
    euclid_lines = []
    while b:
        a, b = b, a % b
        if b != 0:
            q = a//b
            r = a-(a//b)*b
            #think of this as:
            """
            [bignumber,q,b]
            we need to incorporate r.
            """
            euclid_lines.append([a,q,b,r])
    return euclid_lines

def Euclid_div_output(div_list: List[List[symbols]]):
    """
    Puts the elements for the euclid algorithm in the form:
    a = (q)b + r
    :param div_list:
    :return: list of type str,
    """
    form_lines = []
    for exp in div_list:
        form_lines.append(Euclid_express(exp))
    return form_lines

def print_Euclid(euclid_lines: List[str]):
    print('\n')
    print("Output format:   a = q(b) + r" + '\n')
    for element in euclid_lines:
        print(element)

def gcd(a,b):
    return Euclid_division_algorithm(a,b)[-1][-2]



"""
Need to fix params div_algo max
"""
d = Euclid_division_algorithm(1331,)
q = Euclid_div_output(d)
print_Euclid(q)
x,y = symbols('x y')
f = (978*x - 3*(1260*y - (1)*978*x)) - 7*(1260*y-(1)*978*x - 2*(978*x-3*(1260*y-978*x)))
g = sym.simplify(f)
print(g)
r.express_val_str()
print((1111000 + 111100 + 11110 + 1111 )/3)