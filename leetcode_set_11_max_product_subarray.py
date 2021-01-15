# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 14:41:34 2020

@author: joyce
"""

### Leetcode 11 - max product subarray


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        lista = nums[::-1] #[start,stop, step] - está invertendo a array

        for i in range(1,len(nums)):
            
            if nums[i - 1] != 0:
                nums[i] = nums[i]*nums[i - 1]
            
            if lista[i - 1] != 0:
                lista[i] = lista[i]*lista[i-1]   
        
        return max(lista + nums)
    

        
    
def main():
    
    nums = [2,3,-2,4]
    
    print("Teste 1")
    s = Solution() 
    print(s.maxProduct(nums)) # 6
    
    nums2 = [-2,0,-1]
    
    print("Teste 2")
    r = Solution() 
    print(r.maxProduct(nums2)) # 0
    
    nums3 = [-2]
    
    print("Teste 3")
    t = Solution() 
    print(t.maxProduct(nums3)) # -2
    
    nums4 = [-4,-3]
    
    print("Teste 4")
    u = Solution() 
    print(u.maxProduct(nums4)) # 12
    
    nums5 = [0,2]
    
    print("Teste 5")
    v = Solution() 
    print(v.maxProduct(nums5)) # 2
    
    nums6 = [-2,3,-4]
    
    print("Teste 6")
    x = Solution() 
    print(x.maxProduct(nums6)) # 24
    
    nums7 = [1,-2,-2,-1]
    
    print("Teste 7")
    z = Solution() 
    print(z.maxProduct(nums7)) # 4
    
#main()