# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 20:17:40 2020

@author: joyce
"""

#### Letcode 17 - Robot Bounded In Circle


class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        
        direction_x = 0
        direction_y = 1
        x = 0
        y = 0
        
        for i in 4*instructions:
            if i == "G":
                
                x = x + direction_x
                y = y + direction_y
                
            elif i == "L":
                
                direction_x, direction_y = -direction_y, direction_x
                
            else:

                direction_x, direction_y = direction_y, - direction_x
                
        return (x,y) == (0,0)
    
def main():
    
    instructions = "GGLLGG"
    print("Teste 1")
    s = Solution() 
    print(s.isRobotBounded(instructions)) # true
    
    instructions2 = "GG"
    print("Teste 2")
    r = Solution() 
    print(r.isRobotBounded(instructions2)) # false
    
    instructions3 = "GL"
    print("Teste 3")
    t = Solution() 
    print(t.isRobotBounded(instructions3)) # true
    
#main()