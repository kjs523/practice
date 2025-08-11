n=int(input())
x=[input() for i in range(n)]
for i in x:
    if i==''.join(reversed(i)):
        print(i,end=' ')
    else:
        print('',end='')