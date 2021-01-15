# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 17:47:46 2020

@author: joyce
"""
####Leetcode 10 - Bulls and Cows

from collections import Counter

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
    #A: acertou o dígito e a posição
    #B: acertou o dígito mas errou a posição 
        
        count_1 = 0
        count_2 = 0
        a = Counter(secret)
        b = Counter(guess)
        
        for i in range(len(secret)):
            
            if secret[i] == guess[i]:
                
                count_1 = count_1 + 1
            
        for i in set(secret):
            
            count_2 = count_2 + min(a[i], b[i])
                    
        return str(count_1) + str('A') + str(count_2 - count_1) + str('B')              
            
def main():
    
    secret = "1807"
    guess = "7810"
    print("Teste 1")
    s = Solution() 
    print(s.getHint(secret, guess)) #  "1A3B"
    
    secret2 = "1123"
    guess2 = "0111"
    print("Teste 2")
    r = Solution() 
    print(r.getHint(secret2, guess2)) #  "1A1B"
    
    secret3 = "11"
    guess3 = "10"
    print("Teste 3")
    t = Solution() 
    print(t.getHint(secret3, guess3)) #  "1A0B"
          
    secret4 = "1122"
    guess4 = "2211"
    print("Teste 4")
    t = Solution() 
    print(t.getHint(secret4, guess4)) #  "1A4B"
    
    
#main()