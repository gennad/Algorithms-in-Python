def gcd_rec(m, n):
    if m % n == 0:
        return n
    return gcd_rec(n, m %n)

def gcd_iter(m, n):
    while m % n != 0:
        temp = n
        n = m % n
        m = temp
    return n

if __name__ == '__main__':
    print gcd_rec(40, 10)
    print gcd_iter(40, 10)
