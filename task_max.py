def find_max(a,b,c):
    """
    Find the maximum number.
    Args:

        a: int
        b: int
        c: int
    return:
        int
    """
    m = a
    if m<b:
        m=b
    if m<c:
        m=c
    return m
a,b,c = 3, 8,21
print(find_max(a,b,c))

# Example:
# find_max(1,2,3) -> 3
# find_max(-1,12,3) -> 12

def find_max_idx(a,b,c):
    """
    Find the index of the maximum number.
    Args:
        a: int
        b: int
        c: int
    return:
        int
    """
    f = 1
    d = a
    if d<b:
        f+=1
    if d<c:
        f+=2
    return f
a,b,c = 100,2,13
print(find_max_idx(a,b,c))

# Example:
# find_max_idx(10,2,13) -> 3
# find_max_idx(-1,12,3) -> 2