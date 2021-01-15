# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 16:27:46 2020

@author: joyce
"""

###### Leetcode 23 - Gas Station


class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
              
        indice=0
        gas_ = 0
        inic_gas = 0
        
        for i in range(len(gas)):
            inic = gas[i] - cost[i]
            
            if gas_ + inic < 0:
                gas_ = 0
                indice = i + 1
                
            else:
                gas_ = gas_ + inic
                
            inic_gas = inic_gas + inic
        
        return indice if inic_gas >= 0 else - 1
                    

                    
def main():
    
    gas  = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    print("Teste 1")
    s = Solution() 
    print(s.canCompleteCircuit(gas, cost)) # [3]
    
    gas2  = [2,3,4]
    cost2 = [3,4,3]
    print("Teste 2")
    r = Solution() 
    print(r.canCompleteCircuit(gas2, cost2)) # [1,2]
    
    gas3  = [5,1,2,3,4]
    cost3 = [4,4,1,5,1]
    print("Teste 3")
    t = Solution() 
    print(t.canCompleteCircuit(gas3, cost3)) # [1,2]
      
#main()