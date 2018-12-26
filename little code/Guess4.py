from random import randint

name=input('请输入你的名字 ')

f=open('file2.txt')     #5-10行把文件里的数据存到字典里，方便查找
line=f.readlines()      #按行读取至列表
#print(line)
scores={}
for l in line:
    s=l.split()         #把每一行的数据拆分成一个列表
    scores[s[0]]=s[1:]  #通过赋值的方式存入字典中
#print(scores)

score=scores.get(name)  #按照名字找出字典里存放的数据
if score==None:
    score=[0,0,0]

game_times=int(score[0])   #把数据赋值给变量，用来给26行输出以及后续的更改
min_times=int(score[1])
total_times=int(score[2])

if game_times>0:
    avg_times=float(total_times)/game_times
else:
    ave_times=0
print('%s,你已经玩了%d次游戏,最少%d轮猜出答案,平均%d轮猜出答案'%(name,game_times,min_times,total_times))

answer=randint(0,100)      #游戏开始
bingo=False
times=0
print('Guess what I think?')

while bingo==False:
    num=int(input())
    times+=1
    if num<answer:
        print(str(num)+' is too small')
    if num>answer:
        print(str(num)+' is too big')
    if num==answer:
        print('Bingo!')
        bingo=True

if game_times==0 or times<min_times:   #更新数据
    min_times=times
total_times+=times
game_times+=1

scores[name]=[str(game_times),str(min_times),str(total_times)] #用更改后的数据更新字典
result=''                   #初始化一个空字符串，用来存放数据
for i in scores:            #这里的i调用的是字典里的key
    #print(scores[i])
    g=i+' '+' '.join(scores[i])+'\n'    #按照"名字 成绩"的方式存入空字符串，每个人的数据结尾换行
    #print(g)
    result+=g

f=open('file2.txt','w')     #将更新后的数据存入文件
f.write(result)
f.close()






