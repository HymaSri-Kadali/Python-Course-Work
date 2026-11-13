#print column numbers in 3 rows
for row in range(3):
    for col in range(5):
        print(col,end=' ')
    print()
print()

#square star pattern
for row in range(5):
    for col in range(5):
        print('*',end=' ')
    print()
print()

#print an alternate 0 and 1 pattern
for row in range(5):
    for col in range(5):
        if (row+col)%2==0:
            print(1,end=' ')
        else:
            print(0,end=' ')
    print()
print()
#or
for row in range(5):
    for col in range(5):
        print(int((row+col)%2==0),end=' ')
    print()
print()

#print alternate 0s and 1s in columns
for row in range(5):
    for col in range(5):
        print(col%2,end=' ')
    print()
print()

#numbers from 1 to 25 in a square pattern
i=1
for row in range(5):
    for col in range(5):
        print(i,end=' ')
        i+=1
    print()
print()

#product of row and column numbers
for row in range(5):
    for col in range(5):
        print((row*col),end=' ')
    print()
print()

#increasing triangle star pattern
for row in range(5):
    for col in range(row+1):
        print('*',end=' ')
    print()
print()
#or
n=int(input('Enter the size:'))
for row in range(n):
    for col in range(row+1):
        print('*',end=' ')
    print()
print()

#decreasing triangle star pattern
for row in range(5):
    for col in range(5-row):
        print('*',end=' ')
    print()
print()
#or
n=int(input('Enter the size:'))
for row in range(n):
    for col in range(n-row):
        print('*',end=' ')
    print()