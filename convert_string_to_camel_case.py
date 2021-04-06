def to_camel_case(text):
    #your code here
    result = ""
    for i in range(len(text)):
        if text[i]!="-" and text[i]!="_":
            if i!=0:
                if text[i-1]=="-" or text[i-1]=="_":
                    result+=text[i].upper()
                else:
                    result+=text[i]
            else:
                result+=text[i]
    return result
