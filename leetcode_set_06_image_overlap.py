# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 16:51:50 2020

@author: joyce
"""

## Leetcode 6 - maior overlap possivel de duas imagens


class Solution(object):
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        
        overlap = 0
        comp = len(A)
        
        for c in range(comp):
            for l in range(comp):
                slide_A = 0
                slide_B = 0
                
                for i in range(comp - c):
                    for j in range(comp-l):
                        slide_A = slide_A + A[i+c][j+l]*B[i][j]
                        slide_B = slide_B + B[i+c][j+l]*A[i][j]
                
                overlap = max(overlap, slide_A, slide_B)
       
        return overlap
    
def main():
    
    A = [[1,1,0],
         [0,1,0],
         [0,1,0]]
    
    B = [[0,0,0],
         [0,1,1],
         [0,0,1]]

    print("Teste 1")
   
    
    s = Solution() #chamo a classe

    print(s.largestOverlap(A, B)) # 3
    
main()