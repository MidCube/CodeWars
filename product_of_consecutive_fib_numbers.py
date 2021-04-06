def productFib(prod):
    f1=0
    f2=1
    while f1*f2 < prod:
        temp = f1+f2
        f1=f2
        f2=temp
    if f1*f2 == prod:
        result = [f1,f2,True]
    else:
        result = [f1,f2,False]
    return result
