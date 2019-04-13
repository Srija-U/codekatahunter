n=int(input())
l=[int(i) for i  in input().split()]
li=[]
for i in range(0,len(l)):
    if(l[i]%2==0):
        if(i%2!=0):
            li.append(l[i])
    else:
        if(i%2==0):
            li.append(l[i])
print(*li,sep=' ')
