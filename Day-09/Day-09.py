Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> d={}
>>> d={1:1,2:2}
>>> d
{1: 1, 2: 2}
>>> type(d)
<class 'dict'>
>>> d={}
>>> d[1]='integer'
>>> d
{1: 'integer'}
>>> d[1.1]='float'
>>> d
{1: 'integer', 1.1: 'float'}
>>> d[10+11j]='complex'
>>> d
{1: 'integer', 1.1: 'float', (10+11j): 'complex'}
>>> d['str']='string'
>>> d
{1: 'integer', 1.1: 'float', (10+11j): 'complex', 'str': 'string'}
>>> d[[1,2,3]]='list'
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    d[[1,2,3]]='list'
TypeError: unhashable type: 'list'
>>> d[(1,2,3)]='tuple'
>>> d
{1: 'integer', 1.1: 'float', (10+11j): 'complex', 'str': 'string', (1, 2, 3): 'tuple'}
>>> d[{1,23,34}]='set'
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    d[{1,23,34}]='set'
TypeError: unhashable type: 'set'
>>> d[{1:2,3:4}]='dictionary'
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    d[{1:2,3:4}]='dictionary'
TypeError: unhashable type: 'dict'
>>> d[False]='boolean'
>>> d
{1: 'integer', 1.1: 'float', (10+11j): 'complex', 'str': 'string', (1, 2, 3): 'tuple', False: 'boolean'}
>>> d[1]=1
>>> d
{1: 1, 1.1: 'float', (10+11j): 'complex', 'str': 'string', (1, 2, 3): 'tuple', False: 'boolean'}
>>> d.clear()
>>> d
{}
>>> d[1]=11
>>> d[2]=11.2
>>> d[3]=10+11j
>>> d[4]='string'
>>> d[5]=[1,2,3]
>>> d[6]=(1,2,3)
>>> d[7]={1,2,3}
>>> d[8]={1:1,2:2,3:3}
>>> d[9]=False
>>> d
{1: 11, 2: 11.2, 3: (10+11j), 4: 'string', 5: [1, 2, 3], 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 1, 2: 2, 3: 3}, 9: False}
>>> d[10]=11
>>> d[12]=(1,2,3)
>>> d
{1: 11, 2: 11.2, 3: (10+11j), 4: 'string', 5: [1, 2, 3], 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 1, 2: 2, 3: 3}, 9: False, 10: 11, 12: (1, 2, 3)}
>>> d[1]
11
>>> d[8]
{1: 1, 2: 2, 3: 3}
>>> d[10]
11
>>> d[13]
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    d[13]
KeyError: 13
>>> d.get(13)
>>> d.get(7)
{1, 2, 3}
>>> d.get(14,'key is not there')
'key is not there'
>>> d.get(10,'key is not there')
11
>>> 'string' in d
False
>>> 1 in d
True
>>> [1,2,3] in d
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    [1,2,3] in d
TypeError: unhashable type: 'list'
>>> 11.2 in d
False
>>> 11 in d
False
>>> 12 in d
True
>>> 13 in d
False
>>> 'string' not in d
True
>>> [1,2,3] not in d
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    [1,2,3] not in d
TypeError: unhashable type: 'list'
>>> d[8]='dict'
>>> d
{1: 11, 2: 11.2, 3: (10+11j), 4: 'string', 5: [1, 2, 3], 6: (1, 2, 3), 7: {1, 2, 3}, 8: 'dict', 9: False, 10: 11, 12: (1, 2, 3)}
>>> d[3]=3434
>>> d
{1: 11, 2: 11.2, 3: 3434, 4: 'string', 5: [1, 2, 3], 6: (1, 2, 3), 7: {1, 2, 3}, 8: 'dict', 9: False, 10: 11, 12: (1, 2, 3)}
>>> d[11]=100
>>> d
{1: 11, 2: 11.2, 3: 3434, 4: 'string', 5: [1, 2, 3], 6: (1, 2, 3), 7: {1, 2, 3}, 8: 'dict', 9: False, 10: 11, 12: (1, 2, 3), 11: 100}
>>> d[15]=2323.4455
>>> d
{1: 11, 2: 11.2, 3: 3434, 4: 'string', 5: [1, 2, 3], 6: (1, 2, 3), 7: {1, 2, 3}, 8: 'dict', 9: False, 10: 11, 12: (1, 2, 3), 11: 100, 15: 2323.4455}
>>> d.update({13:'dncd',14:(1,2,3)})
>>> d
{1: 11, 2: 11.2, 3: 3434, 4: 'string', 5: [1, 2, 3], 6: (1, 2, 3), 7: {1, 2, 3}, 8: 'dict', 9: False, 10: 11, 12: (1, 2, 3), 11: 100, 15: 2323.4455, 13: 'dncd', 14: (1, 2, 3)}
>>> d.popitem()
(14, (1, 2, 3))
>>> d.pop(11)
100
>>> d.pop(7)
{1, 2, 3}
>>> d
{1: 11, 2: 11.2, 3: 3434, 4: 'string', 5: [1, 2, 3], 6: (1, 2, 3), 8: 'dict', 9: False, 10: 11, 12: (1, 2, 3), 15: 2323.4455, 13: 'dncd'}
>>> del d[5]
>>> d
{1: 11, 2: 11.2, 3: 3434, 4: 'string', 6: (1, 2, 3), 8: 'dict', 9: False, 10: 11, 12: (1, 2, 3), 15: 2323.4455, 13: 'dncd'}
>>> del d[13]
>>> d
{1: 11, 2: 11.2, 3: 3434, 4: 'string', 6: (1, 2, 3), 8: 'dict', 9: False, 10: 11, 12: (1, 2, 3), 15: 2323.4455}
>>> d.clear()
>>> d
{}
>>> d={1: 11, 2: 11.2, 3: 3434, 4: 'string', 6: (1, 2, 3), 8: 'dict', 9: False, 10: 11, 12: (1, 2, 3), 15: 2323.4455}
>>> d
{1: 11, 2: 11.2, 3: 3434, 4: 'string', 6: (1, 2, 3), 8: 'dict', 9: False, 10: 11, 12: (1, 2, 3), 15: 2323.4455}
>>> d.keys()
dict_keys([1, 2, 3, 4, 6, 8, 9, 10, 12, 15])
>>> d.values()
dict_values([11, 11.2, 3434, 'string', (1, 2, 3), 'dict', False, 11, (1, 2, 3), 2323.4455])
>>> d.items()
dict_items([(1, 11), (2, 11.2), (3, 3434), (4, 'string'), (6, (1, 2, 3)), (8, 'dict'), (9, False), (10, 11), (12, (1, 2, 3)), (15, 2323.4455)])
>>> len(d)
10
>>> sorted(d)
[1, 2, 3, 4, 6, 8, 9, 10, 12, 15]
>>> max(d)
15
>>> min(d)
1
>>> a={1:1,2:2}
>>> b=a
>>> b[3]=3
>>> a
{1: 1, 2: 2, 3: 3}
>>> b
{1: 1, 2: 2, 3: 3}
>>> c=a.copy()
>>> c[4]=4
>>> a
{1: 1, 2: 2, 3: 3}
>>> c
{1: 1, 2: 2, 3: 3, 4: 4}
>>> d=dict.fromkeys(['a','b','c','d'],0)
>>> d
{'a': 0, 'b': 0, 'c': 0, 'd': 0}
>>> d.setdefault('a')
0
>>> d.setdefault('e')
>>> d
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': None}
>>> d.setdefault('i',1.2)
1.2
>>> d
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': None, 'i': 1.2}
>>> d.setdefault('c',3232)
0
>>> d
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': None, 'i': 1.2}
>>> 
