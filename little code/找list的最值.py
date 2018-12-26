def findMinandMax(L):
    min=0
    max=0
    L.append(min)
    L.append(max)
    for i in L:
        if min>i:
            min=i
        if max<i:
            max=i
    print(min,max)
a=[-1,2,3,5,8]
findMinandMax(a)