n=int(input())
x=[list(map(int,input().split())) for i in range(n)]
for i in range(n):
    for j in reversed(range(n)):
        print(x[j][i],end=' ')
    print()