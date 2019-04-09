n=int(input())
l=[int(i) for i in input().split()]
li=[]
for i in range(len(l)-1,0,-1):
    li.append(l[i])
    li.append('->')
li.append(l[0])
print(*li,sep='')
