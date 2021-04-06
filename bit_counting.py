def count_bits(n):
    bits = bin(n)
    count = 0
    for i in range(len(bits)):
        if bits[i]=="1":
            count+=1
    return count
