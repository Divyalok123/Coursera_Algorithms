#only for the multiplication of even and same digit numbers 
def Karatsuba(num1, num2): 
        numstr1 = str(num1)
        numstr2 = str(num2)
        if(num1 < 10 or num2 < 10):
            return num1*num2
        length = (len(numstr1) + len(numstr2))//2
        splitlen = length//2
        high1, low1 = int(numstr1[:-splitlen]), int(numstr1[-splitlen:])
        high2, low2 = int(numstr2[:-splitlen]), int(numstr2[-splitlen:])
        p1 = Karatsuba(low1, low2)
        p2 = Karatsuba((high1 + low1), (high2 + low2))
        p3 = Karatsuba(high1, high2)
        return int(p1 + (p2-p1-p3)*10**(splitlen) + (p3*10**(splitlen*2)))
    

                                                                                                                                