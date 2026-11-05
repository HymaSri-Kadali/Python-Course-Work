product=input('Enter product:')
bestseller=eval(input('Enter status(True or False):'))
if bestseller:
    print(f'{product} is best seller')


battery=int(input('Enter battery:'))
if battery<20:
    print(f'Low battery:{battery}.Charge your phone')


bill=int(input('Enter bill:'))
status=eval(input('Is it raining?(True or False) '))
if status:
    bill+=30
    print('Extra delivery charges applied')
print(f'Final bill:{bill}')