def each_cons(lst, n):
    result=[]
    for i in range(len(lst)):
        if i+n<=len(lst):
            result.append(lst[i:i+n])
    return result
