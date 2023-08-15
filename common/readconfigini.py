#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import configparser
from config.conf import cm
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
读取这个conf.ini配置文件以使用里面的信息
###
可以看到我们用python内置的configparser模块对config.ini文件进行了读取。
对于url值的提取，我使用了高阶语法@property属性值，写法更简单。
"""

HOST = 'HOST'


class ReadConfig(object):
    """配置文件"""

    def __init__(self):
        self.config = configparser.RawConfigParser()  # 当有%的符号时请使用Raw读取
        self.config.read(cm.ini_file, encoding='utf-8')

    def _get(self, section, option):
        """获取"""
        return self.config.get(section, option)

    def _set(self, section, option, value):
        """更新"""
        self.config.set(section, option, value)
        with open(cm.ini_file, 'w') as f:
            self.config.write(f)

    @property
    def url(self):
        return self._get(HOST, HOST)


ini = ReadConfig()

if __name__ == '__main__':
    print(ini.url)