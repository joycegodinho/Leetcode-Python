# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 14:25:30 2020

@author: joyce
"""

#### Leetcode 07: sum root to leaf

class Solution(object):
    def sumRootToLeaf(self, root):
            def sumRootToLeaf(root,sum):
                
                if root == None:
                    return 0
                sum = (sum << 1) + root.val
                
                if not root.left and not root.right:
                    return sum
                
                return sumRootToLeaf(root.left, sum) + sumRootToLeaf(root.right, sum)
            
            return sumRootToLeaf(root,0)  