# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 16:59:10 2020

@author: joyce
"""


#####Leetcode 12 - Combination Sum III


from itertools import combinations

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        
        comb = combinations([1,2,3,4,5,6,7,8,9], k)
        soma = []
        
        for i in list(comb):
            if sum(i) == n:
                soma.append(i)
                
        if not soma:
            return []
        else:
            return soma
      
def main():
    
    k = 3 
    n = 7
    
    print("Teste 1")
    s = Solution() 
    print(s.combinationSum3(k, n)) # [[1,2,4]]
    
    k = 3 
    n = 9
    
    print("Teste 2")
    r = Solution() 
    print(r.combinationSum3(k, n)) # [[1,2,6], [1,3,5], [2,3,4]]
    
    k = 2 
    n = 18
    
    print("Teste 3")
    t = Solution() 
    print(t.combinationSum3(k, n)) # []
    
#main()