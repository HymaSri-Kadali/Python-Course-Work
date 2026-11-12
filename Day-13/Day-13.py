pin=1234
for i in range(5):
    epin=int(input('Enter the pin:'))
    if epin==pin:
        print('Login Successful\n')
        break
    else:
        print('Invalid Login')
else:
    print('Max attempts reached! Try again after 30 secs\n')


l=[2,4,6,7,24,90,24,45,34,56,40]
search=int(input('Enter the number:'))
for i in range(len(l)):
    if l[i]==search:
        print(f'{search} is found at {i} index\n')
        break
else:
    print(f'{search} is not found\n')
#enumerate over a str,list,tuple,set,dict
s='codegnan'
for i in enumerate(s):
    print(i[0],i[1])
print()

l=[11,22,33,44,55]
for i in enumerate(l):
    print(i[0],i[1])
print()

t=(11,22,33,44,55)
for i in enumerate(t):
    print(i[0],i[1])
print()

se={11,22,33,44,55}
for i in enumerate(se):
    print(i[0],i[1])
print()

dic={'k1':'v1','k2':'v2','k3':'v3'}
for i in enumerate(dic):
    print(i[0],i[1],dic[i[1]])
print()
#remove all zeros from a list
l=[1,0,3,0,4,0,0,0,0,5,0,6,0,4,0]
while 0 in l:
    l.remove(0)
print(l)
print()
#print nums from 1 to 10
i=1
while i<11:
    print(i,end=' ')
    i+=1
print('\n')
#print nums from 1 to 10(descending order)
i=10
while i>0:
    print(i,end=' ')
    i-=1
print('\n')
#print even nums upto 100
i=2
while i<101:
        print(i,end=' ')
        i+=2
print('\n')
#print multiples of 5 upto 100
i=5
while i<101:
        print(i,end=' ')
        i+=5
print('\n')
#iterate over a str,list,tuple
s='Python Programming'
i=0
while i<len(s):
    print(i,s[i])
    i+=1
print()

l=[1,3,5,7,9,11]
i=0
while i<len(l):
    print(i,l[i])
    i+=1
print()

t=(1,3,5,7,9,11)
i=0
while i<len(t):
    print(i,t[i])
    i+=1
print()
#list traversal with a break and continue condition
l=[1,3,5,7,9,11]
i=0
while i<len(l):
    if l[i]==7:
        break
    print(i,l[i])
    i+=1
print('\n')

l=[1,3,5,7,9,11]
i=-1
while i<len(l)-1:
    i+=1
    if l[i]==7:
        continue
    print(i,l[i])
print('\n')
#symmetrical and full length two pointer traversal
s='Python Programming'
i=0
j=len(s)-1
while i<=j:#while i<len(s):
    if i==j:
        print(s[i])
    else:
        print(s[i],s[j])
    i+=1
    j-=1