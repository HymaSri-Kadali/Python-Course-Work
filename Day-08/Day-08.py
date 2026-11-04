Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> t=()
>>> t=tuple()
>>> t=(1,2,3)
>>> t=tuple((1,2,3,4))
>>> t
(1, 2, 3, 4)
>>> type(t)
<class 'tuple'>
>>> t=1,2,3,4,5
>>> t
(1, 2, 3, 4, 5)
>>> t=(1)
>>> t
1
>>> t=(1,)
>>> t
(1,)
>>> t=(1,2,3,1,3,5,2)
>>> t
(1, 2, 3, 1, 3, 5, 2)
>>> t=(1,1.1,'dds',[1,2,3],(1,2,3),{1,2,3},{1:3,2:4},False)
>>> t
(1, 1.1, 'dds', [1, 2, 3], (1, 2, 3), {1, 2, 3}, {1: 3, 2: 4}, False)
>>> t=(1,2,3)
>>> t
(1, 2, 3)
>>> a,b,c=t
>>> a
1
>>> b
2
>>> c
3
>>> a,b,c=(1,2,3,3)
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    a,b,c=(1,2,3,3)
ValueError: too many values to unpack (expected 3)
>>> a,b,c=(1,2,3)
>>> a
1
>>> b
2
>>> c
3
>>> t=(1,1.1,'dds',[1,2,3],(1,2,3),{1,2,3},{1:3,2:4},False)
>>> t
(1, 1.1, 'dds', [1, 2, 3], (1, 2, 3), {1, 2, 3}, {1: 3, 2: 4}, False)
>>> t[0]=2
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    t[0]=2
TypeError: 'tuple' object does not support item assignment
>>> t.append(1)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    t.append(1)
AttributeError: 'tuple' object has no attribute 'append'
>>> t.add(1)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    t.add(1)
AttributeError: 'tuple' object has no attribute 'add'
>>> t[3]
[1, 2, 3]
>>> t[3].append(4)
>>> t
(1, 1.1, 'dds', [1, 2, 3, 4], (1, 2, 3), {1, 2, 3}, {1: 3, 2: 4}, False)
>>> a=(1,2,3,4)
>>> b=(5,6,7,8,9)
>>> a+b
(1, 2, 3, 4, 5, 6, 7, 8, 9)
>>> a*2
(1, 2, 3, 4, 1, 2, 3, 4)
>>> t
(1, 1.1, 'dds', [1, 2, 3, 4], (1, 2, 3), {1, 2, 3}, {1: 3, 2: 4}, False)
>>> t[2]
'dds'
>>> t[-1]
False
>>> t[::-1]
(False, {1: 3, 2: 4}, {1, 2, 3}, (1, 2, 3), [1, 2, 3, 4], 'dds', 1.1, 1)
>>> t[2::]
('dds', [1, 2, 3, 4], (1, 2, 3), {1, 2, 3}, {1: 3, 2: 4}, False)
>>> t[3:6]
([1, 2, 3, 4], (1, 2, 3), {1, 2, 3})
>>> t[-2:]
({1: 3, 2: 4}, False)
>>> False in t
True
>>> [1,2,3] in t
False
>>> False not in t
False
>>> [1,2,3] not in t
True
>>> t=(29,33,67,43,89,99,67,83)
>>> t
(29, 33, 67, 43, 89, 99, 67, 83)
>>> len(t)
8
>>> sorted(t)
[29, 33, 43, 67, 67, 83, 89, 99]
>>> max(t)
99
>>> min(t)
29
>>> t.count(67)
2
>>> t.index(83)
7
>>> any(t)
True
>>> all(t)
True
>>> t=(29,33,67,43,89,99,67,83,0)
>>> any(t)
True
>>> all(t)
False
>>> sum(t)
510
>>> s=set()
>>> s
set()
>>> type(s)
<class 'set'>
>>> s={1,2,3,4}
>>> s
{1, 2, 3, 4}
>>> s={90,6,45,13,67,8,1,4}
>>> s
{1, 67, 4, 6, 8, 13, 45, 90}
>>> s={1,1,1,1}
>>> s
{1}
>>> s=set()
>>> s.add(1)
>>> s.add(1.2)
>>> s.add(10+11j)
>>> s
{1, (10+11j), 1.2}
>>> s.add('str')
>>> s
{1, (10+11j), 'str', 1.2}
>>> s.add((1,2,3))
>>> s
{1, 1.2, (10+11j), (1, 2, 3), 'str'}
>>> s.add(False)
>>> s
{False, 1, 1.2, (10+11j), (1, 2, 3), 'str'}
>>> s.add([1,2,3])
Traceback (most recent call last):
  File "<pyshell#143>", line 1, in <module>
    s.add([1,2,3])
