def paul(x):
    lookupDic = {"kata":5, "Petes kata":10, "life":0, "eating":1}
    total=0
    for item in x:
        total+=lookupDic[item]
    if total<40:
        return "Super happy!"
    elif total <70:
        return "Happy!"
    elif total<100:
        return "Sad!"
    else:
        return "Miserable!"
