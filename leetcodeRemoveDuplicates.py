### leetcode - remove duplicates

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        
        if len(nums) == 0:
            return 0
        
        
        for j in range(1,len(nums)):
            if nums[j] != nums[i]:
                i = i + 1
                nums[i] = nums[j]
        
        return i + 1

def main():
    
    nums = [1,1,2]
    print("Teste 1")
    s = Solution() #chamo a classe
    print(s.removeDuplicates(nums)) # 2
    
    
    nums2 = [0,0,1,1,1,2,2,3,3,4]
    print("Teste 2")
    r = Solution() #chamo a classe
    print(r.removeDuplicates(nums2)) # 5
    
    

    
main()