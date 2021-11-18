def sort_vowels(s):
    if str(s).isdigit() or s==None: return ''
    return '\n'.join(['|'+i if i in 'aeiouAEIOU' else i+'|' for i in s])