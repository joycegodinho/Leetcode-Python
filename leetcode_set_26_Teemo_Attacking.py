# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 19:20:03 2020

@author: joyce
"""

##### leetcode 26 - Teemo Attacking 

class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        
        total = 0
        
        if len(timeSeries) == 0:
            return 0
        
        for i in range(len(timeSeries) - 1):
            total = total + min(timeSeries[i+1] - timeSeries[i], duration)
            
        return total + duration
        