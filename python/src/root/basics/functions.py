'''
Created on 16 Apr 2018

@author: s258115
'''
print("#### function example #####")
x = 3 # this is defined in the global scope
def my_function(x):
    x=7 # this is defined in the local scope of the function
    print('my_function:', x) # print x=7 local created NOT updating global

my_function(x)
print('global:',x) # print x=3

print("#### function example mutable reference #####")
x = [1, 2, 3]
def func1(x):
    x[1] = 42 # this changes the caller!
    x = 'something else' # this points x to a new string object
func1(x)
print(x) # still prints: [1, 42, 3]

print("#### function using name=values #####")
def func2(a, b, c):
    print(a, b, c)
func2(a=1, c=2, b=3) # prints: 1 3 2

print("#### function using defaults #####")
def func3(a, b=4, c=88):
    print(a, b, c)
func3(1) # prints: 1 4 88
func3(b=5, a=7, c=9) # prints: 7 5 9
func3(42, c=9) # prints: 42 4 9

# variable positions def func(*args):
# variable arguments def func(**kwargs):

print("#### function using return values can be none #####")
def func4():
    pass
func4() # the return of this call won't be collected. It's lost.
a = func4() # the return of this one instead is collected into `a`
print(a) # prints: None

print("#### function using return values can be anything i.e. 2 (sets of) values #####")
def moddiv(a, b):
    return a // b, a % b
print(moddiv(20, 7)) # prints (2, 6)

# recursive functions 

print("#### annonomous functions #####")
def get_multiples_of_five(n):
    return list(filter(lambda k: not k % 5, range(n))) # lambda means no need for a function (is_multiple_of_five(n))
print(get_multiples_of_five(50))

print("# example 1: adder")
def adder(a, b):
    return a + b
# is equivalent to:
adder_lambda = lambda a, b: a + b
print(adder_lambda(1,2))

print("# example 2: to uppercase")
def to_upper(s):
    return s.upper()
# is equivalent to:
to_upper_lambda = lambda s: s.upper()
print(to_upper_lambda("lee"))


# import statments
import unittest # imports the unittest module
from math import sqrt # imports one function from math

from time import sleep, time
print(time())
sleep(.5)
print(time())

print("#### Function key points #####")
# in order to tell Python that it is actually a package, we need to put a __init__.py module in it.
print("### @staticmethod ###")
# place @staticmethod for statics
print("### @classmethod ###")
# @classmethod
#def from_tuple(cls, coords): # where 'cls' is the class the method is in


print("#### property decorator #####")

class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter 
    def age(self, age):
        if 18 <= age <= 99:
            self._age = age
        else:
            print('Error Age must be within [18, 99]')
    
person = Person(39)
print(person.age) # 39 - Notice we access as data attribute
person.age = 42 # Notice we access as data attribute
print(person.age) # 42
person.age = 100 # ValueError: Age must be within [18, 99]
