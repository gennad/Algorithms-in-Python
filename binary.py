def binary(seq, x):
    l = 0
    r = len(seq)
    while l < r:
        m = (l + r) // 2
        if seq[m] < x:
            l = m + 1
        else:
            r = m
    if seq[l] == x:
        return l
    else:
        return -1

if __name__ == '__main__':
    print binary([1,2,3,4,5,6,7,8], 10)
