def f(n):
    if n<10:
        return n
    else:
        n=str(n)
        length=len(n)//2
        i=1
        while i<=(length):
            if n[i-1]==n[-i]:
                return n
            else:
                return False


