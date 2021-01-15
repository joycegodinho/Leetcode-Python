# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 14:28:47 2020

@author: joyce
"""
#####Leetcode 09 - Compare Version

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        
        version1 = version1.split('.')
        version2 = version2.split('.')
        length = max(len(version1), len(version2))
        

        if len(version1) > len(version2):
            for k in range(len(version1) - len(version2)):
                version2.append('0')
        else:
            for l in range(len(version2) - len(version1)):
                version1.append('0')
                         
    
        for i in range(length):
            if int(version1[i]) > int(version2[i]):
                return 1
            elif int(version1[i]) < int(version2[i]):
                    return -1               
        return 0
                    
                    

            
def main():
    
    version1 = "0.1"
    version2 = "1.1"
    print("Teste 1")
    s = Solution() 
    print(s.compareVersion(version1, version2)) # -1
    
    
    version3 = "7.5.2.4"
    version4 = "7.5.3"
    print("Teste 2")
    r = Solution() 
    print(r.compareVersion(version3, version4)) # -1
    
    
    version5 = "1.0.1"
    version6 = "1"
    print("Teste 3")
    t = Solution() 
    print(t.compareVersion(version5, version6)) # 1
    
    
    version7 = "1.0"
    version8 = "1.0.0"
    print("Teste 4")
    u = Solution() 
    print(u.compareVersion(version7, version8)) # 0
    
    
    version9 = "1.01"
    version10 = "1.001"
    print("Teste 5")
    v = Solution() 
    print(v.compareVersion(version9, version10)) # 0
    
main()