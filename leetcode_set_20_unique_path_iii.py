# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 16:49:08 2020

@author: joyce
"""

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        
        linhas = len(grid)
        colunas = len(grid[0])
        si = None
        sj = None
        ei = None
        ej = None
        spaces = 0
        
        for i in range(linhas):
            for j in range(colunas):
                
                if grid[i][j] == 1:
                    si, sj = i, j
                    grid[i][j] = 0
                    
                if grid[i][j] == 2:
                    ei, ej = i, j
                    grid[i][j] = 0
                    
                if grid[i][j] == 0:
                    spaces = spaces + 1
                    
    
        caminho = 0
        direc = [(1,0),(0,1),(-1,0),(0,-1)]
        
        def backtrack( ci, cj, ei, ej, visto):
            
            if ci==ei and cj==ej and len(visto)==spaces:
                
                nonlocal caminho
                caminho = caminho + 1
                return
            
            for di,dj in direc:
                
                ni,nj = ci+di, cj+dj
                
                if 0 <= ni < linhas and 0 <= nj < colunas and grid[ni][nj] == 0 and (ni,nj) not in visto:
                    
                    visto.add((ni,nj))
                    backtrack(ni,nj,ei,ej,visto)
                    visto.remove((ni,nj))
                    
        visto = set()
        visto.add((si,sj))
        backtrack(si,sj,ei,ej,visto)
    
    
        return caminho