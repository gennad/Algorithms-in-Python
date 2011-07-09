#!/usr/bin/env python  
# -*- coding: utf-8 -*-
"""
Josephus permutation. A theoretical problem related to a certain
counting out game. See en.wikipedia.org/wiki/Josephus_problem
or http://mathworld.wolfram.com/JosephusProblem.html for more details.

Created by Huascar A. Sanchez on 2011-03-21.
Copyright (c) 2011 Huascar A. Sanchez. All rights reserved.
"""

from collections import deque
def Josephus(m,n,s = 1):
    """Josephus problem. Only s survivor (s) (the winner(s)).
       Input: n - number of people in the circle
              m - frequency of people to be killed.
              s - number of survivors you want.
       Output: not output. all results will be printed
       on screen.
    """
    N = n + 1
    M = m - 1
    S = s
    if S <= 0: S = 1 # only one survivor  
    Q = deque()
    #print("construct the list\n")  
    for p in range(1,N):
        Q.append(p)

    toString = []
    #print("start the game now!!\n")  
    while len(Q) > S:
        for dp in range(0,M):
            Q.append(Q.popleft())
        toString.append(str(Q.popleft()))

    print(' '.join(toString))
    while Q:
       print("winner " + str(Q.popleft()))

Josephus(5,9)
Josephus(3,40,2)
