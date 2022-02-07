n = int(input())
for i in range(0,n):
    for j in range(0,n-i-1):
        print(" ",end='')
    for k in range(0,2*i+1):
        print("*",end='')
    print()
for i in range(n-1,0,-1):
    for j in range(n,i,-1):
        print(" ",end='')
    for k in range(2*i-1,0,-1):
        print("*",end='')
    print()
