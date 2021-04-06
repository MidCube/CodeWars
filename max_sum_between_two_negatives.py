def max_sum_between_two_negatives(arr):
    max = -1
    total = 0
    hadNeg=False
    for n in arr:
        if hadNeg:
            if n>=0:
                total+=n
            else:
                if total>max:
                    print(total)
                    max = total
                total = 0
        else:
            if n<0:
                hadNeg = True
    return max
