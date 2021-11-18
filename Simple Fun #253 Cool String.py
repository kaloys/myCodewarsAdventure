def cool_string(s): 
    if len(s) <= 1 and s[0].isdigit():
        return False
    for i in range(len(s)-1):
        if s[i].isspace() or s[i+1].isspace(): return False
        if s[i].isdigit() or s[i+1].isdigit(): return False
        if s[i].isupper() and s[i+1].isupper(): return False
        if s[i].islower() and s[i+1].islower(): return False
    return True