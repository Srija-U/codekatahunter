n=int(input())
l=[int(i) for i in input().split()]
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if(round(l[i]+l[j])==0):
            print(l[i],l[j])
