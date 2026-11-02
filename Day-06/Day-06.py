Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s=''
>>> s
''
>>> s='Python'
>>> s
'Python'
>>> s1='Programming'
>>> s1
'Programming'
>>> s+s1
'PythonProgramming'
>>> s*3
'PythonPythonPython'
>>> s1*10
'ProgrammingProgrammingProgrammingProgrammingProgrammingProgrammingProgrammingProgrammingProgrammingProgramming'
>>> '*'*7
'*******'
>>> '0'*5
'00000'
>>> s='python java flask mysql fastapi'
>>> s
'python java flask mysql fastapi'
>>> s[0]
'p'
>>> s[-1]
'i'
>>> s[-7]
'f'
>>> s[17]
' '
>>> s[0:6:1]
'python'
>>> s[:6]
'python'
>>> s[7:11]
'java'
>>> s[12:17]
'flask'
>>> s[18:23]
'mysql'
>>> s[24:]
'fastapi'
>>> s[24:31]
'fastapi'
>>> s[::2]
'pto aafakmslfsai'
>>> s[::-2]
'iasflsmkafaa otp'
>>> s[::-1]
'ipatsaf lqsym ksalf avaj nohtyp'
>>> s[-7:]
'fastapi'
>>> s[-15:-20:-1]
'ksalf'
>>> s[5::-1]
'nohtyp'
>>> 'mysql' in s
True
>>> 'c++' in s
False
>>> 'mysql' not in s
False
>>> 'c++' not in s
True
>>> len(s)
31
>>> ord('a')
97
>>> ord('A')
65
>>> ord('+')
43
>>> ord('/')
47
>>> ord(' ')
32
>>> ord('')
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    ord('')
TypeError: ord() expected a character, but string of length 0 found
>>> ord('@')
64
>>> ord('8')
56
>>> ord('0')
48
>>> chr(97)
'a'
>>> chr(65)
'A'
>>> chr(43)
'+'
>>> chr(47)
'/'
>>> chr(32)
' '
>>> chr(64)
'@'
>>> chr(48)
'0'
>>> chr(10)
'\n'
>>> chr(20)
'\x14'
>>> min(s)
' '
>>> max(s)
'y'
>>> sorted(s)
[' ', ' ', ' ', ' ', 'a', 'a', 'a', 'a', 'a', 'f', 'f', 'h', 'i', 'j', 'k', 'l', 'l', 'm', 'n', 'o', 'p', 'p', 'q', 's', 's', 's', 't', 't', 'v', 'y', 'y']
>>> s.upper()
'PYTHON JAVA FLASK MYSQL FASTAPI'
>>> s.lower()
'python java flask mysql fastapi'
>>> s.title()
'Python Java Flask Mysql Fastapi'
>>> s.capitalize()
'Python java flask mysql fastapi'
>>> s1='MySQL FastAPI GenAI'
>>> s1
'MySQL FastAPI GenAI'
>>> s1.swapcase()
'mYsql fASTapi gENai'
>>> "STRAẞEMÁLAGAÅngströmCafé".casefold()
'strassemálagaångströmcafé'
>>> s='python'
>>> s
'python'
>>> s.center(10,'*')
'**python**'
>>> s.center(10,' ')
'  python  '
>>> s.ljust(10,'*')
'python****'
>>> s.rjust(10,'*')
'****python'
>>> '1'.zfill(5)
'00001'
>>> '123'.zfill(5)
'00123'
>>> '123456789'.zfill(5)
'123456789'
>>> s='python java flask mysql fastapi'
>>> s.find('y')
1
>>> s.find('z')
-1
>>> s.rfind('a')
28
>>> s.rfind('f')
24
>>> s.index('y')
1
>>> s.index('f')
12
>>> s.index('z')
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    s.index('z')
ValueError: substring not found
>>> s.rindex('f')
24
>>> s.rindex('a')
28
>>> s.count('a')
5
>>> s.count('z')
0
>>> s.count(' ')
4
>>> s='     code gnan     '
>>> s
'     code gnan     '
>>> s.strip()
'code gnan'
>>> s.rstrip()
'     code gnan'
>>> s.lstrip()
'code gnan     '
>>> s='python java flask mysql fastapi'
>>> s.replace('a','*')
'python j*v* fl*sk mysql f*st*pi'
>>> s.replace('p','1')
'1ython java flask mysql fasta1i'
>>> s.maketrans('apkqs','12345')
{97: 49, 112: 50, 107: 51, 113: 52, 115: 53}
>>> s.translate(s.maketrans('apkqs','12345'))
'2ython j1v1 fl153 my54l f15t12i'
>>> s.translate(s.maketrans('aeiou','*****'))
'pyth*n j*v* fl*sk mysql f*st*p*'
>>> s='Python Programming'
>>> s.startswith('P')
True
>>> s.startswith('p')
False
>>> s.startswith('Pyt')
True
>>> s.endswith('img')
False
>>> s.endswith('ing')
True
>>> 's'.islower()
True
>>> 'S'.isupper()
True
>>> 'Codegnan@'.isalpha()
False
>>> 'CodeGnan'.isalpha()
True
>>> 'code1234'.isalnum()
True
>>> 'code@1234'.isalnum()
False
>>> 'code'.isalnum()
True
>>> '1234'.isalnum()
True
>>> s.istitle()
True
>>> 'myvar'.isidentifier()
True
>>> 'my@var'.isidentifier()
False
>>> ''.isspace()
False
>>> ' '.isspace()
True
>>> '	hello'.isspace()
False
>>> '1234'.isdecimal()
True
>>> '1234'.isdigit()
True
>>> '1234'.isnumeric()
True
>>> 'a b c d'.split()
['a', 'b', 'c', 'd']
>>> 'a,b,c,d'.split()
['a,b,c,d']
>>> 'a,b,c,d'.split(',')
['a', 'b', 'c', 'd']
>>> 'a-b-c-d'.split('-')
['a', 'b', 'c', 'd']
>>> 'a-b-c-d'.split('-',2)
['a', 'b', 'c-d']
>>> 'a-b-c-d'.rsplit('-')
['a', 'b', 'c', 'd']
>>> 'a-b-c-d'.rsplit('-',2)
['a-b', 'c', 'd']
>>> s='''
hello
world
python
'''
>>> s
'\nhello\nworld\npython\n'
>>> s.splitlines()
['', 'hello', 'world', 'python']
>>> l=['a','b','c','d']
>>> '-'.join(l)
'a-b-c-d'
>>> '@'.join(l)
'a@b@c@d'
>>> ''.join(l)
'abcd'
>>> ' '.join(l)
'a b c d'
>>> s='a-b-c-d'
>>> s.partition('b')
('a-', 'b', '-c-d')
>>> 'python.py'.partition('.')
('python', '.', 'py')
>>> 'pyt.hon.py'.partition('.')
('pyt', '.', 'hon.py')
>>> 'pyt.hon.py'.rpartition('.')
('pyt.hon', '.', 'py')
>>> s='hello'
>>> s.encode()
b'hello'
>>> b'hello'.decode()
'hello'
>>> t='Hello ☺'
>>> t.encode()
b'Hello \xe2\x98\xba'
>>> b'Hello \xe2\x98\xba'.decode()
'Hello ☺'
>>> 
