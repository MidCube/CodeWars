#------------------Bad Code----------------------------------
"""import math

def first_tooth(array):
    n=len(array)
    multiMax=False
    max=-math.inf
    maxLocation=-1
    diff=0
    for i in range(n):
        if i==0:
            if n>1:
                diff=array[i]-array[i+1]
            else:
                diff=0
        elif i==n-1:
            diff=array[i]-array[i-1]
        else:
            diff=array[i]-array[i-1]+array[i]-array[i+1]
        if diff>max:
            max=diff
            maxLocation=i
            multiMax=False
        elif diff==max:
            multiMax=True
    if multiMax:
        return -1
    else:
        return maxLocation"""

#-----------------------Better Code, still O(n)--------------

def first_tooth(lst):
    gums = lst[:1] + lst + lst[-1:]
    diff = [gums[i+1]*2 - gums[i] - gums[i+2] for i in range(len(lst))]
    m = max(diff)
    return diff.index(m) if diff.count(m) == 1 else -1
