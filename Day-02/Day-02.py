n=10
if n%2==0:
	print("Even",'\n')
else:
	print("Odd"'\n')

#Single line comment
	
'''Multi
line
comments'''

"""Multi
line
comments"""

import keyword
print(keyword.kwlist)#keywords in python
print(len(keyword.kwlist),'\n')#length of keywords in python

a=1;b=2#assigning
print(a,b)

a=3#assigning
b=4
print(a,b)

a=b=c=5#assigning
print(a,b,c)

a,b,c=10,'A20',"A30"#assigning
print(a,b,c)

A=[100,'val1',"val2"]#assigning
a,b,c=A
print(A)

a,b,c=c,a,b#swapping
print(a,b,c)

del a#deleting
print(a)
