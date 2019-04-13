n=int(input())
l=[int(i) for i in input().split()]
for i in range(0,len(l)-2):
    for j in range(i+1,len(l)-1):
        for k in range(j+1,len(l)):
            if(l[i]+l[j]==l[k]):
                print(l[i],l[j],l[k],end="\n")
