def fun(l):
    li=[]
    for i in range(len(l)):
        if((i+1)%2==0):
            li.append(l[i])
    return li
n=int(input())
l=[int(i) for i in input().split()]
t=l
while(len(l)>1):
    l=fun(l)
print(t.index(l[0]))
