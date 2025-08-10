n=int(input())
for i in range(n):
    for j in range(n):
        if i>j:
            print(' ',end='')
        else:
            print('*',end='')
    for j in reversed(range(n)):
        if i>=j:
            print(' ',end='')
        else:
            print('*',end='')
    print()