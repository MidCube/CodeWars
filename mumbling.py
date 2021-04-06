def accum(s):
    result=""
    for i in range(len(s)):
        result+=s[i].upper()
        for ii in range(i):
            result+=s[i].lower()
        result+="-"
    return result[:-1]
