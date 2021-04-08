def outed(meet, boss):
    # your code here!
    total=0
    for key in meet.keys():
        if key==boss:
            total+=2*meet[key]
        else:
            total+=meet[key]
    total = total/len(meet.keys())
    if total <= 5:
        return "Get Out Now!"
    else:
        return "Nice Work Champ!"
