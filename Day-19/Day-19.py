#print numbers from 1 to 10 in forward and reverse order
def display(n):
    if n>10:
        print()
        return
    print(n,end='')
    display(n+1)
    print(n,end='')
display(1)
print('\n')

#print a string in forward and reverse order
def display(i):
    if i==len(s):
        print()
        return
    print(s[i],end='')
    display(i+1)
    print(s[i],end='')
s='Python Programming'
display(0)
print('\n')

#print substrings of a string starting from the first character
def display(n):
    if n==len(s):
        return
    print(s[:n+1])
    display(n+1)
s='Python Programming'
display(0)
print()

#print consecutive substrings of length 4 from a given string
def display(n,w):
    if n>len(s)-w:
        return
    print(s[n:n+w])
    display(n+1,w)
s='Python Programming'
display(0,4)
print()

#sum of numbers from 1 to 10
def display(n):
    if n<1:
        return 0
    return n+display(n-1)
print(display(10))
print()
#or
#sum of list elements
def display(n):
    if n==len(l):
        return 0
    return l[n]+display(n+1)
l=[1,2,3,4,5,6,7,8,9,10]
print(display(0))
print()

#factorial
def display(n):
    if n<1:
        return 1
    return n*display(n-1)
print(display(10))