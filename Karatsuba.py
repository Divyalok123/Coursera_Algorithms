def Karatsuba(num1, num2): 
        numstr1 = str(num1)
        numstr2 = str(num2)
        if(num1 < 50 or num2 < 50):
            return num1*num2
        length = (len(numstr1) + len(numstr2))//2
        splitlen1 = len(numstr1)//2
        splitlen2 = len(numstr2)//2
        
        high1, low1 = int(numstr1[:-splitlen1]), int(numstr1[-splitlen1:])
        high2, low2 = int(numstr2[:-splitlen2]), int(numstr2[-splitlen2:])
        p1 = Karatsuba(low1, low2)
        p2 = Karatsuba((high1 + low1), (high2 + low2))
        p3 = Karatsuba(high1, high2)
        return p1 + (p2-p1-p3)*10**(length/2) + (p3*10**(length))