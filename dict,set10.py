n=int(input())
x=[input().split() for i in range(n)]
y=sorted(x)
a=[]
for i in y:
    if i[0] not in a:
        a.append(i[0])
b=[[i[1] for i in y if j==i[0]]for j in a]
for i in range(len(b)):
    for j in b[i]:
        if b[i].count(j)>1:
            b[i].remove(j)
c={}
for i in range(len(a)):
    c.setdefault(a[i],b[i])
print('[1] 회원별 도서 대출 목록:')
for key,value in c.items():
    print(key,':',value)
print()
d=[len(value) for key,value in c.items()]
e=max(d)
l=[]
for key,value in c.items():
    if len(value)==e:
        l.append(key)
print('[2] 최다 대출 회원:','\n',l[0],'(',e,'권',')','\n')
f=[]
for i in range(len(b)):
    for j in b[i]:
        f.append(j)
g=[]
for i in f:
    if f.count(i)>1:
        g.append(i)
h=[]
for i in g:
    if i not in h:
        h.append(i)
print('[3] 2명 이상이 빌린 책 목록:','\n',h,'\n')
k=[]
for key,value in c.items():
    if len(value)==1:
        k.append(key)
if len(k)>=1:
    print('[4] 한 권만 빌린 회원:','\n',k,'\n')
if len(k)==0:
    print('[4] 한 권만 빌린 회원:','\n','없음','\n')
m=[]
for i in x:
    if i[1] not in m:
        m.append(i[1])
print('[5] 전체 통계:','\n','총 회원 수: ',len(c),'명','\n','총 책 수: ',len(m),'권')