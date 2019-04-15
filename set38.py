s=str(input())
l=[]
for i in range(0,len(s)):
    l.append(s[i])
r=[]
for i in l:
    if i in r:
        next
    else:
        r.append(i)
print(*r,sep='')
