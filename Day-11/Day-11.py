data=('admin@gmail.com','admin@123')
gmail=input('Enter the mail:')
password=input('Enter the password:')
if(gmail,password)==data:
    print('Login Successful','\n')
else:
    print('Invalid Login','\n')


seats={
    's1':'Booked',
    's2':'Available',
    's3':'Available',
    's4':'Available',
    's5':'Booked',
    's6':'Available'
    }
seatno=input('Enter the seat number:')
if seatno in seats and seats[seatno]=='Available':
    seats[seatno]='Booked'
    print(f'{seatno} is booked successfully')
    print(seats,'\n')
else:
    print(f'{seatno} is already booked','\n')


products={
    'laptop':{'price':60000,'stock':10},
    'mouse':{'price':500,'stock':0},
    'keyboard':{'price':2000,'stock':3},
    'tab':{'price':25000,'stock':5},
    'phone':{'price':30000,'stock':8}
    }
search=input('Enter the product:')
if search in products and products[search]['stock']>0:
    print(f"You can buy {search} for ₹ {products[search]['price']}",'\n')
else:
    print(f'{search} is not available','\n')


print('Welcome to the Weekend Planner')
budget=int(input('Enter the budget:'))
print('You can go for a ',end='')
if budget>10000:
    print('Trip')
elif budget>5000:
    print('Resort')
elif budget>2000:
    print('Cafe')
elif budget>1000:
    print('Movie')
elif budget>500:
    print('Street shopping')
else:
    print('Sleep')
print()


data={
    'praveen':{'status':True,'python':96,'mysql':95,'fastapi':93},
    'krishna':{'status':True,'python':86,'mysql':85,'fastapi':83},
    'eswar':{'status':True,'python':56,'mysql':65,'fastapi':63},
    'surya':{'status':True,'python':46,'mysql':45,'fastapi':43},
    'raghu':{'status':True,'python':26,'mysql':25,'fastapi':33},
    'abdul':{'status':False,'python':None,'mysql':None,'fastapi':None}
    }
name=input("Enter the name:")
if name in data:
    if data[name]['status']:
        tot=data[name]['python']+data[name]['mysql']+data[name]['fastapi']
        avg=tot/3
        if avg>80:
            print(f'{name}, congrats you got first grade')
        elif avg>60:
            print(f'{name}, good and workhard next time')
        elif avg>40:
            print(f'{name}, better luck next time')
        elif avg>35:
            print(f'{name}, you just passsed,workhard')
        else:
            print(f'{name}, you failed the exam')
    else:
        print(f'{name}, didnot attend the exam')
else:
    print(f'{name} is not found in the data')