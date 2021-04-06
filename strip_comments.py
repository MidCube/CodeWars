import re

def solution(string,markers):
    if markers:
        lines = string.split("\n")
        regexPattern = '|'.join(map(re.escape, markers))
        result=[]
        for item in lines:
            item = re.split(regexPattern,item)
            if len(item)>1:
                item.pop()
            result.append(item[0].rstrip())
        result = "\n".join(result)
        return result
    return string
