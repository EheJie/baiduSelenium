# coding:utf-8
from threading import TIMEOUT_MAX
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains;
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
sys.path.append('../po') # 把Page模块所在路径加到环境变量中
from po.Page import Page

class BaiduSearchPage(Page):

    ################# Elements Locator ##############################
    shezhi_Btn_CSS = (By.CSS_SELECTOR,"#s-usersetting-top[name='tj_settingicon']")
    shezhi_optionsMenu_CSS = (By.CSS_SELECTOR,".s-user-setting-pfmenu")
    souSuoSheZhi_option_LinkText = (By.LINK_TEXT,u"搜索设置")
    souSuoSheZhi_Menu_CSS = (By.CSS_SELECTOR,".bdlayer.s-isindex-wrap .pfpanel-bd")
    meiYe10_CSS = (By.CSS_SELECTOR,".bdlayer.s-isindex-wrap .pfpanel-bd  #se-setting-3 label[for='nr_1']")
    meiYe20_CSS = (By.CSS_SELECTOR,".bdlayer.s-isindex-wrap .pfpanel-bd  #se-setting-3 label[for='nr_2']")
    meiYe50_CSS = (By.CSS_SELECTOR,".bdlayer.s-isindex-wrap .pfpanel-bd  #se-setting-3 label[for='nr_3']")
    saveSetting_Btn_LinText = (By.LINK_TEXT,"保存设置")
    search_input_CSS = (By.CSS_SELECTOR,"input#kw")
    baiDuYiXia_CSS = (By.CSS_SELECTOR,"input#su")
    search_Result_Xpath = (By.XPATH,"//*[@id='content_left']/div[contains(@class,'result')]")  # 此处定位不通用，待加强
    results_title_Xpath = (By.XPATH,"//*[@id='content_left']/div[contains(@class,'result')]//h3") # 此处定位不通用，待加强
    ad_result_CSS =  (By.CSS_SELECTOR,"#content_left span.ec-tuiguang")
    souSuoGongJu_CSS = (By.CSS_SELECTOR,".result-molecule .tool_3HMbZ")
    shiJianBuXian_Xpath = (By.XPATH,"//*[contains(text(),'时间不限')][contains(@class,'hovering_1RCgm')]")
    popoverMenu_CSS = (By.CSS_SELECTOR,"div.pop_over_ppVmY")
    def setingTimeValue_Xpath(text):
        return (By.XPATH,"//li[text()=' "+ text +" ']")
    timeInresults_Xpath = (By.XPATH,"//*[@id='content_left']/div[contains(@class,'result')]//*[@class='c-color-gray2']")


    ##对象操作##
    def hover_Shezhi_button(self):
        ele_SheZhi = self.driver.find_element(*self.shezhi_Btn_CSS)
        ActionChains(self.driver).move_to_element(ele_SheZhi).perform()
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.CSS_SELECTOR,".s-user-setting-pfmenu")))

    def clickSouSuoSheZhi(self):
        self.driver.find_element(*self.souSuoSheZhi_option_LinkText).click()
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.CSS_SELECTOR,".bdlayer.s-isindex-wrap .pfpanel-bd")))

    def setMeiyeTiaoShu(self,displayNum):
        # 设置显示条数的按钮， displayNum 取值为： 10/20/50
        if displayNum == 10:
            self.driver.find_element(*self.meiYe10_CSS).click()
        elif displayNum == 20:
            self.driver.find_element(*self.meiYe20_CSS).click()
        elif displayNum == 50:
            self.driver.find_element(*self.meiYe50_CSS).click()
        else:
            self.loger.error("请输入正确的预期显示条数, 10/20/50!!!")
    
    def clickSaveSetting(self):
        self.driver.find_element(*self.saveSetting_Btn_LinText).click()
        WebDriverWait(self.driver,5).until(EC.alert_is_present())
    
    def acceptAlert(self):
        self.driver.switch_to.alert.accept()
        WebDriverWait(self.driver,5).until(EC.invisibility_of_element_located((By.CSS_SELECTOR,".bdlayer.s-isindex-wrap .pfpanel-bd")))

    def send_searchValue(self,searchValue):
        self.driver.find_element(*self.search_input_CSS).send_keys(searchValue)

    def click_BaiduYixia(self):
        self.driver.find_element(*self.baiDuYiXia_CSS).click()
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='content_left']/div[contains(@class,'result')]")))

    def get_MeiyeResultsNumber(self):
        eles_result = self.driver.find_elements(*self.results_title_Xpath)
        return len(eles_result)
    
    def get_ADResultsNum(self):
        ## 获取并打印结果中的广告数
        eles_ad = self.driver.find_elements(*self.ad_result_CSS)
        return len(eles_ad)
    
    def click_souSuoGongJu(self):
        self.driver.find_element(*self.souSuoGongJu_CSS).click()
        time.sleep(1)
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"//*[contains(text(),'时间不限')][contains(@class,'hovering_1RCgm')]")))
    
    def click_shiJianBuXian(self):
        # self.driver.find_element(*self.shiJianBuXian_Xpath).click()
        self.driver.find_element(*self.shiJianBuXian_Xpath).click()

    def set_resultTime(self,timeSetting):
        if timeSetting in ["一天内","一周内","一月内","一年内"]:
            self.driver.find_element(By.XPATH,"//li[text()=' "+ timeSetting +" ']").click()
            
        else:
            self.loger.info("其他自定义code待编辑!")
            return False

    def get_ResultTimeTextList(self):
        timeInresults_Xpath = "//*[@id='content_left']/div[contains(@class,'result')]//*[@class='c-color-gray2']"
        # eles_timeInResults = self.driver.find_elements_by_xpath(timeInresults_Xpath)
        eles_timeInResults = self.driver.find_elements(By.XPATH,timeInresults_Xpath)
        eles_timeTextList= []
        for ele in eles_timeInResults:
            eleText = ele.text
            eles_timeTextList.append(eleText)
        return eles_timeTextList

    
    def verify_ResultTimeSetting(self,eles_timeTextList,timeSetting):
        if timeSetting==u"一天内":
            for eleText in eles_timeTextList:
                if u"天前" in eleText or  u"年" in eleText:
                    return False
            return True
        else:
            # 其他校验code 待编辑
            return False

if __name__ == '__main__':
    pass
