x={}
a=input('입력 1: ').split(',')
b=input('입력 2: ').split(',')
c=input('입력 3: ').split(',')
e=[a,b,c]
for i in e:
    x.setdefault(i[0],i[1])
y=input('검색할 이름: ')
for key,value in x.items():
    if key==y:
        print(value)
if y not in x:
    print('등록되지 않은 이름입니다')