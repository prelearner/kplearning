def _odd_iter():         #定义一个无穷奇数列
    n=1
    while True:
        n=n+2
        yield n

def g(n):
    return lambda x:x%n>0

def h():
    yield 2               #2不在奇数列_odd_iter()中,但是素数,因此先输出2(12-16行是在奇数列中找出所有素数)
    it=_odd_iter()        #初始化一个新序列
    while True:
        n=next(it)        #返回序列的第一个数
        yield n
        it=filter(g(n),it)    #用n逐个检验新序列it中的元素,删除掉那些为n的倍数的数
for n in h():
    if n<1000:
        print(n)
    else:
        break



