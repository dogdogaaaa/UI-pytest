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
from page.zhuifeng_pages.file_upload_pages import FileUpload
from config.conf import ConfigManager
import time
from pywinauto import Desktop
from common.image_identify import image_identify
"""
test_pytest.fixture + 生成器yield   一起实现了和unittest的setup，teardown一样的前置启动，后置清理的装饰器
"""


class TestFileUpload:
    @pytest.fixture(scope='function', autouse=True)
    def open_file_upload(self, drivers):
        """打开文件上传网址"""
        drivers.get(ConfigManager.FILE_UPLOAD)
        yield
        print("后置")

    @pytest.mark.smoke
    def test_001(self, drivers):
        file = FileUpload(drivers)
        file.click_file_choose
        time.sleep(3)

        app = Desktop()
        dialog = app['打开']
        # 根据名字找到弹出窗口
        dialog["Edit"].type_keys('1.jpg')
        # 在弹出的框中输入相关的值。
        dialog["Button"].click()


if __name__ == '__main__':
    pytest.main(['vs', 'testcases/test_pytest/test_file_upload.py'])
