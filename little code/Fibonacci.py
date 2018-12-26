a=0                          #迭代法
b=1
n=0
while n<6:
    a,b=b,a+b
    n+=1
    print(a)

def fib(max):               #生成器法
    n,a,b = 0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1
for n in fib(6):
    print(n)
