#
def fibo1(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return fibo1(n-1)+fibo1(n-2)

def fibo2(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))

def fibo3(n):
    a,b = 0,1
    yield a
    yield b
    while True:
        a,b = b,a+b
        yield b

def subfibo1(start, end):
    n = 0
    cur = fibo2(n)
    while cur<=end:
        if start<= cur:
            print cur
        n += 1
        cur = fibo2(n)

def subfibo2(start, end):
    for cur in fibo2():
        if cur>end: return
        if cur>=start:
            yield cur

for i in subfibo1(10, 200):
    print i
