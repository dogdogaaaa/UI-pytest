
"""
-------------------------------------------------
   File Name：
   Description :
   Author :   xiaobei
   CreateDate：
   wechat：xiaobei_upup
-------------------------------------------------
"""
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""
它使用了WebDriverWait类，可以检测股票数据是否更新，并判断股票是否涨停或跌停：
启动Chrome驱动程序并在你的浏览器中加载URL。然后，它将等待10秒钟来检查股票价格是否发生变化。
如果股票价格发生变化，则它将打印出涨停或跌停的消息。如果股票价格未发生变化，则测试失败

"""
class RefreshChecker:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome()

    def __enter__(self):
        self.driver.get(self.url)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.driver.quit()

    def get_price(self):
    # get current price
        a = self.driver.find_element_by_id('price').text
        return a


    def check_refresh(self, previous_price, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element((By.ID, 'price'), lambda price: price != previous_price))
        current_price = self.get_price()
        price_change = float(current_price) - float(previous_price)
        if price_change >= 10:
            print("涨停！")
        elif price_change <= -10:
            print("跌停！")
# 测似
    def test_refresh_checker():
        with RefreshChecker("http://www.baidu.com/stock") as checker:
            previous_price = checker.get_price()
            checker.check_refresh(previous_price)
