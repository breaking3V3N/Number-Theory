import sympy as sym
import typing
from typing import List
from sympy import functions, symbols


class Evens:

    def __init__(self,n: int):

        self.n_total = n
        self.even_list = self.gen_num()
        self.even_prime_list = self.gen_even_primes()

    def gen_num(self)->List[symbols]:
        evens = []
        for c in range(0,self.n_total):
            evens.append(2 * c)
        return evens


    def gen_even_factors(self,even_num: int)->List[symbols]:
        even_factors = []
        for num in range(1,self.n_total):
            if even_num / num in self.even_list:
                even_factors.append(num)
        return even_factors

    def gen_even_primes(self)->List[symbols]:
        even_primes = []
        for num in self.even_list:
            num_fac = self.gen_even_factors(num)
            not_in = 0
            for factor in num_fac:
                if factor not in self.even_list:
                    not_in += 1
            if not_in == len(num_fac):
                even_primes.append([num,self.gen_even_factors(num)])
        return even_primes

    def print_evens(self)->None:
        for e in self.even_list:
            print(str(e))

    def print_even_primes(self)->None:
        for e in self.even_prime_list:
            print(str(e))

'''
    def find_primes(self)->List[symbols]:
        for num in range(0,self.n_total):
            for even in self.even_list[0:num]:
                if even

'''

a = Evens(10)
a.print_evens()
a.print_even_primes()