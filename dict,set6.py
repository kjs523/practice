x=input().split(' ')
for i in x:
    if x.count(i)<2:
        x.remove(i)
y=set(x)
print(y)