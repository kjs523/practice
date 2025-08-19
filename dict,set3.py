x=input().split(' ')
a={}
for i in x:
    if i not in a:
        a.setdefault(i,x.count(i))
print(a)