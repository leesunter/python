'''
Created on 24 Apr 2018

@author: s258115
'''
from time import sleep

# --- Simple debug ---
print('#### DEBUG ####')
def debug(*msg, print_separator=True):
    print(*msg)
    # keyword-only argument to be able to print a separator, which is a line of 40 dashes.
    if print_separator:
        print('-' * 40)

debug('Data is ...')
debug('Different', 'Strings', 'Are not a problem')
debug('After while loop', print_separator=False)


# --- Time Debug ---
print('#### TIME DEBUG ####')
def debugTime(*msg, timestamp=[None]):
    print(*msg)
    from time import time # local import *****
    if timestamp[0] is None:
        timestamp[0] = time() #1
    else:
        now = time()
        print(' Time elapsed: {:.3f}s'.format(
            now - timestamp[0]))
        # as we keep the time value update the default which was None
        timestamp[0] = now #2
        
debugTime('Entering nasty piece of code...')
sleep(.3)
debugTime('First step done.')
sleep(.5)
debugTime('Second step done.')


# --- Trace back ----
print('#### TRACEBACK KeyError ####')
d = {'some': 'key'}
key = 'some-other'
# this causes an error to show in the output
# commented out so next code works   print(d[key])
# Returns all the information we need: the module name, the line that caused the error 
# (both the number and the instruction), and the error itself.

print('#### TRACEBACK KeyError trap Exception ####')
# define a custom exception that is raised when the mandatory key isn't there
class ValidatorError(Exception):
    """Raised when accessing a dict results in KeyError. """

d = {'some': 'key'}

mandatory_key = 'some-other'
try:
    # simply, we define a dummy dict and try to access it using mandatory_key
    print(d[mandatory_key])
except KeyError:
    raise ValidatorError(
        '`{}` not found in d.'.format(mandatory_key))

# Python 'ipdb' debugger
#import ipdb
#ipdb.set_trace() # we place a breakpoint here

# Assertions
# assert 4 == 3 # this will break