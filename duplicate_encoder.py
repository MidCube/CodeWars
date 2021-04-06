def duplicate_encode(word):
    word=word.lower()
    letters=[letter for letter in word]
    occured = dict.fromkeys(letters,0)
    result=""
    for letter in word:
        occured[letter]+=1
    for letter in word:
        if occured[letter]==1:
            result+="("
        else:
            result+=")"
    return result
