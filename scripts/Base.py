# coding=utf-8
import os
import unittest
import sys
sys.path.append('..')
from Engine import browser


class Base(unittest.TestCase):
    '''
    基类，用于所有测试类的继承
    '''
    @classmethod
    def  setUpClass(cls):
        cls.driver = browser()
        #cls.driver = browser('ff')
        #cls.driver = browser('eg')

    def setUp(self):
        # 
        # cls.driver = browser() 
        pass

    def tearDown(self):
        for method_name,error in self._outcome.errors:
              if error:
                  case_name = self._testMethodName
                  file_path = os.path.join(os.getcwd()+"/result/img/"+case_name+".png")
                  self.driver.save_screenshot(file_path)
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    pass

