def meeting(rooms, number):
    if number==0:
        return 'Game On'
    result=[]
    for room in rooms:
        thing=room[1]-len(room[0])
        if not thing<0:
            if number>thing:
                result.append(thing)
                number-=thing
            else:
                result.append(number)
                number=0
        else:
            result.append(0)
        if number==0:
            break
    if number!=0:
        return "Not enough!"
    return result
        
