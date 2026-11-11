s='codegnan'
for i in s:
    print(i)
print()

s1=input('Enter the word:')
for i in s1:
    if i in 'aeiouAEIOU':
        print(i)
print()


l=[10,23,45,89,56]
for i in l:
    print(i)
print()

l1=list(map(int,input('Enter the numbers:').split()))
for i in l1:
    if i%2==0:
        print(i)
print()


t=(10,23,45,89,56)
for i in t:
    print(i)
print()

sum=0
t1=tuple(map(int,input('Enter the numbers:').split()))
for i in t1:
    sum+=i
print('Sum of tuple:',sum,'\n')


s={10,23,45,89,56}
for i in s:
    print(i)
print()

max=0
s1=set(map(int,input('Enter the numbers:').split()))
for i in s1:
    if i>max:
        max=i
print('Max of set:',max,'\n')


dict={'python':11,'mysql':22,'fastapi':33,'html':44,'css':55}
for i in dict:
    print(i,':',dict[i])
print()

sum=0
dict={'python':11,'mysql':22,'fastapi':33,'html':44,'css':55}
for i in dict:
    sum+=dict[i]
print('Total Marks:',sum,'\n')


for i in range(1,11):
    print(i,end=' ')
print('\n')


for i in range(20,0,-1):
    print(i,end=' ')
print('\n')


for i in range(2,51,2):
    print(i,end=' ')
print('\n')


n=int(input('Enter the number:'))
for i in range(1,21):
    print(f'{n}*{i}={n*i}')
print()


c='codegnan'
for i in range(len(c)):
    print(c[i],i,end=' ')
print('\n')


sum=0
l=[12,34,45,10,78,43,80]
for i in range(len(l)):
    if l[i]%2==0:
        sum+=i
print(sum,'\n')


mul=1
t=(12,34,45,10,78,43,80)
for i in range(len(t)):
    if t[i]%2!=0:
        mul*=i
print(mul,'\n')


for i in range(1,11):
    if i==5:
        break
    print(i,end=' ')
print('\n')


for i in range(1,11):
    if i==5:
        continue
    print(i,end=' ')
print('\n')


for i in range(1,11):
    pass
if True:
    pass
class Booking:
    pass
def func():
    pass