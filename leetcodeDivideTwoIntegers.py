class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend/divisor >= 2147483647:
            return 2147483647
        if dividend/divisor <= -2147483648:
            return -2147483648
        else:

            divid = abs(dividend)
            div = abs(divisor)
            cont = 0

            if dividend*divisor < 0:
                sign = -1
            else:
                sign = 1

            
            while divid >= div:
                temp = div
                cont2 = 1
                while divid >= temp:
                    divid = divid - temp
                    cont = cont + cont2
                    temp = temp + temp
                    cont2 = cont2 + cont2
              
        return sign*cont


def main():

    s = Solution() 
    
    dividend = 10
    divisor = 3
    print("Teste 1")
    print(s.divide(dividend, divisor)) # 2

    
    dividend2 = 7
    divisor2 = -3
    print("Teste 2")
    print(s.divide(dividend2, divisor2)) # 2

    dividend3 = 11
    divisor3 = 3
    print("Teste 3")
    print(s.divide(dividend3, divisor3)) # 2

    dividend4 = 0
    divisor4 = 1
    print("Teste 4")
    print(s.divide(dividend4, divisor4)) # 2

    dividend5 =-2147483648
    divisor5 = -1
    print("Teste 5")
    print(s.divide(dividend5, divisor5)) # 2


main()