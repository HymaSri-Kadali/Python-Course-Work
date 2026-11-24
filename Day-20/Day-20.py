#add three numbers
s=lambda a,b,c:a+b+c
print(s(10,20,30))
print()

#calculate 18% GST on a given price
gst=lambda price:price+price*0.18
print(gst(1000))
print()

#average of all elements in a list
avg=lambda l:sum(l)/len(l)
l=[20,55,43,60]
print(avg(l))
print()

#check whether a number is even or odd
iseven=lambda n:'Even' if n%2==0 else 'Odd'
print(iseven(10))
print(iseven(11))
print()

#check whether a character is a vowel or consonant
isvowel=lambda ch:'Vowel' if ch in 'aeiouAEIOU' else 'Consonant'
print(isvowel('a'))
print(isvowel('z'))
print()

#using nested if-else statements in lambda function
check=lambda data,pro:(f"Product price:{data[pro]['price']}" if data[pro]['stock']>0 else 'Out of stock') if pro in data else 'Product is unavailable'
data={
    'apple':{'stock':10,'price':50},
    'mango':{'stock':20,'price':40},
    'banana':{'stock':60,'price':10},
    'sapota':{'stock':0,'price':10},
    'coconut':{'stock':30,'price':120}
}
print(check(data,'apple'))
print()

#add 10 to each element in a list using a user-defined function
def addten(l):
    for i in range(len(l)):
        l[i]+=10
    return l
l=[9,8,7,4,3,20]
print(addten(l))
#or(add 10 to each element in a list using map() and lambda function)
l=[9,8,7,4,3,20]
addten=list(map(lambda i:i+10,l))
print(addten)
print()

#extract domain name from a list of email addresses using a user-defined function
def domain(d):
    for i in range(len(d)):
        d[i]=(d[i].split('@')[1]).split('.')[0]
    return d
d=['xyz@codegnan.com','abc@gmail.com','pqr@yahoo.com']
print(domain(d))
#or(extract domain name from a list of email addresses using map() and lambda function)
d=['xyz@codegnan.com','abc@gmail.com','pqr@yahoo.com']
domain=list(map(lambda i:(i.split('@')[1]).split('.')[0],d))
print(domain)
print()

#convert all elements in a list to uppercase
c=['effrf','fjeif','enpane']
u=list(map(lambda i:i.upper(),c))
print(u)
print()

#calculate 18% GST for each product in a dictionary
d={'a':20,'b':30,'c':1000,'e':500,'d':2000}
gst=dict(map(lambda i:(i[0],i[1]+i[1]*0.18),d.items()))
print(gst)
print()

#print even numbers from a list
l=[1,2,3,4,5,6,7,8,9,10]
even=list(filter(lambda i:i%2==0,l))
print(even)
print()

#print vowels from a list
a=['e','i','h','l','a','d','o']
vowels=list(filter(lambda i:i in 'aeiouAEIOU',a))
print(vowels)
print()

#calculate sum of all elements in a list
from functools import reduce
l=[1,2,3,4,5,6,7,8,9,10]
sum_of_l=reduce(lambda sum,i:sum+i,l)#replace + with * to get multiplication
print(sum_of_l)
print()

#calculate maximum of all elements in a list
from functools import reduce
l=[1,2,3,4,5,6,7,8,9,10]
max_of_l=reduce(lambda max,i:max if max>i else i,l)#replace > with < to get min
print(max_of_l)
print()

#calculate 18% GST for each product in a dictionary
d={'a':900,'b':200,'c':1000,'d':1300}
s={'s1': True, 's2':False,'s3':True,'s4':True,'s5':False}
gst=dict(map(lambda i:(i[0],i[1]+i[1]*0.18),d.items()))
gre=dict(filter(lambda i:i[1]>500,d.items()))
booked=dict(filter(lambda i:i[1]==True,s.items()))
unbooked=dict(filter(lambda i:i[1]!=True,s.items()))
print(gst)
print(gre)
print(booked)
print(unbooked)
print()

#sorting a dictionary by keys and values
d={'laptop':90000,'keyboard':2000,'camera':100000,'mouse':1300}
print(dict(sorted(d.items())))
print(dict(sorted(d.items(),reverse=True)))
print(dict(sorted(d.items(),key=lambda i:i[1])))
print(dict(sorted(d.items(),key=lambda i:i[1],reverse=True)))