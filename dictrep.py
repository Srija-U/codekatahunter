n=int(input())
ab=[int(i) for i in input().split()]
l=len(ab)
ab.sort()
b={}
c=[]
t=[]
te=0
for i in range(0,l):
    if(ab[i] in b):
        next
    else:
        b[ab[i]]=0
        c.append(ab[i])
le=len(c)
for i in range(0,le):
    for j in range(0,l):
        if(c[i]==ab[j]):
            b[c[i]]+=1
d=list(b.values())
#c-->key_list
#d-->val_list
for i in range(0,le):
    if(d[i]>1):
        t.append(c[d.index(d[i])])
        b.pop(c[d.index(d[i])],None)
        c=list(b.keys())
print(*t,sep=' ')
