Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l=[]
>>> l=list()
>>> l=[1,2,3]
>>> l=list([1,2,3,4])
>>> l
[1, 2, 3, 4]
>>> l=[2,3,4,5,5]
>>> l
[2, 3, 4, 5, 5]
>>> l=[1,1,1,1]
>>> l
[1, 1, 1, 1]
>>> l=[1,12.3,3+5j,'str',[1,2],(1,2),{1,2},{1:2},False,None]
>>> l
[1, 12.3, (3+5j), 'str', [1, 2], (1, 2), {1, 2}, {1: 2}, False, None]
>>> [1,2,3]+[4,5,6]
[1, 2, 3, 4, 5, 6]
>>> [1,2,3]*3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> l=['python','java','c','flask','fastapi','mysql','aws']
>>> l
['python', 'java', 'c', 'flask', 'fastapi', 'mysql', 'aws']
>>> l[0]
'python'
>>> l[-1]
'aws'
>>> l[:2]
['python', 'java']
>>> l[-3:]
['fastapi', 'mysql', 'aws']
>>> l[2:5]
['c', 'flask', 'fastapi']
>>> l[1::2]
['java', 'flask', 'mysql']
>>> l[::2]
['python', 'c', 'fastapi', 'aws']
>>> l[::-1]
['aws', 'mysql', 'fastapi', 'flask', 'c', 'java', 'python']
>>> l[-3:-6:-1]
['fastapi', 'flask', 'c']
>>> 'c' in l
True
>>> 'css' in l
False
>>> 'c' not in l
False
>>> 'css' not in l
True
>>> len(l)
7
>>> sorted(l)
['aws', 'c', 'fastapi', 'flask', 'java', 'mysql', 'python']
>>> max(l)
'python'
>>> min(l)
'aws'
>>> l
['python', 'java', 'c', 'flask', 'fastapi', 'mysql', 'aws']
>>> id(l)
2342259525960
>>> l[1]='html'
>>> l
['python', 'html', 'c', 'flask', 'fastapi', 'mysql', 'aws']
>>> id(l)
2342259525960
>>> l.append('a')
>>> l
['python', 'html', 'c', 'flask', 'fastapi', 'mysql', 'aws', 'a']
>>> id(l)
2342259525960
>>> l.extend([1,2])
>>> l
['python', 'html', 'c', 'flask', 'fastapi', 'mysql', 'aws', 'a', 1, 2]
>>> id(l)
2342259525960
>>> l.insert(1,'c++')
>>> l
['python', 'c++', 'html', 'c', 'flask', 'fastapi', 'mysql', 'aws', 'a', 1, 2]
>>> id(l)
2342259525960
>>> l=[29,33,67,43,89,99,67,83]
>>> sum(l)
510
>>> l.pop()
83
>>> l
[29, 33, 67, 43, 89, 99, 67]
>>> l.pop(0)
29
>>> l
[33, 67, 43, 89, 99, 67]
>>> l.pop(2)
43
>>> l
[33, 67, 89, 99, 67]
>>> l.remove(89)
>>> l
[33, 67, 99, 67]
>>> l.remove(67)
>>> l
[33, 99, 67]
>>> del l[2]
>>> l
[33, 99]
>>> l.clear()
>>> l
[]
>>> l=[29,33,67,43,89,99,67,83]
>>> l.count(67)
2
>>> l.index(99)
5
>>> sorted(l)
[29, 33, 43, 67, 67, 83, 89, 99]
>>> l.sort()
>>> l
[29, 33, 43, 67, 67, 83, 89, 99]
>>> l.reverse()
>>> l
[99, 89, 83, 67, 67, 43, 33, 29]
>>> l.sort(reverse=True)
>>> l
[99, 89, 83, 67, 67, 43, 33, 29]
>>> l.sort(reverse=False)
>>> l
[29, 33, 43, 67, 67, 83, 89, 99]
>>> a=[1,2]
>>> c=a
>>> c
[1, 2]
>>> a is c
True
>>> c.append(3)
>>> c
[1, 2, 3]
>>> a
[1, 2, 3]
>>> b=a.copy()
>>> b
[1, 2, 3]
>>> b.append(4)
>>> b
[1, 2, 3, 4]
>>> a
[1, 2, 3]
>>> l
[29, 33, 43, 67, 67, 83, 89, 99]
>>> any(l)
True
>>> all(l)
True
>>> l.append(0)
>>> l
[29, 33, 43, 67, 67, 83, 89, 99, 0]
>>> any(l)
True
>>> all(l)
False
>>> l=[0,0.0,0+0j,' ',[],(),set(),{}]
>>> any(l)
True
>>> all(l)
False
>>> l=[0,0.0,0+0j,'',[],(),set(),{}]
>>> any(l)
False
>>> all(l)
False
>>> l.append(1)
>>> any(l)
True
>>> all(l)
False
>>> 

