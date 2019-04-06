n=str(input())
l=len(n)
s=0
for i in range(0,l):
    s+=int(n[i])
if(len(str(s))==1):
    print("YES")
else:
    temp=s
    rev=0
    while(s>0):
        dig=s%10
        rev=rev*10+dig
        s=s//10
    if(temp==rev):
        print("YES")
    else:
        print("NO")
