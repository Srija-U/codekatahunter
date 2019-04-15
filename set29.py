n,m=map(int,input().split())
a=[]
for i in range(0,n):
    b=set([int(i) for i in input().split()])
    a.append(b)
t=set.intersection(*a)
print(*t,sep=' ')
