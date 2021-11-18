def swap_vowel_case(st):     
    res = ""
    for i in st:
        if i in "aeouiAEOUI":
            if i.islower(): i = i.upper()
            elif i.isupper(): i = i.lower()
        res += i
    return res