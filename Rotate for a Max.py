def max_rot(n):
    newl = []
    newl.append(n)
    for i in range(len(str(n))-1):
        rleft = str(newl[i])
        fdigit = rleft[i]
        newleft = ''.join(rleft[c] for c in range(len(rleft)) if c != i)
        rleft = newleft+fdigit
        newl.append(int(rleft))
    return max(newl)