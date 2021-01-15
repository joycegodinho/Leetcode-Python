# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 16:05:30 2020

@author: joyce
"""

#### Leetcode 15 - Lenght of last word - One Line Version

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        #s=s.rstrip().split(' ')[-1]
                
        return len(s.rstrip().split(' ')[-1])
        
def main():
    
    s = "Hello World"
    print("Teste 1")
    r = Solution() 
    print(r.lengthOfLastWord(s)) # 5
    
    s = "a "
    print("Teste 2")
    t = Solution() 
    print(t.lengthOfLastWord(s)) # 1
    
    s = " "
    print("Teste 3")
    q = Solution() 
    print(q.lengthOfLastWord(s)) # 0
    

main()