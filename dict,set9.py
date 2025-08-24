n=int(input())
x=[input().split() for i in range(n)]
y=[]
a={}
for i in x:
    if i[0] not in y:
        y.append(i[0])
b=[[i[1] for i in x if j==i[0]]for j in y]
for i in range(len(b)):
    a.setdefault(y[i],b[i])
print('[1] 대출기록:','\n',a,'\n')
c=set()
for i in x:
    if i[1] not in c:
        c.add(i[1])
print('[2] 전체 대출된 책 목록 (중복 제거):','\n',c,'\n')
d=[len(value) for key,value in a.items()]
e=max(d)
l=[]
for key,value in a.items():
    if len(value)==e:
        l.append(key)
print('[3] 가장 많이 대출한 사람:','\n',[l],'\n')
f=[]
for key,value in a.items():
    if len(value)>=3:
        f.append(key)
print('[4] 3권 이상 대출한 사람:','\n',f,'\n')
g=[]
for i in x:
    if i[1] not in g:
        g.append(i[1])
h=[[j[1] for j in x if i==j[1]]for i in g]
k=[]
for i in h:
    k.append(len(i))
for i in h:
    if len(i)==max(k):
        print('[5] 가장 많이 대출된 책:','\n',i[0])