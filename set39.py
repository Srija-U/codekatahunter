n=int(input())
l=[int(i) for i in input().split()]
a=[]
for i in range(0,n):
    a.append(l[i])
maxsofar=a[0]
currmax=a[0]
for i in range(1,n):
    currmax=max(a[i],currmax+a[i])
    maxsofar=max(currmax,maxsofar)
print(maxsofar)
