Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=input()
232
>>> a
'232'
>>> type(a)
<class 'str'>
>>> a=input("Enter the string:")
Enter the string:python
>>> a
'python'
>>> a=int(input())
8343
>>> a
8343
>>> a=int(input("Enter the integer:"))
Enter the integer:3232
>>> a
3232
>>> a=float(input("Enter the float:"))
Enter the float:12.34
>>> a
12.34
>>> a=float(input("Enter the float:"))
Enter the float:12
>>> a
12.0
>>> a=list(input())
123456789
>>> a
['1', '2', '3', '4', '5', '6', '7', '8', '9']
>>> a=list(input())
0 12 345 6789
>>> a
['0', ' ', '1', '2', ' ', '3', '4', '5', ' ', '6', '7', '8', '9']
>>> '0 12 345 6789'.split(' ')
['0', '12', '345', '6789']
>>> '0,12,345,6789'.split(',')
['0', '12', '345', '6789']
>>> 'a bc def ghij'.split()
['a', 'bc', 'def', 'ghij']
>>> a=input().split()
0 12 345 6789
>>> a
['0', '12', '345', '6789']
>>> int([1,2,3])
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    int([1,2,3])
TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
>>> map(int,a)
<map object at 0x00000195753F13C8>
>>> list(map(int,a))
[0, 12, 345, 6789]
>>> a=list(map(int,input().split()))
0 12 345 6789
>>> a
[0, 12, 345, 6789]
>>> a=list(map(float,input().split()))
1.2 3.45 67.89
>>> a
[1.2, 3.45, 67.89]
>>> a=tuple(input().split())
0 12 345 6789
>>> a
('0', '12', '345', '6789')
>>> a=tuple(map(int,input().split()))
0 12 345 6789
>>> a
(0, 12, 345, 6789)
>>> a=tuple(map(float,input().split()))
1.2 3.45 67.89
>>> a
(1.2, 3.45, 67.89)
>>> a=set(input().split())
0 12 345 6789
>>> a
{'6789', '12', '0', '345'}
>>> a=set(map(int,input().split()))
0 12 345 6789
>>> a
{0, 345, 12, 6789}
>>> a=set(map(float, input().split()))
1.2 3.45 67.89
>>> a
{1.2, 67.89, 3.45}
>>> a,b,c=(1,2,3)
>>> a
1
>>> b
2
>>> c
3
>>> a,b,c=[1,2,3]
>>> a
1
>>> b
2
>>> c
3
>>> a,b,c=list(map(int,input().split()))
1 2 3
>>> a
1
>>> b
2
>>> c
3
>>> email, password=input().split()
hyma@gmail.com 12345
>>> email
'hyma@gmail.com'
>>> password
'12345'
>>> a,b,c=list(map(float, input().split()))
12.3 343.5 4.3
>>> a
12.3
>>> b
343.5
>>> c
4.3
>>> a=eval(input())
24
>>> a
24
>>> a=eval(input())
2323.4545
>>> a
2323.4545
>>> a=eval(input())
2+3j
>>> a
(2+3j)
>>> a=eval(input())
'sdsd'
>>> a
'sdsd'
>>> a=eval(input())
'1234'
>>> a
'1234'
>>> a=eval(input())
[1,2,3]
>>> a
[1, 2, 3]
>>> a=eval(input())
(1,2,3)
>>> a
(1, 2, 3)
>>> a=eval(input())
{12332,3434,5454,523451}
>>> a
{3434, 523451, 12332, 5454}
>>> a=eval(input())
{1:5,2:6,3:7,4:8}
>>> a
{1: 5, 2: 6, 3: 7, 4: 8}
>>> a=eval(input())
True
>>> a
True
>>> a=eval(input())
None
>>> a
>>> a=10
>>> b=5.2
>>> c='codegnan'
>>> print(a,b,c)
10 5.2 codegnan
>>> print('a=',a,'b=',b,'c=',c)
a= 10 b= 5.2 c= codegnan
>>> print('a=',a,'b=',b,'c=',c,sep=' ')
a= 10 b= 5.2 c= codegnan
>>> print('a=',a,'b=',b,'c=',c,sep='')
a=10b=5.2c=codegnan
>>> print('a=',a,'b=',b,'c=',c,sep='-')
a=-10-b=-5.2-c=-codegnan
>>> print('a=',a,'b=',b,'c=',c,end='\n\n')
a= 10 b= 5.2 c= codegnan

>>> print('a=',a,'b=',b,'c=',c,end='@')
a= 10 b= 5.2 c= codegnan@
>>> print('a=',a,'b=',b,'c=',c,end='\n\n\n')
a= 10 b= 5.2 c= codegnan


>>> print(f'a={a} b={b} c={c}')
a=10 b=5.2 c=codegnan
>>> print('a=%d b=%f c=%s'%(a,b,c))
a=10 b=5.200000 c=codegnan
>>> print('a=%d b=%.2f c=%s'%(a,b,c))
a=10 b=5.20 c=codegnan
>>> print('a={} b={} c={}'.format(a,b,c))
a=10 b=5.2 c=codegnan
>>> print('a={} b={} c={}'.format(b,c,a))
a=5.2 b=codegnan c=10
>>> 
