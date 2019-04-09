n=int(input())
l=[int(i) for i in input().split()]
a=[]
for i in range(0,len(l)):
    p=1
    for j in range(0,len(l)):
        if(i==j):
            next
        else:
            p*=l[j]
    a.append(p)
print(*a,sep=' ')
