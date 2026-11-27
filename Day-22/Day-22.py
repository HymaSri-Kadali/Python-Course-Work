#know the count of digits in a number
n=str(6111111334444555666222)
c=1
res=''
for i in range(len(n)-1):
    if n[i]==n[i+1]:
        c+=1
    else:
        res+=n[i]+str(c)
        c=1
print(res+n[i]+str(c))
print()

#find the repeated and missing number in a list
l=[1,2,3,3,5,6]
repeated=0
missing=0
for i in range(len(l)-1):
    if l[i]+1!=l[i+1]:
        repeated=l[i+1]
        missing=l[i]+1
        break
print(f'Repeated number:{repeated}\nMissing number:{missing}')
print()

#check whether the string is balanced or unbalanced parentheses
s='{([(])}'
res=[]
for i in s:
    if i in ('{','[','('):
        res.append(i)
    elif res==[]:
        print('Unbalanced')
        break
    elif i=='}':
        p=res.pop()
        if p!='{':
            print('Unbalanced')
            break
    elif i==')':
            p=res.pop()
            if p!='(':
                print('Unbalanced')
                break
    elif i==']':
            p=res.pop()
            if p!='[':
                print('Unbalanced')
                break
else:
    print('Balanced')