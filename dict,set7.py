a=input().split(',')
b=input().split(',')
c=input().split(',')
d=input().split(',')
e=input().split(',')
x=(a,b,c,d,e)
y={}
for i in x:
    if int(i[1])>=160:
        y.setdefault(i[0],int(i[1]))
print(y)