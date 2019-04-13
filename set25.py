n=int(input())
l=[int(i) for i in input().split()]
s=[]
ss=[]
s.append(l[n-1])
for i in range(n-2,0,-1):
    t=c=0
    for j in range(i+1,n):
        c+=1
        if(l[i]>l[j]):
            t+=1
    if(t==c):
        s.append(l[i])
ss.append(max(l))
print(*s,sep=' ')
print(*ss,sep=' ')
