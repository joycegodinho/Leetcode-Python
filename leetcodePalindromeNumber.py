class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        i = 0
        j = len(x) - 1
        igual = True
        
        if len(x) > 2:

            while j > 1 and igual:
                if x[i] != x[j]:
                    igual= False
                i = i + 1
                j = j - 1
            return igual
        
        elif len(x) == 2:
            
            if x[0] != x[1]:
                igual= False
            return igual
        
        return igual
            

def main():
    
    x = 121 
    print("Teste 1")
    u = Solution() 
    print(u.isPalindrome(x)) # true
    
    x2 = -121
    print("Teste 2")
    u = Solution() 
    print(u.isPalindrome(x2)) # false

    x3 = 10
    print("Teste 3")
    u = Solution() 
    print(u.isPalindrome(x3)) # false
    
    x4 = -101
    print("Teste 4")
    u = Solution() 
    print(u.isPalindrome(x4)) # false
    
    x5 = 1
    print("Teste 5")
    u = Solution() 
    print(u.isPalindrome(x5)) # true
    
main()