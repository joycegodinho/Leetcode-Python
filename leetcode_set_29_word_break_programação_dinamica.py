# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 17:36:35 2020

@author: joyce
"""
######Leetcode 29 - Word Break- programação dinâmica

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
        
        '''  
        v = s
        wordDict.sort(key=len, reverse=False)
        
        for i, string in enumerate(wordDict) :
            if string in s:
                s = s.replace(str(string), "1")
                
        wordDict.sort(key=len, reverse=True)
        
        for i, string in enumerate(wordDict) :
            if string in v:
                v = v.replace(str(string), "1")
                
        s = s.replace("1", "")
        v = v.replace("1", "")
       

        
        if len(s) ==  0 or len(v) ==  0:
            return True , wordDict, v, s
        else:
            return False , wordDict, s,v
        '''
        dp = [False]*(len(s)+1)
        dp[0] = True
        wordDict = set(wordDict)
        
        for i in range(len(s)):
            for j in range(i+1):
                if not dp[j]:
                    continue
                string = s[j:i+1]
                if string in wordDict:
                    dp[i+1] = True
                    break
        
        return dp[-1]
        
                
def main():
    
    s = "leetcode"
    wordDict = ["leet", "code"]
    print("Teste 1")
    u = Solution() 
    print(u.wordBreak(s, wordDict)) # True
    
    s2 = "applepenapple"
    wordDict2 = ["apple", "pen"]
    print("Teste 2")
    v = Solution() 
    print(v.wordBreak(s2, wordDict2)) # True
    
    s3 = "catsandog"
    wordDict3 = ["cats","dog","sand","and","cat"]
    print("Teste 3")
    x = Solution() 
    print(x.wordBreak(s3, wordDict3)) # False
    
    s4 = "a"
    wordDict4 = []
    print("Teste 4")
    z = Solution() 
    print(z.wordBreak(s4, wordDict4)) # False
    
    s5 = "bb"
    wordDict5 = ["a","b","bbb","bbbb"]
    print("Teste 5")
    y = Solution() 
    print(y.wordBreak(s5, wordDict5)) # True
       
    s6 = "cars"
    wordDict6 = ["car","ca","rs"]
    print("Teste 6")
    x = Solution() 
    print(x.wordBreak(s6, wordDict6)) # True
    
    s7 = "aaaaaaa"
    wordDict7 = ["aaaa","aaa"]
    print("Teste 7")
    q = Solution() 
    print(q.wordBreak(s7, wordDict7)) # True
    
    s8 = "cbca"
    wordDict8 = ["bc","ca"]
    print("Teste 8")
    p = Solution() 
    print(p.wordBreak(s8, wordDict8)) # False
    

main()
