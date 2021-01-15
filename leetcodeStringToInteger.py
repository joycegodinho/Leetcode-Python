class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """

        #retirar espaços

        s = s.strip()
        
        # declarar variáveis

        numerico = '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'
        semLetra = True
        i = 0
        resp = []
        sinal = 1

        # avaliar sinais
        
        if s == "":
            return 0

        if s[0] == "-":
            sinal = -1
            i = 1
  
        if s[0] == "+":
            i = 1
        # avaliar numeros
        
        while semLetra and i < len(s):
            if s[i] in numerico:
                resp.append(s[i])
                i = i + 1
            else:
                semLetra = False

        # transformar o vetor de strings em uma strings

        resp = "".join(resp)

        # avaliar tamanho e strings vazias

        if resp == "":
            return 0
        else:  
            resp = int(resp) * sinal
            if resp >= 2147483647:
                return 2147483647
            elif resp <= -2147483648:
                return -2147483648
            else:
                return resp

def main():
    
    s = "  -42"
    print("Teste 1")
    r = Solution() 
    print(r.myAtoi(s)) # 42

    s2 = "4193 with words"
    print("Teste 2")
    r = Solution() 
    print(r.myAtoi(s2)) # 4193

    s3 = "words and 987"
    print("Teste 3")
    r = Solution() 
    print(r.myAtoi(s3)) # 0

    s4 = "-91283472332"
    print("Teste 4")
    r = Solution()
    print(r.myAtoi(s4)) # -2147483648

    s5 = "+-12"
    print("Teste 5")
    r = Solution()
    print(r.myAtoi(s5)) # 0

    s6 = ""
    print("Teste 6")
    r = Solution()
    print(r.myAtoi(s6)) # 0

main()