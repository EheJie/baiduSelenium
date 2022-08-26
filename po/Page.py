# coding:utf-8

class Page():
    """
    基类，用于所有页面类的继承
    """
    Baidu_url = 'https://www.baidu.com/'

    def __init__(self,driver,url=Baidu_url):
        self.driver = driver
        self.url = url
        self.driver.get(self.url)


    def find_element(self,*location):
        return self.driver.find_element(*location)

    def find_elements(self,*location):
        return self.driver.find_elements(*location)

if __name__ == '__main__':
    pass



