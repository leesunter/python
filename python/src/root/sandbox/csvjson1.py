'''
Created on 23 Mar 2018

@author: s258115
'''
import sys
import csv  
import json 


print('Hello')
print(sys.version)  

# Open the CSV  
f = open( 'c:/Temp/test.csv', 'rU' )  
# Change each fieldname to the appropriate field name. 
reader = csv.DictReader( f, fieldnames = ( "fieldname0","fieldname1","fieldname2","fieldname3" ))  
# Parse the CSV into JSON  
out = json.dumps( [ row for row in reader ] )  

print('JSON parsed!')

# Save the JSON  
f = open( 'c:/Temp/test.json', 'w')  
f.write(out)  
print('JSON saved!')  