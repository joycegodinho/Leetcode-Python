# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 14:45:23 2020

@author: joyce
"""
#### Leecode 13 - Insert Interval

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        
        resp = []
        
        
        for i, (x,y) in enumerate(intervals):
            
            if y < newInterval[0]:
                resp.append([x,y])
            
            elif x > newInterval[1]:
                resp.append(newInterval)
                return resp + intervals[i:]
            
            else:
                newInterval[0] = min(newInterval[0], x)
                newInterval[1] = max(newInterval[1], y)
                
        resp.append(newInterval)
        
                
        return resp
                
        
def main():
    
    intervals = [[1,3],[6,9]]
    newInterval = [2,5]
    
    print("Teste 1")
    s = Solution() 
    print(s.insert(intervals, newInterval)) # [[1,5],[6,9]]
   
   
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]
    
    print("Teste 2")
    r = Solution() 
    print(r.insert(intervals, newInterval)) # [[1,2],[3,10],[12,16]]
    
    
#main()