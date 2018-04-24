'''
Created on 12 Apr 2018

@author: s258115
'''

print("####### Numbers ######")
a =12
b =3
print(a+b)
print(a-b)
print(a/b) # true division 4.0
print(a//b) # integer division, flooring returns 4
print(a*b)
print(a**b) #power operator
print(a%b)# remainder of the division 12/3 = 0

pi1 = 3.1415926536 # how many digits of PI can you remember?
radius = 4.5
#print('area ='  pi1 * (radius ** 2))

#print("####### Fractions ########")
#import fractions.Fraction
#print(fractions.Fraction(10,6)) # reduces to 5/3
#print(fractions.Fraction(1,3)+ fractions.Fraction(2,3)) # =1/1
#f= fractions.Fraction(10,6)
#print('numerator=' f.numerator()))
#print('denomiator=' f.denominator())

print("######## Booleans #######")
print(int(True))
print(bool(1))
print(bool(-3))
print(not True)
print(True and True)
print(True or False)
print(True+1) # =2 (true is 1 and false is 0)

print("##### Strings ######")
s = "The trouble is you think you have time."
print(s[0]) # indexing at position 0, which is the first char - T
print(s[2:14]) # slicing, both start and stop positions 
print(s[:]) # quick way of making a copy


print('##### tuples ####')
#A tuple is a sequence of arbitrary Python objects. In a tuple, items are separated by commas.
print(())
print((1,2,3,4,5))


print('######## Lists #####')
print([]) # empty list
print(list()) # empty list
print([1, 2, 3]) # as with tuples, items are comma separated
print([x + 5 for x in [2, 3, 4]]) # Python is magic (adds 5 to each)  [7, 8, 9]
print(list((1, 3, 5, 7, 9))) # list from a tuple
print(list('hello')) # list from a string ['h', 'e', 'l', 'l', 'o']
a = [1, 2, 1, 3]
a.append(13)
print(a) # we can append anything at the end [1, 2, 1, 3, 13]
print(a.count(1)) # how many `1` are there in the list? - 2
a.extend([5, 7]) # extend the list by another (or sequence)
print(a) # [1, 2, 1, 3, 13, 5, 7]
print(a.index(13))  # position of `13` in the list (0-based indexing) - 4
a.insert(0, 17) # insert `17` at position 0
print(a) # [17, 1, 2, 1, 3, 13, 5, 7]
print(a.pop()) # pop (remove and return) last element -7
print(a.pop(3)) # pop element at position 3
print(a) # reminder of what we have in a = [17, 1, 2, 3, 13, 5]
a.remove(17) # remove `17` from the list
print(a) # [1, 2, 3, 13, 5]
a.reverse() # reverse the order of the elements in the list
print(a) # [5, 13, 3, 2, 1]
a.sort() # sort the list
print(a) # [1, 2, 3, 5, 13]
a.clear() # remove all elements from the list
print(a) # []
#a + b # `+` with list means concatenation

print("#### Dictionary #####")
print('a'=='a') # check whether an object is the same as another one
d = dict(zip('hello', range(5)))
# First, notice how we're creating a dictionary by iterating over the zipped version of the string 'hello' 
# and the list [0, 1, 2, 3, 4]. The string 'hello' has two 'l' characters inside, and they are paired up 
# with the values 2 and 3 by the zip function. Notice how in the dictionary, the second occurrence of the
# 'l' key (the one with value 3), overwrites the first one (the one with value 2).
print(d) # {'e': 1, 'h': 0, 'o': 4, 'l': 3}
print(d.keys()) # dict_keys(['e', 'h', 'o', 'l'])
print(d.values()) # dict_values([1, 0, 4, 3])
print(d.items()) # dict_items([('e', 1), ('h', 0), ('o', 4), ('l', 3)])
print(3 in d.values()) # 3 is in values so True
print(('o', 4) in d.items()) # ('o', 4) is in items so True
print(d.get('h','default value')) # get key h and value is returned 0
print(d.get('z','default value')) # get key z no value so default returned
# d.setdefault('a', 1) # 'a' is missing, we get the set default value 1
# collections module which are more advanced lists/collections etc.

#Python caches short strings and small numbers, to avoid having many copies of them clogging up
#the system memory. Everything is handled properly under the hood so you don't
#need to worry a bit, but make sure that you remember this behavior should your
#code ever need to fiddle with IDs.
# id(a)==id(b) a=1000000 b=1000000 FALSE  BUT  when a=5 and b=5 TRUE
