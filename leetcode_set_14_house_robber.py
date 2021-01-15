# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 15:20:41 2020

@author: joyce
"""

#### Leetcode 14 --- House Robber ---- Programação Dinâmica


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        
        if len(nums)==0:
            return 0
        
        if len(nums)==1:
            return int(nums[0])
        
        soma1 = nums[0]
        soma2= max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            
            temp = soma2
            soma2=max(soma2, soma1 + nums[i])
            soma1= temp
            
        return int(soma2)
        
def main():
    
    nums = [1,2,3,1]
    print("Teste 1")
    s = Solution() 
    print(s.rob(nums)) # 4
    
    nums2 = [2,7,9,3,1]
    print("Teste 2")
    r = Solution() 
    print(r.rob(nums2)) # 12
    
main()