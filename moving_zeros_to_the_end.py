def move_zeros(array):
    for item in array:
        if item==0:
            array.remove(0)
            array.append(0)
    return array
