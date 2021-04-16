def revrot(strng, sz):
    if sz <=0 or strng=="" or sz>len(strng):
        return ""
    n=len(strng)//sz
    result=""
    for i in range(n):
        slice = strng[i*sz:(i+1)*sz]
        total = sum([int(num)**3 for num in slice])
        if total%2==0:
            result+=slice[::-1]
        else:
            result+=slice[1:]+slice[0]
    return result
