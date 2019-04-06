n=int(input())
l=[int(i) for i in input().split()]
l.sort()
b=[]
for i in range(n,0,-1):
    b.append(l[i-1])
c=0
for i in range(0,n):
    if(l[i]==0):
        c=c+1
if(c==n):
    print('0')
else:
    print(*b,sep='')
