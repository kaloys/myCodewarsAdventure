def last_survivor(s, arr):
    l = list(s)
    for i in arr: del(l[i])
    return ''.join(l)