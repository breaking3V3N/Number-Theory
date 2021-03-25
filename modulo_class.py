import sympy as sym
import typing
from typing import List
from sympy import symbols,functions


class modulo_n:

    def __init__(self,int_n: int):
        self.n = int_n
        self.residue_classes = self.create_residue_class()
        self.residue_times_table = self.times_table()
        self.poten_gen = self.set_powers()
        self.generators = self.find_gen()

    def create_residue_class(self):
        res_class = []
        for x in range(0,self.n):
            res_class.append(x)
        return res_class

    def print_residue_class(self):
        print(self.residue_classes)

    def add_res_element(self,a, b):
        if a + b < self.n:
            return a + b
        else:
            return (a+b)%self.n

    def mult_res_element(self, a, b):
        if a*b < self.n:
            return a*b
        else:
            return (a *b) % self.n

    def add_table(self):
        table = {}
        for element in self.residue_classes:
            table[element] = []
        for num in table:
            num_table = []
            for res_iter in self.residue_classes:
                num_table.append(self.add_res_element(num, res_iter))
            table[num] += num_table
        return table

    def times_table(self):
        table = {}
        for element in self.residue_classes[1:]:
            table[element] = {}
        for num in table:
            num_info = {'factors': [], 'mult_inverse': int}
            num_table = []
            for res_iter in self.residue_classes[1:]:
                num_table.append(self.mult_res_element(num,res_iter))
                if self.mult_res_element(num,res_iter) == 1 and (num or res_iter) != 0:
                    num_info['mult_inverse'] = res_iter
                num_info['factors'] = num_table
            table[num] = num_info
        return table

    def inverse_table(self):
        emp = []
        for element in self.residue_times_table:
            emp.append([element,self.residue_times_table[element]['mult_inverse']])
        return emp[1:]
    def prime_power(self,element):
        a = element
        sol = []
        k = len(self.residue_classes)-1
        while k != 0:
            a = self.mult_res_element(a,element)
            sol.append(a)
            k -=1
        sol.sort()
        return [a,sol]
    def power(self,element,k):
        a = element
        while k != 1:
            a = self.mult_res_element(a,element)
            k -=1
        return a

    def set_powers(self):
        powers = []
        for element in self.residue_classes:
            powers.append(self.prime_power(element))
        return powers

    def find_gen(self):
        gens = []
        for gen in self.poten_gen:
            if gen[1] == self.residue_classes[1:]:
                gens.append(gen)
        return gens



    #def prime_square_check(self,):

    #def chinese_remainder_theorem(self,equations:List[functions]
    #def inverse_computer(self):






a = modulo_n(5)
#b = modulo_n(11)
#c = modulo_n(19)
a.print_residue_class()
print(a.prime_power(2))
print(a.poten_gen)
print(a.generators)
'''
#print(a.mult_res_element(int(a.residue_classes[3]),int(a.residue_classes[2])))
#rint(a.times_table())
#print(a.inverse_table())
#print(154 % 19)
#print(a.mult_res_element(11,7))
print(a.times_table())
l = [1,2,5,10,11,22,55,110,121,242,605,1210]
for x in range(0,41):
    print("&7^{" + str(x+1) + "} \mod{41} \equiv " + str(a.mult_res_element(7,7**x)) + str(r',\\'))
for y in range(0,len(l)):
    print("2^{" + str(l[y]+1) + "} \mod{1331}),")

'''

