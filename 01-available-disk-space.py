def segment(x, space):
    # Write your code here
    mx = None
    for i in range(0, len(space) + 1 - x):
        mn = None
        for j in range(i, i + x):
            if mn == None or space[j] < mn:
                mn = space[j]
        if mx == None or mn > mx:
            mx = mn
    return mx

def segment2(x, space):
    # Write your code here
    s = [space[i:i + x] for i in range(0, len(space) + 1 - x)]
    mn = [min(i) for i in s]
    mx = max(mn)
    return mn

def segment3(x, space):
    # Write your code here
    return max([min(s) for s in [space[i:i + x] for i in range(0, len(space) + 1 - x)]])


print(segment3(2, [8, 2, 4, 6]))