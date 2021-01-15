# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 11:11:46 2020

@author: joyce
"""

###### Leetcode 28 - Subarray Product Less Than K - slide window



class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        produto = 1
        inicio = 0
        resp = 0
        
        if k <= 1:
            return 0
        
        for fim in range(len(nums)):
            produto = produto*nums[fim]
            
            while fim >= inicio and produto >= k:
                produto = produto/nums[inicio]
                inicio = inicio + 1
           
            else:
                resp = resp + fim - inicio + 1
                fim = fim + 1
               
        return resp
                
                
            