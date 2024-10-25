"""
https://en.wikipedia.org/wiki/Levenshtein_distance

time O(mn)
space O(mn)

It is often used to find relevance of a short string in a longer text. The shorter the distance, the closer the relationship between text and string.
However, efficiency suffers when we need to compute edit distance for two long strings.
"""

from functools import cache

def distance(a, b):
    @cache
    def min_change(a, b, i, j):
        if i == len(a):
            return len(b)-j
        if j == len(b):
            return len(a)-i
        if a[i] == b[j]:
            return min_change(a, b, i+1, j+1)
        else:
            return 1 + min(
                min_change(a, b, i+1, j), # replace
                min_change(a, b, i, j+1), # insert
                min_change(a, b, i+1, j+1) # replace
            )
    return min_change(a, b, 0, 0)

def iterative_distance(a, b):
    m = len(a)
    n = len(b)

    d = [[0]*(n+1) for i in range(m+1)]
    for i in range(1, m+1):
        d[i][0] = i

    for j in range(1, n+1):
        d[0][j] = j

    for j in range(1, n+1):
        for i in range(1, m+1):
            cost = 0 if a[i-1] == b[j-1] else 1
            d[i][j] = min(
                d[i-1][j] + 1, # delete
                d[i][j-1] + 1, # insert
                d[i-1][j-1] + cost, # replace
            )
    return d[m][n]

if __name__ == "__main__":
    assert distance("kitten", "sitting") == 3
    assert iterative_distance("kitten", "sitting") == 3
