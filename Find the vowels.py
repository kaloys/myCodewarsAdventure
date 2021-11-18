def vowel_indices(word):
    vow = 'aeiouy'
    return [i for i in range(1,len(word)+1) if word[i-1].lower() in vow]