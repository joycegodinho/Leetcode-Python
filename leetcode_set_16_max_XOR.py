# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 22:18:56 2020

@author: joyce
"""
##### Leetcode 16 - Maximum XOR of Two Numbers in an Array

class Solution:
    def findMaximumXOR(self, nums):
        resposta=0
        mascara = 0
        for i in range(31, -1, -1):
            mascara |= 1<<i
            procurado = set([num & mascara for num in nums])
                
            inicio = resposta | 1<<i
            for p in procurado:
                if inicio^p in procurado:
                    resposta = inicio
                    break
         
        return resposta