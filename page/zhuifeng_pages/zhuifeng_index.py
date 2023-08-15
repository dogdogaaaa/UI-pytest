from page.basePage import PageObject, PageElement
from page.basePage import *

"""
-------------------------------------------------
   File Name：
   Description :
   Author :   xiaobei
   CreateDate：
   wechat：xiaobei_upup
-------------------------------------------------
"""
"""
在平时中我们应该养成写注释的习惯，因为过一段时间后，没有注释，代码读起来很费劲。
"""


class zhuifeng_index_page(PageObject):
    input_account = PageElement(xpath='/html/body/section/main/div/div[2]/div/form/div[1]/div/div/input')
    input_password = PageElement(xpath='/html/body/section/main/div/div[2]/div/form/div[2]/div/div/input')
    auto_code = PageElement(xpath='/html/body/section/main/div/div[2]/div/form/div[3]/div/div/input')
    log_in_button = PageElement(xpath='/html/body/section/main/div/div[2]/div/form/div[4]/div/button[1]')
    image = PageElement(id='code')
    image_code = PageElement(xpath='/html/body/section/main/div/div[2]/div/form/div[3]/div/div/input')


    @property
    def click_log_in_button(self):
        """点击搜索"""
        return self.log_in_button.click()



