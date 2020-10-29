class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        dicionario = {'M': 1000, 'D':500, 'C':100,'L':50, 'X':10, 'V':5, 'I':1}
        resp = 0 
        comp = len(s)-1

        for i in range(comp):
            if dicionario[s[i]] < dicionario[s[i+1]]:
                resp = resp - dicionario[s[i]]
            else:
                resp = resp + dicionario[s[i]]
        resp = resp + dicionario[s[-1]]
        return resp

def main():
    
    s = "III"
    print("Teste 1")
    u = Solution() 
    print(u.romanToInt(s)) # 3
    
    s2 = "IV"
    print("Teste 2")
    u = Solution() 
    print(u.romanToInt(s2)) # 4

    s3 = "IX"
    print("Teste 3")
    u = Solution() 
    print(u.romanToInt(s3)) # 9
    
    s4 = "LVIII"
    print("Teste 4")
    u = Solution() 
    print(u.romanToInt(s4)) # 58
    
    s5 = "MCMXCIV"
    print("Teste 5")
    u = Solution() 
    print(u.romanToInt(s5)) # 1994
    
main()


