n=int(input())
l=[int(i) for i in input().split()]
le=len(l)
l.sort()
a={}
a[l[0]]=1
for i in range(1,le):
    a[l[i]]=1
    if(l[i-1]==l[i]):
        a[l[i]]=2
        i=i+1
b=list(a.keys())
c=list(a.values())
print(b[c.index(1)])
