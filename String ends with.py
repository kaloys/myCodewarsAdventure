def solution(string, ending):
    return ending in string[-len(ending):]

def solution(string, ending):
    return string.endswith(ending)