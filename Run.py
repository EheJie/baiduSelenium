# coding:utf-8
import os
import unittest
import time
from HTMLTestRunner import HTMLTestRunner
from libs.ShareModules import InsertLog

def load_test_case(ScriptPath):
    #创建测试集
    test_suite = unittest.TestSuite()
    #使用discover方法筛选测试用例
    discover = unittest.defaultTestLoader.discover(ScriptPath,
                                                   pattern = r'*_tc.py',
                                                   top_level_dir = None)

    #遍历discover对象，并将测试用例加载到测试集中
    for suite in discover:
        for cases in suite:
            for case in cases:
                test_suite.addTest(case)
    return test_suite

def run_tests():
    try:        
        dirpath = './scripts'
        sute = load_test_case(dirpath)
        currenttime = time.strftime('%y%m%d%H%M%S')
        file_dir = os.path.join(os.getcwd()+"/result/report/")
        file_path = file_dir + currenttime +".html"
        fp = open(file_path,'wb')
        runner = HTMLTestRunner(stream=fp,title=u'This is BaiduSearch report',description=u'这个是百度搜索的测试报告',verbosity=2)
        runner.run(sute)
        fp.close()
    except BaseException as msg:
        InsertLog('error',msg)



## 启动测试
run_tests()