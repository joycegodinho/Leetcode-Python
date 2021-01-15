# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 15:56:10 2020

@author: joyce
"""

##### Leetcode 07 - verificação se ambos os imputs tem o mesmo padrao de repetição


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        substring = str.split(' ')
        vetor_string = []
        vetor_pattern = []
        
        for i in range(len(substring)):
            if substring[i] == substring[0]:
                vetor_string.append(1)
            else:
                if substring [i] == substring[1]:
                    vetor_string.append(0)
                else:
                    vetor_string.append(2)

        for j in range(len(pattern)):
            if pattern[j] == pattern[0]:
                vetor_pattern.append(1)
            else:
                if pattern[j] == pattern[1]:
                    vetor_pattern.append(0)
                else:
                    vetor_pattern.append(2)
                    
        if vetor_pattern == vetor_string:
            return True, vetor_pattern, vetor_string
        else:
            return False, vetor_pattern, vetor_string        
        

def main():
    
    pattern = "abba"
    str = "fish whoops helloworld fish" 
    print("Teste 1")
    s = Solution() #chamo a classe
    print(s.wordPattern(pattern, str)) # False
    
    
    pattern2 = "abba"
    str2 = "dog cat cat dog" 
    print("Teste 2")
    r = Solution() #chamo a classe
    print(r.wordPattern(pattern2, str2)) # True
    
    
    pattern3 = "abba"
    str3 = "dog cat cat fish" 
    print("Teste 3")
    t = Solution() #chamo a classe
    print(t.wordPattern(pattern3, str3)) # False
    
    
    pattern4 = "abc"
    str4 = "a b c" 
    print("Teste 4")
    u = Solution() #chamo a classe
    print(u.wordPattern(pattern4, str4)) # True
    
main()