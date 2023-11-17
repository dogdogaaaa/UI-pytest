#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
"""
# ================================================== 
# @Time : 2023-06-23 13:55:01 
# @Author : 小北
# @微信：xiaobei_upup
# @Email : 2211484376@qq.com
# @QQ群：585971269
# @微信群：可加我微信拉你
# @Site : 苏州
# @Desc : 
# @跳槽辅导：初中高级测试跳槽涨薪面试辅导，详情咨询微信
# @求职辅导：初中高级测试求职面试辅导，详情咨询微信
# @特色： 小北独创VIP面试速成课程，拿下心仪的offer
# @如何付款：先拿offer再付款，只需交定金，相互信任无套路
# ================================================== 
"""
import pytest
from page.zhuifeng_pages.zhuifeng_index import zhuifeng_index_page
from config.conf import ConfigManager
import time
from common.image_identify import image_identify
"""
test_pytest.fixture + 生成器yield   一起实现了和unittest的setup，teardown一样的前置启动，后置清理的装饰器
"""


class TestSearch:
    @pytest.fixture(scope='function', autouse=True)
    def open_baidu(self, drivers):
        """打开百度"""
        drivers.get(ConfigManager.ZHUIFENG)
        yield
        print("后置")

    @pytest.mark.smoke
    @pytest.mark.parametrize('username, password', [
        ('wzz', '12345')
    ])
    def test_001(self, drivers, username, password):
        zhufeng = zhuifeng_index_page(drivers)
        zhufeng.input_account = username
        zhufeng.input_password = password
        # zhufeng.log_in_button.click()
        zhufeng.image_code = image_identify(drivers, zhufeng.image,  '简单验证码.png', 'crop_pic.png')
        zhufeng.click_log_in_button
        time.sleep(3)




if __name__ == '__main__':
    pytest.main(['vs', 'testcases/test_pytest/test_search_baidu_index.py'])
