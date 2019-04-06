class st:
    def __init__(self):
        self.items=[]
    def isempty(self):
        return(self.items==[])
    def push(self,data):
        self.items.append(data)
    def pop(self):
        return self.items.pop()
s=st()
txt=str(input())

for i in txt:
    s.push(i)
rev=''
while not s.isempty():
    rev=rev+s.pop()

if(rev==txt):
    print("YES")
else:
    print("NO")
