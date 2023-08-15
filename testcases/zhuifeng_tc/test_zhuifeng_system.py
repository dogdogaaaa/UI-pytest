#!/usr/bin/env python3
# -*- coding:utf-8 -*-

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
from page.zhuifeng_pages.zhuifeng_index import zhuifeng_index_page
from config.conf import ConfigManager
import time

"""
test_pytest.fixture + 生成器yield   一起实现了和unittest的setup，teardown一样的前置启动，后置清理的装饰器
"""


class TestSearch2:
    @pytest.fixture(scope='function', autouse=True)
    def open_baidu(self, drivers):
        """打开"""
        drivers.get(ConfigManager.ZHUIFENG)
        yield
        print("后置")

    @pytest.mark.parametrize('username, password', [
        ('user1', 'pass1'),
        ('user2', 'pass2'),
        ('user3', 'pass3')
    ])
    def test_001(self, drivers,username, password):
        zhufeng = zhuifeng_index_page(drivers)
        zhufeng.input_account = username
        zhufeng.input_password = password
        time.sleep(3)


    # @allure.step("操作步骤2")
    # def test_002(self, drivers):
    #     baidu = baidu_index_page(drivers)
    #     baidu.search_frame.send_keys('阿里巴巴')
    #
    #     baidu.click_search
    #     webdriver = WebPage(drivers)
    #     webdriver.refresh()
    #     # print(webdriver.get_source)
    #     assert baidu.search_button
    #     # log.info()

