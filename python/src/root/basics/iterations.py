'''
Created on 12 Apr 2018

@author: s258115
'''

print("#### if #####")
income = 15000
if income < 10000:
    tax_coefficient = 0.0 #1
elif income < 30000:
    tax_coefficient = 0.2 #2
elif income < 100000:
    tax_coefficient = 0.35 #3
else:
    tax_coefficient = 0.45 #4  
print('I will pay:', income * tax_coefficient, 'in taxes')
# ternary operator
order_total = 247 # GBP
discount = 25 if order_total > 100 else 0
print(order_total, discount)

print("#### for #####")
for number in [0, 1, 2, 3, 4]:
    print(number)
for number in range(5):
    print(number)
list(range(-10, 10, 4)) # three values: step is added [-10, -6, -2, 2, 6]
  
print("#### sequence #####")  
surnames = ['Rivest', 'Shamir', 'Adleman']
for position in range(len(surnames)): # len in 3
    print(position, surnames[position])
for surname in surnames: # simpler
    print(surname)
for position, surname in enumerate(surnames): # use of position. more efficient then len
    print(position, surname)   
    
print("#### iteration #####")  
print("#### ZIP as better than referencing a position #####")  
people = ['Jonas', 'Julio', 'Mike', 'Mez']
ages = [25, 30, 31, 39]
nationalities = ['Belgium', 'Spain', 'England', 'Bangladesh']
for person, age, nationality in zip(people, ages, nationalities): # 3 values and 3 lists
    print(person, age, nationality)
    
print("#### while #####")  
n = 39
remainders = []
while n > 0: #while true
    n, remainder = divmod(n, 2)
    remainders.append(remainder)
    # reassign the list to its reversed copy and print it
    remainders = remainders[::-1] # easy way to get the reversed version of a list (missing start and end parameters, step = -1, produces the same list, from end to start, in reverse order)
    print(remainders)

print("#### continue and break #####")  
class NumberException(Exception):
    pass
for number in [0, 1, 2, 3, 4]:
    if number == 3: #breaks at 3
        break
    elif number <4: #  prints 0,1,2 (as we broke out at 3)
        print(number)
        continue
print("#### exceptions #####")  
if number is 3:
    print(" raise NumberException('exception thrown.')")
    #raise NumberException('exception thrown.')
   
print("#### primes example loops etc #####")  
primes = []
upto = 100
for n in range(2, upto + 1): # no need for is prime flag
    for divisor in range(2, n):
        if n % divisor == 0:
            break
    else:
        primes.append(n)
print(primes)

print("#### infinite count #####")  
from itertools import count
for n in count(5, 3): # starts from 5 and keeps adding 3 to it until we break
    if n > 20:
        break
    print(n, end=', ') # instead of newline, comma and space
print()

print("#### Iterators terminating on the shortest input sequence #####")  
from itertools import compress
data = range(10)
even_selector = [1, 0] * 10
odd_selector = [0, 1] * 10
even_numbers = list(compress(data, even_selector))
odd_numbers = list(compress(data, odd_selector))
print("odd selector values:",odd_selector)
print("list data:",list(data))
print("even numbers:",even_numbers)
print("odd numbers:",odd_numbers)


