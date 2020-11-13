class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        resp = []

        for i in range(len(nums)):
            if nums[i] == target:
                resp.append(i)
        if len(resp) == 0:
            return [-1,-1]
        if len(resp) == 1:
            return [resp[0], resp[0]]
        if len(resp) > 2:
            return [resp[0], resp[-1]]
        else:
            return resp

def main():
    
    nums = [5,7,7,8,8,10]
    target = 8
    print("Teste 1")
    s = Solution() #chamo a classe
    print(s.searchRange(nums, target)) # 2

    nums2 = [5,7,7,8,8,10]
    target2 = 6
    print("Teste 2")
    s = Solution() #chamo a classe
    print(s.searchRange(nums2, target2)) # 2

    nums3 = []
    target3 = 0
    print("Teste 3")
    s = Solution() #chamo a classe
    print(s.searchRange(nums3, target3)) # 2

    nums4 = [1]
    target4 = 1
    print("Teste 4")
    s = Solution() #chamo a classe
    print(s.searchRange(nums4, target4)) # 2

main()