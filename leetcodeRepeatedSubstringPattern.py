# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 11:07:19 2020

@author: joyce
"""


### Descobrir se uma string é feita da repetição de uma substring

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #s = str(s)
        
        for i in range(1,len(s)//2 + 1):
            
            substring = s[:i]
            intervalo = len(s)//i
            
            if substring* intervalo == s:
                return True

        return False
            

def main():
    
    testlist = "abab"  

    print("Teste 1")
   
    
    s = Solution() #chamo a classe

    print(s.repeatedSubstringPattern(testlist)) #True
    


    testlist2 = "aba"  
   
    print("Testes 2")
   
    
    p = Solution() #chamo a classe

    print(p.repeatedSubstringPattern(testlist2)) #False
    

    testlist3 = "abcabcabcabc" 
    
    print("Teste 3")
   
    
    r = Solution() #chamo a classe

    print(r.repeatedSubstringPattern(testlist3)) #True
    
main()
                
            