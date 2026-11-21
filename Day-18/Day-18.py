#mutable and immutable data types when passed to a function
def display(n):
    n+=10
    print('Inside Function:',n)
n=10
display(n)
print('Outside Function:',n)

def display(f):
    f+=10.3
    print('Inside Function:',f)
f=10.3
display(f)
print('Outside Function:',f)

def display(s):
    s+='Programming'
    print('Inside Function:',s)
s='Python'
display(s)
print('Outside Function:',s)

def display(l):
    l.append(5)
    print('Inside Function:',l)
l=[1,2,3,4]
display(l)
print('Outside Function:',l)

def display(t):
    t+=(5,6,7,8)
    print('Inside Function:',t)
t=(1,2,3,4)
display(t)
print('Outside Function:',t)

def display(s1):
    s1.update({5,6,7,8})
    print('Inside Function:',s1)
s1={1,2,3,4}
display(s1)
print('Outside Function:',s1)

def display(d):
    d[5]=5
    print('Inside Function:',d)
d={1:1,2:2,3:3,4:4}
display(d)
print('Outside Function:',d)

def display(b):
    b=True
    print('Inside Function:',b)
b=False
display(b)
print('Outside Function:',b)
print()

#local variable scope(output:nameerror)
def display():
    n1=10
    print('Inside:',n1)
display()
print('Outside:',n1)
print()

#accessing a global variable
def display():
    print('Inside:',n)
n=10
display()
print('Outside:',n)
print()

#modifying a global variable
def display():
    global n
    n=10
    print('Inside:',n)
display()
print('Outside:',n)
print()

#local scope in a nested function
def display():
    course='JFS'
    print('Starting:',course)
    def update():
        course='PFS'
        print('Updated:',course)
    update()
    print('Final',course)
display()
print()

#nonlocal keyword
def display():
    course='JFS'
    print('Starting:',course)
    def update():
        nonlocal course
        course='PFS'
        print('Updated:',course)
    update()
    print('Final',course)
display()
print()

#length of a string
s='python'
print(len(s))
print()

#overwriting a built-in function(output:typeerror)
s='python'
len=10
print(len(s))