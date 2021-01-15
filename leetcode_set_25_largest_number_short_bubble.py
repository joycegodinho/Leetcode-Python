# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 16:25:11 2020

@author: joyce
"""

##### Leetcode 25 - Largest Number - short bubble

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        
        
        string=[]
        
        for num in nums:
            string.append(str(num))
            
        #string.sort(reverse=True)
        
                
        fim = len(nums) - 1
        trocou = True
        
        while fim > 0 and trocou:
            
            trocou = False
            
            for i in range(fim):
                if string[i] + string[i+1] < string[i+1] + string[i]:
                    string[i], string[i+1] = string[i+1], string[i]
                    
                    trocou = True
            
            fim = fim - 1
        
        string = "".join(string)
        
        if string[0] == '0':
            return string[0]
        
        else:
            return string
        
           
def main():
    
    nums = [10,2]
    print("Teste 1")
    u = Solution() 
    print(u.largestNumber(nums)) # e
    
    nums2 = [3,30,34,5,9]
    print("Teste 2")
    u = Solution() 
    print(u.largestNumber(nums2)) # e
    
    nums3 = [0,9,8,7,6,5,4,3,2,1]
    print("Teste 3")
    u = Solution() 
    print(u.largestNumber(nums3)) # e
    
    nums4 = [9]
    print("Teste 4")
    u = Solution() 
    print(u.largestNumber(nums4))   

    nums5 = [74,21,33,51,77,51,90,60,5,56]
    print("Teste 5")
    u = Solution() 
    print(u.largestNumber(nums5))
    
main()