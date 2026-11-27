#return and display a tuple of reel ranges using a normal function
def reels():
    res=('1-100','101-200','201-300','301-400','400-500')
    return res
feed=reels()
print(feed)
print()

#generate and display tuple elements one by one using yield and next()
def reels():
    res=('1-100','101-200','201-300','301-400','400-500')
    yield res[0]
    yield res[1]
    yield res[2]
    yield res[3]
    yield res[4]
feed=reels()
print(next(feed))
print(next(feed))
print(next(feed))
print(next(feed))
print(next(feed))
print()
#or(using for loop and yield)
def reels():
    res=('1-100','101-200','201-300','301-400','400-500')
    for i in res:
        yield i
feed=reels()
print(next(feed))
print(next(feed))
print(next(feed))
print(next(feed))
print(next(feed))
print()
#or(display all generated reel ranges using a for loop)
def reels():
    res=('1-100','101-200','201-300','301-400','400-500')
    for i in res:
        yield i
feed=reels()
for i in feed:
    print(i)
print()

#find and display all factors of a given number using a generator
def factors(n):
    for i in range(1,n+1):
        if n%i==0:
            yield i
fact=factors(12)
for i in fact:
    print(i,end=' ')
print('\n')

#generate and display prime numbers up to 50 using a generator
def prime(n):
    for i in range(2,n+1):
        for j in range(2,i//2+1):
            if i%j==0:
                break
        else:
            yield i
display=prime(50)
for i in display:
    print(i,end=' ')
print('\n')

#generate and display the first 10 fibonacci numbers using a for loop
n,a,b=10,0,1
print(a,b,end=' ')
for i in range(n-2):
    c=a+b
    print(c, end=' ')
    a=b
    b=c
print()
#or(generate and display the first 10 Fibonacci numbers using yield)
def fib(n):
    if n==1:
        yield 0
    elif n>=2:
        a,b=0,1
        yield a
        yield b
        for _ in range(n-2):
            c=a+b
            a=b
            b=c
            yield c
display=fib(10)
for i in display:
    print(i,end=' ')
print('\n') 

#list comprehension
#create a list of numbers
n=int(input('Enter a number:'))
res=[i for i in range(1,n+1)]
print(res)
print()

#find all factors
n=int(input('Enter a number:'))
fact=[i for i in range(1,n+1) if n%i==0]
print(fact)
print()

#filter and display names starting with the letter 's'
names=['swathi','dhanasri','sowmya','sreeja']
resn=[i for i in names if i.startswith('s')]
print(resn)
print()

#display even numbers and replace odd numbers with 0
l=[1,34,445,941,56,89,34,76,349]
rese=[i if i%2==0 else 0 for i in l]
print(rese)
print()

#create a nested list containing five lists, each with numbers from 1 to 3
nes=[[j for j in range(1,4)] for i in range(5)]
print(nes)
print()

#set comprehension
#create a set of numbers from 1 to 10
n=int(input('Enter a number:'))
res={i for i in range(1,n+1)}
print(res)
print()

#find all factors
n=int(input('Enter a number:'))
fact={i for i in range(1,n+1) if n%i==0}
print(fact)
print()   

#dict comprehension
#create a dictionary with numbers from 1 to n as keys and their values increased by 10
n=int(input('Enter a number:'))
res={i:i+10 for i in range(1,n+1)}
print(res)