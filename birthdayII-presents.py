def present(x,y):
    #your code here
    if x=="goodpresent":
        return "".join([chr(ord(s)+y) for s in x])
    elif x=="crap" or x=="empty":
        #for some reason when I use .sort() on a list it returns none so I can't join it
        #but only 2 cases so no need to bother too much
        return "acpr" if x=="crap" else "empty"
    elif x=="bang":
        temp=[ord(n)-y for n in x]
        return str(sum(temp))
    elif x=="badpresent":
        return "Take this back!"
    else:
        return "pass out from excitement "+str(y)+" times"
