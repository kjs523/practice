x=input()
a=x.lower()
b=set(a)
c=('q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m')
d=''.join(a)
y={}
for i in b:
    if i in c:
        y.setdefault(i,a.count(i))
print(y)