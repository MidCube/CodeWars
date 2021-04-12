def cake(candles,debris):
    #your code here
    total = 0
    for i in range(len(debris)):
        if i%2==0:
            total+=ord(debris[i])
        else:
            total+=ord(debris[i])-96
    return "That was close!" if total<=candles*0.7 or candles==0 else "Fire!"
