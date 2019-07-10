
from testcase import pay_test
from unittest.runner import TextTestRunner
def run_1():
    import unittest
    suite=unittest.TestSuite()
    suite1=unittest.defaultTestLoader.loadTestsFromModule(pay_test)    
    suite.addTests(suite1)
    runner=TextTestRunner()
    runner.run(suite)
for i in range(1,100):
    run_1()