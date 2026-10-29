a=10
print(type(a))

b=1.25
print(type(b))

c=2+5j
print(type(c))

s="string"
print(type(s))

l=[1,1,1]
print(l)
print(type(l))

l=[l,1.2,'string',[1,2,3]]
print(l)
print(type(l))

s='code'
print(id(s))

s+='gnan'
print(id(s))
print(type(s))
print(s)

l=[1,2,3]
print(id(l))

l.append(4)
print(l)
print(id(l))

l.pop()
print(l)
print(id(l))

t=(1,1,1)
print(t)

t=(1,2.3,5)
print(t)
print(type(t))

s={34, 124, 124, 32843, 34,32843, 1, 124}
print(s)
print(type(s))

d={1:55,2:98.76,3:10+11j,4:'one',5:[12,356,9],6:(1,23,15),7:{5,3,4,4,5,3}}
print(d)

pro={"pro_name":"laptop","price":55,"discount":10}
print(pro)
print(type(d))

b=True
print(b)
print(type(b))

n=None
print(n)
print(type(n))
