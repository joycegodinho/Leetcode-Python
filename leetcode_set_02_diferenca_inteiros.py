# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 13:57:57 2020

@author: joyce


Dada um vetor de inteiros, descubra se existem dois índices distintos 
i e j no vetor de modo que a diferença absoluta entre nums [i] e nums [j] 
seja no máximo t e a diferença absoluta entre i e j seja no máximo k
"""


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        
        if t < 0 or not nums or k <=0:
            return False
        
        intervalos = {} #dicionario
        largura = t + 1 #todos colocados no mesmo intervalo terão diferenças não maiores que t
        
        for count, valor in enumerate(nums):
            elemento = valor//largura
            if elemento in intervalos:
                return True # se um segundo elemento vai para o mesmo intervalo retorna True, pois no mesmo intervalo todos terão diferenças não maiores que t
            else: #checar dois intervalos adjacentes
                intervalos[elemento] = valor
                if elemento - 1 in intervalos and valor - intervalos[elemento-1] <= t:
                    return True
                if elemento + 1 in intervalos and intervalos[elemento+1] - valor <= t:
                    return True
                if count >= k:
                    del intervalos[nums[count-k]//largura]
        else:
            return False


        
def main():
    
    testlist = [1,2,3,1]  
    '''
    
    for i in range(0, 21):
        n = random.randint(1, 100)
        testlist.append(n)
    '''
    
    print("Teste 1")
   
    
    s = Solution() #chamo a classe

    print(s.containsNearbyAlmostDuplicate(testlist, 3, 0)) #True
    


    testlist2 = [1,0,1,1]  
    '''
    
    for i in range(0, 21):
        n = random.randint(1, 100)
        testlist.append(n)
    '''
    
    print("Testes 2")
   
    
    p = Solution() #chamo a classe

    print(p.containsNearbyAlmostDuplicate(testlist2, 1, 2)) #True
    

    testlist3 = [1,5,9,1,5,9] 
    '''
    
    for i in range(0, 21):
        n = random.randint(1, 100)
        testlist.append(n)
    '''
    
    print("Teste 3")
   
    
    r = Solution() #chamo a classe

    print(r.containsNearbyAlmostDuplicate(testlist3, 2, 3)) #False
    
main()
