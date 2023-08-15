"""
-------------------------------------------------
   File Name：
   Description :
   Author :   xiaobei
   CreateDate：
   wechat：xiaobei_upup
-------------------------------------------------
"""
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest


class ScreenshotUtil:
    def __init__(self):
        self.driver = None

    def create_driver(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(chrome_options=options)

    def take_screenshot(self, name):
        if not self.driver:
            self.create_driver()
        self.driver.get_screenshot_as_file(os.path.join(os.getcwd(), f"{name}.png"))

    def close_driver(self):
        if self.driver:
            self.driver.quit()


@pytest.fixture()
def screenshot():
    screenshot_util = ScreenshotUtil()
    yield screenshot_util
    screenshot_util.close_driver()


def test_take_screenshot(screenshot):
    screenshot.take_screenshot("test")
    assert os.path.isfile(os.path.join(os.getcwd(), "test.png"))
