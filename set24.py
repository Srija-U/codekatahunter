from itertools import permutations
txt=str(input())
l=set(permutations(txt))
for i in l:
    print(''.join(i))
