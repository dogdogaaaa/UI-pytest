#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
"""
# ================================================== 
# @Time : 2023-08-12 19:20:47 
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

from page.wps_index.login_page import wps_login


def login(driver, username, password):
    login1 = wps_login(driver)
    login1