n=int(input())
a=[int(i) for i in input().split()]
l=len(a)
a.sort()
b={}
c=[]
t=[]
te=0
for i in range(0,l):
    if(a[i-1]==a[i]):
        next
    else:
        b[a[i]]=0
        c.append(a[i])
le=len(c)
for i in range(0,le):
    for j in range(0,l):
        if(c[i]==a[j]):
            b[c[i]]+=1
d=list(b.values())
#c-->key_list
#d-->val_list
for i in range(0,le):
    if(d[i]==1):
        te+=1
if(te==le):
    print("unique")
    exit()
for i in range(0,le):
    if(d[i]>1):
        t.append(c[d.index(d[i])])
        b.pop(c[d.index(d[i])],None)
        c=list(b.keys())
print(*t,sep=' ')