TypeError: unhashable type: 'list'
>>> s.add({1,2,3})
Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    s.add({1,2,3})
TypeError: unhashable type: 'set'
>>> s.add({1:1,2:2})
Traceback (most recent call last):
  File "<pyshell#145>", line 1, in <module>
    s.add({1:1,2:2})
TypeError: unhashable type: 'dict'
>>> s
{False, 1, 1.2, (10+11j), (1, 2, 3), 'str'}
>>> a={8,1,4,6}
>>> b={4,5,6,7,8,9}
>>> a+b
Traceback (most recent call last):
  File "<pyshell#149>", line 1, in <module>
    a+b
TypeError: unsupported operand type(s) for +: 'set' and 'set'
>>> a*2
Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    a*2
TypeError: unsupported operand type(s) for *: 'set' and 'int'
>>> a[2]
Traceback (most recent call last):
  File "<pyshell#151>", line 1, in <module>
    a[2]
TypeError: 'set' object does not support indexing
>>> a[:3]
Traceback (most recent call last):
  File "<pyshell#152>", line 1, in <module>
    a[:3]
TypeError: 'set' object is not subscriptable
>>> 4 in a
True
>>> 9 in a
False
>>> 4 not in a
False
>>> 9 not in a
True
>>> a|b
{1, 4, 5, 6, 7, 8, 9}
>>> a&b
{8, 4, 6}
>>> a^b
{1, 5, 7, 9}
>>> a-b
{1}
>>> b-a
{9, 5, 7}
>>> a.isdisjoint(b)
False
>>> a.isdisjoint({2,3,5,7})
True
>>> a
{8, 1, 4, 6}
>>> {8}.issubset(a)
True
>>> {8,1,4,6}.issubset(a)
True
>>> {100,99}.issubset(a)
False
>>> a.issubset(b)
False
>>> b.issubset(a)
False
>>> {1,2,3,4,5,6,7,8,9,10}.issuperset(a)
True
>>> s={12,34,8,40,13,29,50,56,90}
>>> s
{34, 8, 40, 12, 13, 50, 56, 90, 29}
>>> sorted(s)
[8, 12, 13, 29, 34, 40, 50, 56, 90]
>>> len(s)
9
>>> max(s)
90
>>> min(s)
8
>>> sum(s)
332
>>> any(s)
True
>>> all(s)
True
>>> s={12,34,8,40,13,29,50,56,90,0}
>>> any(s)
True
>>> all(s)
False
>>> s={12,34,8,40,13,29,50,56,90}
>>> s.add(1)
>>> s
{1, 34, 8, 40, 12, 13, 50, 56, 90, 29}
>>> s.add(100)
>>> s
{1, 34, 100, 8, 40, 12, 13, 50, 56, 90, 29}
>>> s.update({10,20,30})
>>> s
{1, 34, 100, 8, 40, 10, 12, 13, 50, 20, 56, 90, 29, 30}
>>> s.pop()
1
>>> s.pop()
34
>>> s.pop()
100
>>> s
{8, 40, 10, 12, 13, 50, 20, 56, 90, 29, 30}
>>> s.remove(10)
>>> s.remove(40)
>>> s
{8, 12, 13, 50, 20, 56, 90, 29, 30}
>>> s.remove(40)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    s.remove(40)
KeyError: 40
>>> s.discard(50)
>>> s
{8, 12, 13, 20, 56, 90, 29, 30}
>>> s.discard(50)
>>> s
{8, 12, 13, 20, 56, 90, 29, 30}
>>> s.clear()
>>> s
set()
>>> a={1,2,3,4,5}
>>> a
{1, 2, 3, 4, 5}
>>> b=a
>>> b.add(6)
>>> b
{1, 2, 3, 4, 5, 6}
>>> a
{1, 2, 3, 4, 5, 6}
>>> c=a.copy()
>>> c.add(20)
>>> c
{1, 2, 3, 4, 5, 6, 20}
>>> a
{1, 2, 3, 4, 5, 6}
>>> s=frozenset({1,2,3,4})
>>> s
frozenset({1, 2, 3, 4})
>>> type(s)
<class 'frozenset'>
>>> len(s)
4
>>> max(s)
4
>>> min(s)
1
>>> 
