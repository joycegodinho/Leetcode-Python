# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 18:07:32 2020

@author: joyce

Leetcode - reverse integer

Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment that could only store integers within the 32-bit 
signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your 
function returns 0 when the reversed integer overflows.
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y = []
        i = len(str(x)) - 1 
        
        if x > 0:
            x = str(x)
       

            while i >= 0:
                y.append(int(x[i]))
                i = i -1 
            y = ''.join(map(str, y))
            
            if int(y) >= 2**31 -1:
                return 0            
            return int(y)
        
        elif x < 0:           
            x = str(x)
          
            while i > 0:
                y.append(int(x[i]))
                i = i -1 
            y = ''.join(map(str, y))
            
            if -int(y) <= -2**31:
                return 0 
            return -int(y)
        
        else:
            return 0
            
def main():
    
    x = 123
    print("Teste 1")
    u = Solution() 
    print(u.reverse(x)) #321
    
    x2 = -123
    print("Teste 2")
    u = Solution() 
    print(u.reverse(x2)) #-321
    
    x3 = 0
    print("Teste 3")
    u = Solution() 
    print(u.reverse(x3)) #0
    
    x4 = 120
    print("Teste 4")
    u = Solution() 
    print(u.reverse(x4)) #0

    x5 = 1534236469
    print("Teste 5")
    u = Solution() 
    print(u.reverse(x5)) #0
    
    x6 = -1534236469
    print("Teste 6")
    u = Solution() 
    print(u.reverse(x6)) #0
    
main()
