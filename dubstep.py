#this was very late so the code is trash, should just use split on "WUB"

def song_decoder(song):
    currentWord=""
    lookingAtWord = False
    result=""
    for i in range(len(song)):
        if i<2:
            if song[i]=="W" and song[i+1]=="U" and song[i+2]=="B":
                result+=" "
            elif song[i-1]=="W" and song[i]=="U" and song[i+1]=="B":
                continue
            else:
                result+=song[i]
            
        elif song[i-2]=="W" and song[i-1]=="U" and song[i]=="B":
            continue
        elif song[i-1]=="W" and song[i]=="U" and song[i+1]=="B":
            continue
        elif song[i]=="W" and song[i+1]=="U" and song[i+2]=="B":
            result+=" "
        else:
            result+=song[i]
    
    prev=""
    result2=""
    for letter in result:
        if letter==" " and prev!=" ":
            result2+=letter
        if letter!=" ":
            result2+=letter
        prev=letter
            
    return result2.strip()
