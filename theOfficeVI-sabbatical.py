def sabb(s, val, happiness):
    word = "sabbatical"
    word = [letter for letter in word]
    count = 0
    for letter in s:
        if letter in word:
            count+=1
    total = count+val+happiness
    if total>22:
        return "Sabbatical! Boom!"
    return "Back to your desk, boy."
