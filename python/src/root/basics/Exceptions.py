'''
Created on 16 Apr 2018

@author: s258115
'''

def try_syntax(numerator, denominator):
   
    try:
        print(' - In the try block: {}/{}'
              .format(numerator, denominator))
        result = numerator / denominator
    except ZeroDivisionError as zde: # catches the exception
        print(" -",zde) # printe exception
    # add more except-ion types
    else:
        print(' - The result is:', result)
        return result
    finally:
        print(' - Exiting')
print("first attempt",try_syntax(12, 4)) # returns 3.0
print("second attempt",try_syntax(11, 0)) # returns None as exception occurred