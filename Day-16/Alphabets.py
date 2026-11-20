#A
n=int(input('Enter the size:'))
m=n//2
for row in range(n):
    for col in range(n):
        if  row==0 or col==0 or col==n-1 or row==m:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
#B
n=int(input('Enter the size:'))
m=n//2
for row in range(n):
    for col in range(n):
        if row==0 or col==0 or row==n-1 or col==n-1 or row==m:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
#C
n=int(input('Enter the size:'))
for row in range(n):
    for col in range(n):
        if row==0 or col==0 or row==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
#D
n=int(input('Enter the size:'))
for row in range(n):
    for col in range(n):
        if ((row==0 or row==n-1) and (col not in (0,n-1))) or col==0 or ((col==n-1) and (row not in (0,n-1))):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
#E
n=int(input('Enter the size:'))
m=n//2
for row in range(n):
    for col in range(n):
        if row==0 or col==0 or row==n-1 or row==m:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
#F
n=int(input('Enter the size:'))
m=n//2
for row in range(n):
    for col in range(n):
        if row==0 or col==0 or row==m:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
#G
n=int(input('Enter the size:'))
m=n//2
for row in range(n):
    for col in range(n):
        if row==0 or col==0 or row==n-1 or (col==n-1 and row>=m) or (row==m and col>=m):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
#H
n=int(input('Enter the size:'))
m=n//2
for row in range(n):
    for col in range(n):
        if col==0 or col==n-1 or row==m:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
#I
n=int(input('Enter the size:'))
m=n//2
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or col==m:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
#J
n=int(input('Enter the size:'))
m=n//2
for row in range(n):
    for col in range(n):
        if row==0 or col==m or (row==n-1 and col<=m) or (col==0 and row>=m):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
#K
n=int(input('Enter the size:'))
m=n//2
for row in range(n):
    for col in range(n):
        if col==0 or (row<=m and row+col==m) or (row>m and row-col==m):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
#L
n=int(input('Enter the size:'))
for row in range(n):
    for col in range(n):
        if row==n-1 or col==0:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
#M
n=int(input('Enter the size:'))
m=n//2
for row in range(n):
    for col in range(n):
        if col==0 or col==n-1 or (row==col and row<=m) or (row+col==n-1 and row<=m):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
#N
n=int(input('Enter the size:'))
for row in range(n):
    for col in range(n):
        if col==0 or col==n-1 or row==col:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
#O
n=int(input('Enter the size:'))
for row in range(n):
    for col in range(n):
        if ((row==0 or row==n-1) and (col not in (0,n-1))) or ((col==0 or col==n-1) and (row not in (0,n-1))):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
#P
n=int(input('Enter the size:'))
m=n//2
for row in range(n):
    for col in range(n):
        if row==0 or col==0 or row==m or (col==n-1 and row<=m):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
#Q
n=int(input('Enter the size:'))
m=n//2
for row in range(n):
    for col in range(n):
        if ((row==0 or row==n-1) and (col not in (0,n-1))) or ((col==0 or col==n-1) and (row not in (0,n-1))) or (row==col and row>=m):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
#R
n=int(input('Enter the size:'))
m=n//2
for row in range(n):
    for col in range(n):
        if row==0 or col==0 or row==m or (col==n-1 and row<=m) or (row==col and row>=m):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
#S
n=int(input('Enter the size:'))
m=n//2
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or row==m or (col==0 and row<m) or (col==n-1 and row>m):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
#T
n=int(input('Enter the size:'))
m=n//2
for row in range(n):
    for col in range(n):
        if row==0 or col==m:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
#U
n=int(input('Enter the size:'))
for row in range(n):
    for col in range(n):
        if col==0 or row==n-1 or col==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
#V
n=int(input('Enter the size:'))
for row in range(n):
    for col in range(2*n-1):
        if row==col or col==2*n-2-row:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
#W
n=int(input('Enter the size:'))
m=n//2
for row in range(n):
    for col in range(n):
        if col==0 or col==n-1 or (row==col and row>=m) or (row+col==n-1 and row>=m):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
#X
n=int(input('Enter the size:'))
for row in range(n):
    for col in range(n):
        if row==col or row+col==n-1 :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
#Y
n=int(input('Enter the size:'))
m=n//2
for row in range(n):
    for col in range(n):
        if (row<=m and (row==col or row+col==n-1)) or (row>m and col==m):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
#Z
n=int(input('Enter the size:'))
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or row+col==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()