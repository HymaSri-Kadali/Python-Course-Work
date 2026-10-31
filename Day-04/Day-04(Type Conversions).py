Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> i=24
>>> int(i)
24
>>> float(i)
24.0
>>> complex(i)
(24+0j)
>>> str(i)
'24'
>>> list(i)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    list(i)
TypeError: 'int' object is not iterable
>>> tuple(i)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    tuple(i)
TypeError: 'int' object is not iterable
>>> set(i)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    set(i)
TypeError: 'int' object is not iterable
>>> dict(i)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    dict(i)
TypeError: 'int' object is not iterable
>>> bool(i)
True
>>> bool(0)
False
>>> f=12.34
>>> int(f)
12
>>> float(f)
12.34
>>> complex(f)
(12.34+0j)
>>> str(f)
'12.34'
>>> list(f)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    list(f)
TypeError: 'float' object is not iterable
>>> tuple(f)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    tuple(f)
TypeError: 'float' object is not iterable
>>> set(f)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    set(f)
TypeError: 'float' object is not iterable
>>> dict(f)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    dict(f)
TypeError: 'float' object is not iterable
>>> bool(f)
True
>>> bool(0.0)
False
>>> c=10+11j
>>> int(c)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    int(c)
TypeError: can't convert complex to int
>>> float(c)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    float(c)
TypeError: can't convert complex to float
>>> complex(c)
(10+11j)
>>> str(c)
'(10+11j)'
>>> list(c)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
>>> tuple(c)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    tuple(c)
TypeError: 'complex' object is not iterable
>>> set(c)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    set(c)
TypeError: 'complex' object is not iterable
>>> dict(c)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    dict(c)
TypeError: 'complex' object is not iterable
>>> bool(c)
True
>>> bool(0+0j)
False
>>> s='codegnan'
>>> int(s)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: 'codegnan'
>>> float(s)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    float(s)
ValueError: could not convert string to float: 'codegnan'
>>> complex(s)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    complex(s)
ValueError: complex() arg is a malformed string
>>> str(s)
'codegnan'
>>> list(s)
['c', 'o', 'd', 'e', 'g', 'n', 'a', 'n']
>>> tuple(s)
('c', 'o', 'd', 'e', 'g', 'n', 'a', 'n')
>>> set(s)
{'e', 'o', 'a', 'g', 'n', 'c', 'd'}
>>> dict(s)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    dict(s)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> bool(s)
True
>>> bool('')
False
>>> s1='1234'
>>> int(s1)
1234
>>> float(s1)
1234.0
>>> str(s1)
'1234'
>>> complex(s1)
(1234+0j)
>>> list(s1)
['1', '2', '3', '4']
>>> tuple(s1)
('1', '2', '3', '4')
>>> set(s1)
{'2', '4', '1', '3'}
>>> dict(s1)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    dict(s1)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> bool(s1)
True
>>> bool('0')
True
>>> l=[1,2,3,4]
>>> int(l)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
>>> float(l)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a number, not 'list'
>>> complex(l)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    complex(l)
TypeError: complex() first argument must be a string or a number, not 'list'
>>> str(l)
'[1, 2, 3, 4]'
>>> list(l)
[1, 2, 3, 4]
>>> tuple(l)
(1, 2, 3, 4)
>>> set(l)
{1, 2, 3, 4}
>>> dict(l)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    dict(l)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> bool(l)
True
>>> bool([])
False
>>> t=(1,2,3,4)
>>> int(t)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    int(t)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'tuple'
>>> float(t)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    float(t)
TypeError: float() argument must be a string or a number, not 'tuple'
>>> complex(t)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    complex(t)
TypeError: complex() first argument must be a string or a number, not 'tuple'
>>> str(t)
'(1, 2, 3, 4)'
>>> list(t)
[1, 2, 3, 4]
>>> tuple(t)
(1, 2, 3, 4)
>>> set(t)
{1, 2, 3, 4}
>>> dict(t)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    dict(t)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> bool(t)
True
>>> bool(())
False
>>> s2={1,2,3,4}
>>> int(s2)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    int(s2)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'set'
>>> float(s2)
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    float(s2)
TypeError: float() argument must be a string or a number, not 'set'
>>> complex(s2)
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    complex(s2)
TypeError: complex() first argument must be a string or a number, not 'set'
>>> str(s2)
'{1, 2, 3, 4}'
>>> list(s2)
[1, 2, 3, 4]
>>> tuple(s2)
(1, 2, 3, 4)
>>> set(s2)
{1, 2, 3, 4}
>>> dict(s2)
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    dict(s2)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> bool(s2)
True
>>> bool(set())
False
>>> d={1:5,2:6,3:7,4:8}
>>> int(d)
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    int(d)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'dict'
>>> float(d)
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    float(d)
TypeError: float() argument must be a string or a number, not 'dict'
>>> complex(d)
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    complex(d)
TypeError: complex() first argument must be a string or a number, not 'dict'
>>> str(d)
'{1: 5, 2: 6, 3: 7, 4: 8}'
>>> list(d)
[1, 2, 3, 4]
>>> tuple(d)
(1, 2, 3, 4)
>>> set(d)
{1, 2, 3, 4}
>>> dict(d)
{1: 5, 2: 6, 3: 7, 4: 8}
>>> bool(d)
True
>>> bool({})
False
>>> b=True
>>> int(b)
1
>>> float(b)
1.0
>>> complex(b)
(1+0j)
>>> str(b)
'True'
>>> list(b)
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    list(b)
TypeError: 'bool' object is not iterable
>>> tuple(b)
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    tuple(b)
TypeError: 'bool' object is not iterable
>>> set(b)
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    set(b)
TypeError: 'bool' object is not iterable
>>> dict(b)
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    dict(b)
TypeError: 'bool' object is not iterable
>>> bool(b)
True
>>> bool()
False
>>> 
