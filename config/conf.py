#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
from selenium.webdriver.common.by import By
from common.times import dt_strftime
"""
配置文件总是项目中必不可少的部分！
将固定不变的信息集中在固定的文件中
这个conf文件我模仿了Django的settings.py文件的设置风格，但是又有些许差异
author: B站小北  time：2023-04-18
"""

class ConfigManager(object):
    """
    在这个文件中我们可以设置自己的各个目录，也可以查看自己当前的目录。

    遵循了约定：不变的常量名全部大写，函数名小写。看起来整体美观。
    """
    # 项目目录
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 页面元素目录
    ELEMENT_PATH = os.path.join(BASE_DIR, 'page_element')

    # 报告文件
    REPORT_FILE = os.path.join(BASE_DIR, 'report.html')

    # 元素定位的类型
    LOCATE_MODE = {
        'css': By.CSS_SELECTOR,
        'xpath': By.XPATH,
        'name': By.NAME,
        'id': By.ID,
        'class': By.CLASS_NAME
    }

    # 邮件信息
    EMAIL_INFO = {
        'username': '2211484376@qq.com',  # 切换成你自己的地址
        'password': 'QQ邮箱授权码',
        'smtp_host': 'smtp.qq.com',
        'smtp_port': 465
    }

    # 收件人
    ADDRESSEE = [
        '2211484376@qq.com',
    ]

    # 测试网址
    BAIDU_URL = "https://www.baidu.com"
    ZHUIFENG = "https://exam.wzzz.fun"
    WPS_LOGIN = "https://account.wps.cn/"
    FILE_UPLOAD = "https://letcode.in/file"
    WMS_URL = "http://192.168.10.129/login?redirect=%2Findex"
    WHOLE_PATH = "./screenshots/简单验证码.png"
    CROP_PATH = "./screenshots/crop_pic.png"
    USERNAME = "admin"
    PASSWORD = "123456"
    @property
    def log_file(self):
        """日志目录"""
        log_dir = os.path.join(self.BASE_DIR, 'logs')
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        return os.path.join(log_dir, '{}.log'.format(dt_strftime()))

    @property
    def ini_file(self):
        """配置文件"""
        ini_file = os.path.join(self.BASE_DIR, 'config', 'config.ini')
        if not os.path.exists(ini_file):
            raise FileNotFoundError("配置文件%s不存在！" % ini_file)
        return ini_file


cm = ConfigManager()
if __name__ == '__main__':
    print(cm.BASE_DIR)