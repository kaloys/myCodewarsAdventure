def some_but_not_all(seq, pred): 
    return len(set([True if pred(i) else False for i in seq]))>1