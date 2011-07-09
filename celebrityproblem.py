def naive_celeb(G):
    n = len(G)
    for u in range(n):
        for v in range(n):
            if u == v: continue
            if G[u][v]: break
            if not G[v][u]: break
        else:
            return u
    return None

def celeb(G):
    n = len(G)
    u, v = 0, 1
    for c in range(2,n+1):
        if G[u][v]:
            u = c
        else:
            v = c
    if u == n:
        c = v
    else:
        c = u

    for v in range(n):
        if c == v:
            continue
        if G[c][v]:
            break
        if not G[v][c]:
            break
    else:
        return c
    return None

from random import randrange
n = 100
G = [[randrange(2) for i in range(n)] for i in range(n)]

c = randrange(n)
for i in range(n):
    G[i][c] = True
    G[c][i] = False
naive_celeb(G)
celeb(G)
