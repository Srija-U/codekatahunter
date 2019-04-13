n=int(input())
l=[int(i) for i in input().split()]
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if((round(l[i]+l[j])==0)or(round(l[i]+l[j])==-1)or(round(l[i]+l[j])==1)):
            print(l[i],l[j])
            exit()
