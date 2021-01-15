# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 12:55:41 2020

@author: joyce
"""
#### leetcode 30 - First missing positive

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        if nums:
           for i in range(1, len(nums) +2):
               if i not in nums:
                   return i
            
        
        return 1
        
def main():
    
    nums = [1,2,0]
    print("Teste 1")
    u = Solution() 
    print(u.firstMissingPositive(nums)) # 3
    
    nums2 = [3,4,-1,1]
    print("Teste 2")
    u = Solution() 
    print(u.firstMissingPositive(nums2)) # 2
    
    nums3 = [7,8,9,11,12]
    print("Teste 3")
    u = Solution() 
    print(u.firstMissingPositive(nums3)) # 1
    

    
main()