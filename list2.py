n=int(input())
x=list(map(int,input().split()))
i=0
while i<len(x):
    if x.count(x[i])>1:
        x.remove(x[i])
    i+=1
x.sort()
for i in x:
    print(i,end=(' '))