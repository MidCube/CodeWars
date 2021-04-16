def partition(arr, classifier_method):
    result=([],[])
    for item in arr:
        if classifier_method(item):
            result[0].append(item)
        else:
            result[1].append(item)
    return result
