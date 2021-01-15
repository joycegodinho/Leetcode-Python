# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 11:29:43 2020

@author: joyce
"""
#### leetcode 24 - Find the Difference

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        t = sorted(t)
        t = list(t)
        
        s = sorted(s)
        s = list(s)

        for i in range(len(s)):
            
            if s[i] != t[i]:
                return t[i]
         
        return t[-1]
    
def main():
    
    s = "abcd"
    t = "abcde"
    print("Teste 1")
    u = Solution() 
    print(u.findTheDifference(s, t)) # e
    
    s2 = "abcda"
    t2 = "adbace"
    print("Teste 2")
    u = Solution() 
    print(u.findTheDifference(s2, t2)) # e
    
    s3 = "a"
    t3 = "aa"
    print("Teste 3")
    u = Solution() 
    print(u.findTheDifference(s3, t3)) # a
    
    s4 = "ae"
    t4 = "aea"
    print("Teste 4")
    u = Solution() 
    print(u.findTheDifference(s4, t4)) # a
    
#main()