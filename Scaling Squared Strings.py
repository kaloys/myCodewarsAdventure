def scale(strng, k, n):
    if strng=='': return ''
    newl = []
    for word in strng.split('\n'):
        for i in range(n):
            newl.append(''.join([i*k for i in word]))
    return '\n'.join(newl)