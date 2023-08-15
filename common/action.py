#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：
   Description :
   Author :   xiaobei
   CreateDate：
   wechat：xiaobei_upup
-------------------------------------------------
"""

import math
import os
import time


def swipe_view_by_percent(driver, x1, y1, x2, y2):
    """
    滑动函数（百分比类型）
    Args:
        driver: appium驱动。webdriver类型
        x1: 滑动起点坐标的横坐标占屏幕宽度的百分比。0<x1<1
        y1: 滑动起点坐标的纵坐标占屏幕高度的百分比。0<y1<1
        x2: 滑动终点坐标的横坐标占屏幕宽度的百分比。0<x2<1
        y2: 滑动终点坐标的纵坐标占屏幕高度的百分比。0<y2<1

    Returns:

    """
    width = driver.get_window_size()['width']
    height = driver.get_window_size()['height']
    detal_x = abs(x2 - x1) * width  # x坐标差值
    detal_y = abs(y2 - y1) * height  # y坐标差值
    t = math.sqrt(detal_x ** 2 + detal_y ** 2) * 5
    driver.swipe(x1 * width, y1 * height, x2 * width, y2 * height, t)
    time.sleep(1)


def swipe_view(driver, start_point, end_point):
    is_ele_num = 0
    if is_appium_element(start_point):
        is_ele_num += 1

    if is_appium_element(end_point):
        is_ele_num += 1
    start_point_coordinate = get_point_coordinate(start_point)
    # print(start_point_coordinate)
    end_point_coordinate = get_point_coordinate(end_point)
    # print(end_point_coordinate)
    duration = math.sqrt((end_point_coordinate['x'] - start_point_coordinate['x']) ** 2 + (
            end_point_coordinate['y'] - start_point_coordinate['y']) ** 2) * 5
    if is_ele_num == 2:
        driver.scroll(start_point, end_point, duration)
    else:
        driver.swipe(start_point_coordinate['x'], start_point_coordinate['y'], end_point_coordinate['x'],
                     end_point_coordinate['y'], duration)

def swipe_view_time(driver, start_point, end_point, duration):
    is_ele_num = 0
    if is_appium_element(start_point):
        is_ele_num += 1

    if is_appium_element(end_point):
        is_ele_num += 1
    start_point_coordinate = get_point_coordinate(start_point)
    # print(start_point_coordinate)
    end_point_coordinate = get_point_coordinate(end_point)
    # print(end_point_coordinate)
    # duration = math.sqrt((end_point_coordinate['x'] - start_point_coordinate['x']) ** 2 + (
            # end_point_coordinate['y'] - start_point_coordinate['y']) ** 2) * 5
    if is_ele_num == 2:
        driver.scroll(start_point, end_point, duration)
    else:
        driver.swipe(start_point_coordinate['x'], start_point_coordinate['y'], end_point_coordinate['x'],
                     end_point_coordinate['y'], duration)

def is_appium_element(element):
    import appium
    if isinstance(element, appium.webdriver.webelement.WebElement):
        return True
    else:
        return False


def get_point_coordinate(ele):
    import re
    coordinate = {}
    if is_appium_element(ele):
        temp = ele.get_attribute('bounds')
        print(temp)
        searchObj = re.search(r'\[(\d+),(\d+)\]\[(\d+),(\d+)\]', temp)
        if searchObj:
            x_1 = int(searchObj.group(1))
            y_1 = int(searchObj.group(2))
            x_2 = int(searchObj.group(3))
            y_2 = int(searchObj.group(4))
            coordinate['x'] = (x_2 - x_1) / 2 + x_1
            coordinate['y'] = (y_2 - y_1) / 2 + y_1
        else:
            # TODO 抛出异常
            pass
    elif isinstance(ele, tuple):
        coordinate['x'] = ele[0]
        coordinate['y'] = ele[1]
    else:
        # TODO 抛出异常
        pass
    return coordinate


def get_zhibiao_button(ele):
    import re
    coordinate = {}
    temp = ele.get_attribute('bounds')
    print(temp)
    searchObj = re.search(r'\[(\d+),(\d+)\]\[(\d+),(\d+)\]', temp)
    if searchObj:
        x_2 = int(searchObj.group(3))
        y_2 = int(searchObj.group(4))
        coordinate['x'] = x_2 / 2
        coordinate['y'] = y_2 - 100
    else:
        # TODO 抛出异常
        pass
    print([coordinate['x'], coordinate['y']])
    return [(coordinate['x'], coordinate['y'])]


def close_open_app(driver, bundld_id, use_key_element=False, key_element=None):
    """
    app关闭重启函数
    Args:
        driver:         appium驱动
        bundld_id:      要操作的app包名
        use_key_element:    是否校验关键元素
        key_element:    关键元素


    Returns:

    """
    time.sleep(4)
    if driver.query_app_state(bundld_id) == 4:
        if use_key_element:
            if key_element is not None:
                return True
    try:
        staus = driver.terminate_app(bundld_id, timeout=5000)
    except:
        driver.close_app()  # 该函数仅能关闭初始化指定的app

    driver.activate_app(bundld_id)
    if driver.query_app_state(bundld_id) == 4:
        return True
    else:
        return False
