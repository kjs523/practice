n=int(input())
for i in range(n):
    for j in reversed(range(n)):
        if i>=j:
            print('*',end='')
        else:
            print(' ',end='')
    for j in range(n):
        if i>j:
            print('*',end='')
        else:
            print(' ',end='')
    print()
for i in range(n-1):
    for j in range(n):
        if i<j:
            print('*',end='')
        else:
            print(' ',end='')
    for j in reversed(range(n-1)):
        if i>=j:
            print('',end='')
        else:
            print('*',end='')
    print()