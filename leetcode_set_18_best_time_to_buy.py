# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 18:06:26 2020

@author: joyce
"""
####Leetcode 18 -- Best Time to Buy and Sell Stock

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        gap = 0
        
        
        for j in range(0, len(prices)-1):
                
            gap = max(gap, max(prices[j+1:]) - prices[j])

                    
        return gap
    

        
def main():
    
    prices = [7,1,5,3,6,4]
    print("Teste 1")
    s = Solution() 
    print(s.maxProfit(prices)) # 5
    
    prices2 = [7,6,4,3,1]
    print("Teste 2")
    r = Solution() 
    print(r.maxProfit(prices2)) # 0
    
    prices3 = []
    print("Teste 3")
    t = Solution() 
    print(t.maxProfit(prices3)) # 0
    
    prices4 = [1]
    print("Teste 4")
    u = Solution() 
    print(u.maxProfit(prices4)) # 0
    
    prices5 = [2,1]
    print("Teste 5")
    v = Solution() 
    print(v.maxProfit(prices5)) # 0
    

    
main()