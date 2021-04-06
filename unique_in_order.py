def unique_in_order(iterable):
    result = []
    for i in range(len(iterable)):
        if i==0:
            result.append(iterable[i])
        else:
            if iterable[i] != iterable[i-1]:
                result.append(iterable[i])
    return result
