def zero(n = None): return 0 if n is None else n(0)
def one(n = None): return 1 if n is None else n(1)
def two(n = None): return 2 if n is None else n(2)
def three(n = None): return 3 if n is None else n(3)
def four(n = None): return 4 if n is None else n(4)
def five(n = None): return 5 if n is None else n(5)
def six(n = None): return 6 if n is None else n(6)
def seven(n = None): return 7 if n is None else n(7)
def eight(n = None): return 8 if n is None else n(8)
def nine(n = None): return 9 if n is None else n(9)


def plus(num): return lambda x: x + num
def minus(num): return lambda x: x - num
def times(num): return lambda x: x * num
def divided_by(num): return lambda x: x // num

print(seven(times(five())))
