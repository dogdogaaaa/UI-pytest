#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
"""
# ================================================== 
# @Time : 2023-08-15 18:42:37 
# @Author : 小北
# @微信：xiaobei_upup
# @Email : 2211484376@qq.com
# @QQ群：585971269
# @微信群：可加我微信拉你
# @Site : 苏州
# @Desc : 
# @跳槽辅导：初中高级测试跳槽涨薪就业辅导，详情咨询微信
# @求职辅导：初中高级测试求职就业辅导，详情咨询微信
# @特色： 小北独创VIP就业速成课程，拿下心仪的offer
# @如何付款：官方小程序付款 or 微信 or 支付宝
# ================================================== 
"""

from page.basePage import *

class FileUpload(PageObject):
    file_choose = PageElement(css='.file-label')


    @property
    def click_file_choose(self):
        """点击搜索"""
        return self.file_choose.click()