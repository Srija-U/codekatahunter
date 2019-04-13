n,m=map(int,input().split())
l=[int(i) for i in input().split()]
li=[int(i) for i in input().split()]
f=0
if(all(x in l for x in li)):
    f=1
if(f):
    print("YES")
else:
    print("NO")
