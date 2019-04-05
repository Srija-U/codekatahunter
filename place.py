n=int(input())
l=[int(i) for i in input().split()]
le=len(l)
a=[]
res=[]
for i in range(0,le):
    a.append(i)
c=0
for i in range(0,le):
    if(a[i]==l[i]):
        res.append(a[i])
        c=1
if(c==0):
    print('-1')
print(*res,sep=" ")

