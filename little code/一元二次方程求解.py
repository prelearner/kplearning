import math
def quadratic(a,b,c):
    if a==b==c==0:
        print('该方程组的解为全体实数')
    if a==b==0 and c!=0:
        print('该方程组无实数解')
    if a==0:
        if b!=0:
            print('x1=x2=%f'%(-c/b))
    else:
        if pow(b,2)-4*a*c<0:
            print('该方程组无实数解')
        if pow(b,2)-4*a*c==0:
            print('x1=x2=%d'%((-b)/2*a))
        if pow(b,2)-4*a*c>0:
            x=pow(b,2)-4*a*c
            y=math.sqrt(x)
            z1=(-b+y)/(2*a)
            z2=(-b-y)/(2*a)
            print('x1=%.3f,x2=%.3f'%(z1,z2))
quadratic(2,5,1)





