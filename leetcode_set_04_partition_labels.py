# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 15:42:32 2020

@author: joyce
"""

'''
Uma string S de letras inglesas minúsculas é fornecida. Queremos particionar esta string em tantas partes quanto possível, de 
modo que cada letra apareça em no máximo uma parte e retornar uma lista de inteiros representando o tamanho dessas partes.

'''

class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """

 
        ultima = dict() #criar um dicionário que armazenará os maiores indices de cada letra
        unicas = set(S) #letras na ordem sem repetição
        i = len(S)-1
        res = []
        start = 0
        end = 0
        
        while unicas:
            if S[i] in unicas:
                ultima[S[i]] = i
                unicas.remove(S[i])
            i = i - 1
        
        #return ultima

        for indice, valor in enumerate(S):
            end = max(end, ultima[valor])
            if end == indice: 
                res.append(end - start + 1)
                start = indice + 1
            
        return res
       
        
def main():
    
    testlist = "ababcbacadefegdehijhklij" 

    print("Teste 1")
   
    
    s = Solution() #chamo a classe

    print(s.partitionLabels(testlist)) #[9,7,8]
    


   
    
main()
                
            