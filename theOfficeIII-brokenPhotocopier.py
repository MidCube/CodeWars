def broken(inp):
    result=""
    for i in inp:
        if i=="0":
            result+="1"
        else:
            result+="0"
    return result
