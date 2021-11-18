def comfortable_word(word):
    newl = ["left" if word[i] in "qwertasdfgzxcvb" else "right" for i in range(len(word))]
    for i in range(len(newl)-1):
        if newl[i] == newl[i+1]: return False
    return True
    