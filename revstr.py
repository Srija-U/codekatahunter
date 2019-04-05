s=str(input())
sp=s.split()
l=len(sp)
a=[]
for i in range(0,l):
    a.append((sp[i][::-1]))
print(*a,sep=' ')
