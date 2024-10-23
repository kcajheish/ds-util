def hash(s):
    m = 10**9+1
    p = 31
    p_pow = 1
    hash_value = 0
    for c in s:
        hash_value += ((ord(c)-ord('a')+1) * p_pow) % m
        p_pow = (p_pow * p) % m
    return hash_value
