from math import sqrt
def is_square(arr):
    if not arr: return None
    res = [True if int(sqrt(i))**2 == i else False for i in arr]
    return True if all(res) else False