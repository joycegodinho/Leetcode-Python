#### Leetcode remove element
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        init = 0
        final = len(nums) - 1
        
        while init <= final:
            
            if nums[init] != val:
                init = init + 1
            else:
                nums[init], nums[final] = nums[final], nums[init]
                final = final - 1
        
        return init, nums[:init]

def main():
    
    nums = [3,2,2,3]
    val = 3
    print("Teste 1")
    s = Solution() #chamo a classe
    print(s.removeElement(nums, val)) # 2
    
    
    nums2 = [0,1,2,2,3,0,4,2]
    val2 = 2
    print("Teste 2")
    r = Solution() #chamo a classe
    print(r.removeElement(nums2, val2)) # 5

    nums3 = []
    val3 = 2
    print("Teste 3")
    r = Solution() #chamo a classe
    print(r.removeElement(nums3, val3)) # 0
    
    
main()
