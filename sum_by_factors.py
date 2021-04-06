#first 4 kyu task, definitely bloated

import math

def primeFactors(n,lst):
    n=abs(n)
    while n % 2 == 0:
        lst.append(2)
        n = n / 2
    
    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i== 0:
            lst.append(int(i))
            n = n / i
    
    if n > 2:
        lst.append(int(n))
    return list(dict.fromkeys(lst))
        
def sum_for_list(lst):
    factors = []
    for item in lst:
        primeFactors(item,factors)
    factors = list(dict.fromkeys(factors))
    factors.sort()
    result=[]
    for item in factors:
        temp = 0
        for num in lst:
            if num%item==0:
                temp+=num
        result.append([item,temp])
    return result
