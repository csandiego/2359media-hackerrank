def findSmallestDivisor(s, t):
    x, y = len(s), len(t)
    # if s isn't divisible by t just based on their lengths
    if x % y != 0:
        return -1
    # if s isn't merely a result of repeated t's
    if s != t * (x // y):
        return -1
    # if t is divisible by some substring j, return len(j)
    i, j = 0, ''
    while i < y:
        j += t[i]
        i += 1
        if y % i == 0 and t == j * (y // i):
            return len(j)
    # if there are no repetitions within t, return len(t)
    return len(t)

print(findSmallestDivisor('bcdbcdbcdbcd', 'bcdbcd'))