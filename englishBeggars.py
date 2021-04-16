def beggars(values, n):
    if n == 0:
        return []
    results = [[] for i in range(n)]
    for i in range(len(values)):
        results[i%n].append(values[i])
        
    results2=[]
    for item in results:
        results2.append(sum(item))
    return results2
