n,m=map(int,input().split())
l=[]
for i in range(0,n):
    l.append([int(i) for i in input().split()])
c=0
te=l
for i in range(0,n):
    for j in range(0,m):
        if(l[i][j]==0):
            c+=1
for i in range(0,n,1):
    for j in range(0,m,1):
        if(c>0):
            if(l[i][j]==0):
                for s in range(0,n):
                    te[s][j]=0
                for t in range(0,m):
                    te[i][t]=0
                c-=1
                
for i in range(0,n):
    print(*te[i],sep=' ')
