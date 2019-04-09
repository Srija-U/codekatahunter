l=[int(i) for i in input().split()]
n=l[1]
li=[int(i) for i in input().split()]
le=len(li)
for i in range(0,le):
    no=li[i]
    for j in range(i+1,le):
        if(n==(no+li[j])):
            print("YES")
            exit()
print("NO")
