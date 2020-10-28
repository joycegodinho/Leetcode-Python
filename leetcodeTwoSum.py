# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 18:10:47 2020

@author: joyce

 *Given an array of integers nums and an integer target, return indices 
 *of the two numbers such that they add up to target.

"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) > 2:
            
            for i in range(len(nums)):
                
                for j in range(i+1, len(nums)):
                    solution = nums[i] + nums[j]
                    
                    if solution == target:
                        return [i,j]

        elif len(nums) == 2:
            return [0,1]
        
        else:
            return [0]
                
                
def main():
    
    nums = [2,7,11,15] 
    target = 9
    print("Teste 1")
    u = Solution() 
    print(u.twoSum(nums, target)) # [0, 1]
    
    nums2 = [3,2,4]
    target2 = 6
    print("Teste 2")
    u = Solution() 
    print(u.twoSum(nums2, target2)) # [1,2]
    
    nums3 = [3,3]
    target3 = 6
    print("Teste 3")
    u = Solution() 
    print(u.twoSum(nums3, target3)) # [0,1]
    
    nums4 = [3,2,3]
    target4 = 6
    print("Teste 4")
    u = Solution() 
    print(u.twoSum(nums4, target4)) # [0,2]
    
    nums5 = [3]
    target5 = 3
    print("Teste 5")
    u = Solution() 
    print(u.twoSum(nums5, target5)) # [0]
    
    nums6 = [2,5,5,11]
    target6 = 10
    print("Teste 6")
    u = Solution() 
    print(u.twoSum(nums6, target6)) # [1,2]
    

    
main()