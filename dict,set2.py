n=list(map(int,input().split(' ')))
n.sort()
for i in n:
    if n.count(i)>1:
         n.remove(i)
print(n)