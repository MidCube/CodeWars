def meeting(rooms):
    for i in range(len(rooms)):
        if rooms[i]=="O":
            return i
    return 'None available!'
