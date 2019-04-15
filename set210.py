a,b=map(int,input().split())
t=a
l=[]
res=0
for i in range(0,b-a+1):
    l.append(format(t,'b'))
    t+=1
for i in range(0,len(l)):
    t=str(l[i])
    te=0
    for j in range(0,len(t)):
        if(t[j]=='1'):
            te+=1
    if te>1:
        if(te==2):
            res+=1
            next
        for k in range(2,te+1):
            if(te%k==0):
                break
            else:
                res+=1
           
print(res)
