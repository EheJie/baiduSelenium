# coding=utf-8
import os
import sys
sys.path.append('..')
import time
import unittest
import HTMLTestRunner
from Base import Base
from po.BaiduSeachPage import BaiduSearchPage
from libs.ShareModules import InsertLog


class BaiduSearch(Base):
    u'''百度抖索功能测试'''
    
    def test_searchSetting_TiaoShu20(self):
        u'''测试搜索设置每页显示条数为20'''
        obj = BaiduSearchPage(self.driver)
        obj.hover_Shezhi_button()
        obj.clickSouSuoSheZhi()
        obj.setMeiyeTiaoShu(20)
        obj.clickSaveSetting()
        obj.acceptAlert()
        obj.send_searchValue("沉思录")
        obj.click_BaiduYixia()   
        time.sleep(3) 
        meiYeTiaoshu = obj.get_MeiyeResultsNumber()
        self.assertEqual(meiYeTiaoshu,20,"实际条数为：" + str(meiYeTiaoshu))

    def test_searchResults_ADTiaoShu(self):
        u'''测试搜索结果含有广告'''
        obj = BaiduSearchPage(self.driver)
        obj.send_searchValue("沉思录")
        obj.click_BaiduYixia()
        adTiaoshu = obj.get_ADResultsNum()
        InsertLog('info',"Has Advertisement Number: "+str(adTiaoshu))        
        self.assertTrue(adTiaoshu>0, "结果中没有广告！！")
        

    def test_searchResultTimeSetting_YiTian(self):
        u'''设置显示一天内的搜索结果，检测结果'''
        obj = BaiduSearchPage(self.driver)
        obj.send_searchValue("沉思录")
        obj.click_BaiduYixia()  
        time.sleep(3)
        obj.click_souSuoGongJu()
        obj.click_shiJianBuXian()
        obj.set_resultTime(u"一天内")
        time.sleep(3)
        timeTextList = obj.get_ResultTimeTextList()
        success = obj.verify_ResultTimeSetting(timeTextList,u'一天内')
        self.assertTrue(success,"时间列表为: "+ ",".join(timeTextList))

# // 调试
if __name__ == '__main__':
    
    file_path = os.path.join(os.getcwd()+"/result/report/"+"testReport.html")
    f = open(file_path,'wb')
    suite = unittest.TestSuite()
    suite.addTest(BaiduSearch('test_searchSetting_TiaoShu20'))
    suite.addTest(BaiduSearch('test_searchResults_ADTiaoShu'))
    suite.addTest(BaiduSearch('test_searchResultTimeSetting_YiTian'))
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="This is BaiduSearch report",description=u"这个是我们百度搜索报告",verbosity=2)
    runner.run(suite)
