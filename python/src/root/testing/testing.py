'''
Created on 16 Apr 2018

@author: s258115
'''
import unittest

class Test(unittest.TestCase):


    def setUp(self):
        print("setup test")


    def tearDown(self):
        print("tear down test")


    def testSuccess(self):
        if (1==1):
            print("success")
        else:
            print("fail")
            
    def testFail(self):
        if (1==2):
            print("success")
        else:
            print("fail")        


# Run test
unittest.main()
    
    
    