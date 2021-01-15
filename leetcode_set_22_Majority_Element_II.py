# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 16:45:06 2020

@author: joyce
"""
##### Leetcode 22 --- Majority Element II
from collections import Counter 

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        ##### Solução 01
        
        '''
        dic = {}
        resp = []
        
        for n in nums:
            if n in dic:
                dic[n] = dic[n]+1
            else:
                dic[n] = 1
        
        for n in dic:
            if dic[n] > sum(dic.values())/3:
                resp.append(n)
        
        return resp
    
        '''
        
        ##### Solução 02
        
        resp = []
        counts = Counter(nums)
        
        for num, times in counts.items():
            if times > len(nums)/3:
                
                resp.append(num)
                
        return resp

def main():
    
    nums = [3,2,3]
    print("Teste 1")
    s = Solution() 
    print(s.majorityElement(nums)) # [3]
    
    nums2 = [1,1,1,3,3,2,2,2]
    print("Teste 2")
    r = Solution() 
    print(r.majorityElement(nums2)) # [1,2]
      
main()