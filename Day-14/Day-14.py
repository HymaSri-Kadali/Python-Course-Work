#sum of first and last values moving inward
l=[12,9,3,4,5,10,2,4,5,2,4,5,1]
i=0
j=len(l)-1
while i<=j:
    if i==j:
        print(l[i])
    else:
        print(l[i]+l[j])
    i+=1
    j-=1
print()

bill=0
while True:
    product=input('Enter the product name(STOP):').lower()
    if product=='stop':
        print('Total bill:',bill)
        break
    price=int(input('Enter the price:'))
    quantity=int(input('Enter the quantity:'))
    bill+=price*quantity
print()

product={'salt':30,'milk':20,'sugar':25,'curd':10,'ghee':50}
print('Welcome to the store'.center(50,'-'))
print('Product Name','Price')
for i in product:
    print(i.ljust(12,' '),':',product[i])
carts={}
while True:
    cart=input('Enter the Product Name(EXIT):').lower()
    if cart=='exit':
        break
    qua=int(input('Enter the quantity:'))
    carts[cart]=qua
print('Bill'.center(50,'-'))
print('Product Name Quantity Price(₹)')
bill=0
for i in carts:
    print(i.ljust(12,' '),str(carts[i]).ljust(12,' '),product[i])
    bill+=carts[i]*product[i]     
print(f'Total bill:₹ {bill}')
print('Thanks for Shopping'.center(50,'-'))