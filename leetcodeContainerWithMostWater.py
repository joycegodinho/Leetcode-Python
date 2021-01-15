class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        '''
        areaMax = 0
       
        for i in range(len(height)):
            for j in range( i+1, len(height)):
                area = min(height[i], height[j])*(j-i)
                areaMax = max(areaMax,area)
                
        return areaMax
        '''

        areaMax = 0
        i = 0
        j = len(height) - 1

        while(i < j):
            area = min(height[i], height[j])*(j-i)
            areaMax = max(areaMax,area)
            if (height[i] < height[j]):
                i = i + 1
            else:
                j = j - 1

        return areaMax


def main():

    height = [1,8,6,2,5,4,8,3,7]
    print("Teste 01")
    u = Solution()
    print(u.maxArea(height)) #49

    height2 = [1,1]
    print("Teste 02")
    u = Solution()
    print(u.maxArea(height2)) #1

    height3 = [4,3,2,1,4]
    print("Teste 03")
    u = Solution()
    print(u.maxArea(height3)) #16

    height4 = [1,2,1]
    print("Teste 04")
    u = Solution()
    print(u.maxArea(height4)) #2

main()
