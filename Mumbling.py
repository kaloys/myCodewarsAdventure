def accum(s):
    return '-'.join(s[i].upper()+(s[i]*i).lower() for i in range(len(s)))