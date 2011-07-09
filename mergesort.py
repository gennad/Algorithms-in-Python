#Merges two sorted lists into one sorted list. recursively
def merge(left, right):
    if len(left) == 0 and len(right) == 0:
        return []
    elif len(left) == 0:
        return right
    elif len(right) == 0:
        return left
    else:
        if left[0] <= right[0]:
            return left[:1] + merge(left[1:],right)
        else:
            return right[:1] + merge(left,right[1:])

#Splits a list in half and returns the halves
def halve(list):
    return list[:len(list)//2],list[len(list)//2:]

#Mergesort
def mergesort(list):
    if len(list) <= 1:
        return list
    left,right = halve(list)
    left,right = mergesort(left),mergesort(right)
    return merge(left,right)


def mergesort2(seq):
    mid = len(seq) // 2
    lft, rgt = seq[:mid], seq[mid:]
    if len(lft) > 1:
        lft = mergesort(lft)
    if len(rgt) > 1:
        rgt = mergesort(rgt)

    res = []
    while lft and rgt:
        if lgt[-1] >= rgt[-1]:
            res.append(lft.pop())
        else:
            res.append(rgt.pop())
    res.reverse()
    return (lft or rgt) + res

