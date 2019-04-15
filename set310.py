n=int(input())
l=[int(i) for i in input().split()]
li=[int(i) for i in input().split()]
c=1
i=0
for j in range(i+1,n):
    if(li[i]<=l[j]):
        c+=1
        i=j
print(c)
