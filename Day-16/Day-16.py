#increasing right-aligned triangle star pattern
n=int(input('Enter the size:'))
for row in range(n):
    for spa in range(n-1-row):
        print(' ',end=' ')
    for col in range(row+1):
        print('*',end=' ')
    print()
print()

#decreasing left-aligned triangle star pattern
n=int(input('Enter the size:'))
for row in range(n):
    for spa in range(row):
        print(' ',end=' ')
    for col in range(n-row):
        print('*',end=' ')
    print()
print()

#increasing and decreasing star pattern
n=int(input('Enter the size:'))
m=n//2
for row in range(n):
    if row<=m:
        for col in range(row+1):
            print('*',end=' ')
    else:
        for col in range(n-row):
            print('*',end=' ')
    print()
print()
#or
n=int(input('Enter the size:'))
m=n//2
for row in range(n):
    if row<=m:
        print('* '*(row+1))
    else:
        print('* '*(n-row))
print()
#or
n=int(input('Enter the size:'))
m=n//2
for row in range(n):
    print('* '*(row+1) if row<=m else '* '*(n-row))
print()

#hollow square star pattern
n=int(input('Enter the size:'))
for row in range(n):
    for col in range(n):
        if row==0 or col==0 or row==n-1 or col==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
print()

#square star pattern with middle lines
n=int(input('Enter the size:'))
m=n//2
for row in range(n):
    for col in range(n):
        if row==0 or col==0 or row==n-1 or col==n-1 or row==m or col==m:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
print()

#square star pattern with diagonals
n=int(input('Enter the size:'))
for row in range(n):
    for col in range(n):
        if row==0 or col==0 or row==n-1 or col==n-1 or row==col or row+col==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
print()

#square star pattern with middle lines and diagonals
n=int(input('Enter the size:'))
m=n//2
for row in range(n):
    for col in range(n):
        if row==0 or col==0 or row==n-1 or col==n-1 or row==m or col==m or row==col or row+col==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()