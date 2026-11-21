#print numbers from 1 to 10
def nums():
    for i in range(1,11):
        print(i)
nums()
print()

#number is prime or composite
def factors(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c>2:
        print('Composite Number')
    else:
        print('Prime Number')
factors(int(input('Enter a number:')))
#or (using return)
def factors(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return 'Composite Number'
    return 'Prime Number'
print(factors(int(input('Enter a number:'))))
print()

#sum of digits of a number
def sum_num(n):
    s=0
    while n>0:
        s+=n%10
        n//=10
    return s
print(sum_num(12345))
print()

#reverse a number
def rev_num(n):
    s=0
    while n>0:
        s=(s*10)+n%10
        n//=10
    return s
print(rev_num(12345))
print()

#positional arguments
def display(n,e,p):
    print('Name:',n)
    print('Email:',e)
    print('Password:',p)
display('abc','abc@gmail.com','abc@123')
display('abc@gmail.com','abc@123','abc')
display('abc@123','abc','abc@gmail.com')
print()

#keyword arguments
def display(n,e,p):
    print('Name:',n)
    print('Email:',e)
    print('Password:',p)
display(n='abc',e='abc@gmail.com',p='abc@123')
display(e='abc@gmail.com',p='abc@123',n='abc')
display(p='abc@123',n='abc',e='abc@gmail.com')
print()

#default arguments
def display(n,e,p,phno=None):
    print('Name:',n)
    print('Email:',e)
    print('Password:',p)
    print('Phone Number:',phno)
display('abc','abc@gmail.com','abc@123')
display('abc','abc@gmail.com','abc@123',9876543210)
print()

#multiple values using *args(variable length argument)
def display(*n):
    print(n)
display(1,2,3,4,5)
display(1,2,3)
display(1,2,3,4,5,6,7)
print()

#multiple keyword values using **kwargs(keyword length argument)
def display(**n):
    print(n)
display(n1=1,n2=2,n3=3,n4=4,n5=5)
display(n1=1,n2=2,n3=3)
display(n1=1,n2=2,n3=3,n4=4,n5=5,n6=6,n7=7)
print()

#find the highest and lowest marks
def hm(data):
    max=0
    res=''
    for i in data:
        if data[i]>max:
            max=data[i]
            res=i
    print(f'Highest marks, {res}:{max}')
def lm(data):
    min=999#float('inf')
    res=''
    for i in data:
        if data[i]<min:
            min=data[i]
            res=i
    print(f'Lowest marks, {res}:{min}')
data={}
for i in range(3):
    n=input('Enter the name:')
    m=int(input('Enter the marks:'))
    data[n]=m
hm(data)
lm(data)