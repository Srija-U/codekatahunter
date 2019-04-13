n=int(input())
l=[int(i) for i in input().split()]
d={}
for i in l:
    if i not in d.keys():
        d.update({i:1})
        if(l.index(i)==n-1):
            print("unique")
    else:
        print(i)
        break
