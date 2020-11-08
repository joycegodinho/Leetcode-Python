# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 11:15:15 2020

@author: joyce
"""
#Given an array of 4 digits, find the latest 24-hour time that can be made using each digit exactly once.

from itertools import permutations

class Solution(object):
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        
        P = permutations(A)
        maximo = -1
        
        for i, j, k, w in P:
            
            horas = i*10 + j
            minutos = k*10 + w
            
            if horas < 24 and minutos < 60:
                
                tempo = horas*60 + minutos
                maximo = max(maximo, tempo)
         
        if maximo == -1:
            
            return ""
        else:
            
            maxima_hora = maximo//60
            maximo_minuto = maximo%60
            return "{:02d}:{:02d}".format(maxima_hora, maximo_minuto)
                        
import random

def main():
    
    print("Testes")
    testlist = []
     
    for i in range(0, 4):
        n = random.randint(1,9)
        testlist.append(n)
    
    print(testlist)
 
    s = Solution() #chamo a classe

    print(s.largestTimeFromDigits(testlist)) #chamo a função
    
main()
