# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 19:26:47 2020

@author: joyce
"""
#####Leetcode 19 - Sequencial Digits

class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        numeros = '123456789'
        resposta = []
        
        for i in range(len(numeros)):
            
            for j in range(i+1, len(numeros)):
                sequencial = int(numeros[i:j+1])
                
                if sequencial >= low and sequencial <= high:
                    resposta.append(sequencial)
       
        resposta.sort()
        
        return resposta
    
def main():
    
    low = 100 
    high = 300
    print("Teste 1")
    s = Solution() 
    print(s.sequentialDigits(low, high)) # [123,234]
    
    low2 = 1000
    high2 = 13000
    print("Teste 2")
    r = Solution() 
    print(r.sequentialDigits(low2, high2)) # [1234,2345,3456,4567,5678,6789,12345]
      
#main()