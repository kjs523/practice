x=input().split(',')
a={}
for i in x:
    if len(''.join(i))>=5:
        a.setdefault(i,len(''.join(i)))
print(a)