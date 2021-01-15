###Leetcode - longest common prefix

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if len(strs)==0:
            return ""
        
        strs.sort() 
        first = strs[0]
        last = strs[-1]
        limite = min(len(first), len(last))
        resp=""
        
        
        for cont in range(limite):
            if first[cont] == last[cont]:
                resp = resp + first[cont]
                  
            else:
                break
                    

        return resp
        
        
def main():
    
    strs = ["flower","flow","flight"] 
    print("Teste 1")
    s = Solution() #chamo a classe
    print(s.longestCommonPrefix(strs)) # fl
    
    
    strs2 = ["dog","racecar","car"]
    print("Teste 2")
    r = Solution() #chamo a classe
    print(r.longestCommonPrefix(strs2)) # ""
    
    

    
#main()