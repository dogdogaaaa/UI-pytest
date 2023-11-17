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
# @Desc : 免费验证码识别
# @跳槽辅导：初中高级测试跳槽涨薪就业辅导，详情咨询微信
# @求职辅导：初中高级测试求职就业速成辅导，详情咨询微信
# @特色： 小北独创VIP面试速成课程，拿下心仪的offer
# @如何付款：小程序付款 or 支付宝 or 微信
# ==================================================
"""
from PIL import Image
import ddddocr


def image_identify(driver, ele, whole_name, crop_name):
    """
    :param driver: 浏览器驱动
    :param ele: 验证码的元素
    :param whole_name: 整个页面的截图名字
    :param crop_name:  页面中对于验证码的抠图名字
    :return: 返回验证码识别出来的字符串
    """
    driver.save_screenshot(whole_name)
    left = ele.location['x']
    top = ele.location['y']
    right = ele.size['width'] + left
    height = ele.size['height'] + top

    img = Image.open(whole_name).crop((left, top, right, height))
    img.save(crop_name)

    ocr = ddddocr.DdddOcr()
    with open(crop_name, 'rb') as f:
        image = f.read()
    res = ocr.classification(image)
    print(res)
    return res
