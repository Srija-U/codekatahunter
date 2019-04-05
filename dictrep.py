no=int(input())
ab=[int(i) for i in input().split()]
l=len(ab)
ab.sort()
ba={}
ca=[]
ta=[]
te=0
for i in range(0,l):
    if(ab[i] in ba):
        next
    else:
        ba[ab[i]]=0
        ca.append(ab[i])
le=len(ca)
for i in range(0,le):
    for j in range(0,l):
        if(ca[i]==ab[j]):
            ba[ca[i]]+=1
da=list(ba.values())
#ca-->key_list
#da-->val_list
for i in range(0,le):
    if(da[i]>1):
        ta.append(ca[da.index(da[i])])
        ba.pop(ca[da.index(da[i])],None)
        ca=list(ba.keys())
print(*ta,sep=' ')
