n=int(input())
for i in range((n-1)//2+1):
    for j in reversed(range((n-1)//2+1)):
        if i==j:
            print('*',end='')
        else:
            print(' ',end='')
    for j in range((n-1)//2+1):
        if j==0:
            print('',end='')
        elif j==i:
            print('*',end='')
        else:
            print(' ',end='')
    print()
for i in range(1,(n-1)//2+1):
    for j in range((n-1)//2+1):
        if i==j:
            print('*',end='')
        else:
            print(' ',end='')
    for j in reversed(range((n-1)//2)):
        if i==j:
            print('*',end='')
        else:
            print(' ',end='')
    print()
