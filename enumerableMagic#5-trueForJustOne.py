def one(sq, fun): 
    result = False
    for item in sq:
        if not result and fun(item):
            result=True
        elif result and fun(item):
            return False
    return result
