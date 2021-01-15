# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 16:31:26 2020

@author: joyce
"""
##### Leetcode 21 - car pooling

class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        
        lista = []
        
        for people, start, end in trips:
            lista.append((start, people))
            lista.append((end, -people))
        lista.sort()
        
        for _, people in lista:
            capacity = capacity - people
            
            if capacity < 0:
                return False
        
        return True
            