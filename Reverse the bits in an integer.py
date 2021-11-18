def reverse_bits(n):
    binrev = bin(n)[::-1]
    return int(binrev[:-2], 2)