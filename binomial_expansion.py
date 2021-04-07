import math

def expand(expr):
    expr=expr.split(")")
    expr[1]=expr[1][1:]
    power=int(expr[1])
    if power==0:
        return "1"
    expr[0]=expr[0][1:]
    xco=""
    x=""
    y=""
    onXCo=True
    onX=False
    for letter in expr[0]:
        if onXCo:
            if letter=="-":
                xco+=letter
            else:
                try:
                    int(letter)
                    xco+=letter
                except ValueError:
                    x+=letter
                    onXCo=False
                    onX=True
        elif onX:
            if letter=="-":
                y+=letter
                onX=False
            elif letter=="+":
                onX=False
            else:
                x+=letter
        else:
            y+=letter
    if xco=="-":
        xco+="1"
    if xco=="":
        xco+="1"
    
    #now do the maths
    result=""
    xco = int(xco)
    y=int(y)
    for i in range(power+1):
        c=math.comb(power,i)
        cx=xco**(power-i)
        cy=y**i
        total=c*cx*cy
        if i==power:
            if total>0:
                result+="+"+str(total)
            else:
                result+=str(total)
        elif i==0:
            if power!=1:
                if total==1:
                    result+=x+"^"+str(power-i)
                elif total==-1:
                    result+="-"+x+"^"+str(power-i)
                else:
                    result+=str(total)+x+"^"+str(power-i)
            else:
                if total==1:
                    result+=x
                elif total==-1:
                    result+="-"+x
                else:
                    result+=str(total)+x
        elif power-i==1:
            if total>0:
                result+="+"+str(total)+x
            elif total==1:
                result+=x
            elif total==-1:
                result+="-"+x
            else:
                result+=str(total)+x
        else:
            if total>0:
                result+="+"+str(total)+x+"^"+str(power-i)
            elif total==1:
                result+=x+"^"+str(power-i)
            elif total==-1:
                result+="-"+x+"^"+str(power-i)
            else:
                result+=str(total)+x+"^"+str(power-i)
    return result
