def baby_count(x):
    count=0
    x=[letter.lower() for letter in x]
    print(x)
    while True:
        try:
            x.remove('b')
            x.remove('a')
            x.remove('b')
            x.remove('y')
            count+=1
            
        except ValueError:
            break
    if count>0:
        return count
    else:
        return 'Where\'s the baby?!'
