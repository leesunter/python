'''
Created on 24 Apr 2018

@author: s258115
'''
# Loggers expose the interface that the application code uses directly
# Handlers send the log records (created by loggers) to the appropriate destination
# Filters provide a finer grained facility for determining which log records to output
# Formatters specify the layout of the log records in the final output


import logging
# specify a filename, the minimum logging level we want to capture in the file, and the message
# format. We'll log the date and time information, the level, and the message
logging.basicConfig(
    filename='logging.log',
    level=logging.DEBUG, # minimum level capture in the file
    format='[%(asctime)s] %(levelname)s:%(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p')

mylist = [1, 2, 3]
logging.info('Starting to process `mylist`...')

for position in range(4):
    try:
        logging.debug('Value at position {} is {}'.format(
            position, mylist[position]))
    except IndexError:
        logging.exception('Faulty position: {}'.format(position))

logging.info('Done parsing `mylist`.')