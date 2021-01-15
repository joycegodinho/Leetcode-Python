##Search insert position os a target

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
      
        nums.append(target)
        nums =  sorted(set(nums))
        primeiro = 0
        ultimo = len(nums) - 1 #len da o número de elementos na lista, como a contagem começa em 0, a posição do ultimo da lista é len - 1
        encontrado = False
    
        while primeiro <= ultimo and not encontrado:
            meio = (primeiro + ultimo)//2
            
            if nums[meio] == target:
                encontrado = True
                index = meio
                
            else:
                if target < nums[meio]:
                    ultimo = meio - 1
                else:
                    primeiro = meio + 1
        
        return index

def main():
    
    nums = [1,3,5,6]
    target = 5
    print("Teste 1")
    s = Solution() #chamo a classe
    print(s.searchInsert(nums, target)) # 2

    nums2 = [1,3,5,6]
    target2 = 2
    print("Teste 2")
    s = Solution() #chamo a classe
    print(s.searchInsert(nums2, target2)) # 2

    nums3 = [1,3,5,6]
    target3 = 7
    print("Teste 3")
    s = Solution() #chamo a classe
    print(s.searchInsert(nums3, target3)) # 2

    nums4 = [1,3,5,6]
    target4 = 0
    print("Teste 4")
    s = Solution() #chamo a classe
    print(s.searchInsert(nums4, target4)) # 2

    nums5 = [1,3]
    target5 = 1
    print("Teste 5")
    s = Solution() #chamo a classe
    print(s.searchInsert(nums5, target5)) # 2

main()