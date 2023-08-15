#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# ==================================================
# @Time : 2023-06-23 14:04:29
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
import csv
import threading


"""
test_pytest.fixture + 生成器yield   一起实现了和unittest的setup，teardown一样的前置启动，后置清理的装饰器
"""


@pytest.fixture(scope='function', autouse=True)
def open_baidu(drivers):
    """打开百度"""
    drivers.get(ConfigManager.ZHUIFENG)
    yield
    print("后置")

def read_csv_file(file_path):
    """生成器方式去读取csv里面的数据来做数据驱动测试，yield关键字来控制一行一行的读取字典里面的内容（字典里面的数据是隐形的，还未产生，就和奶糖盒子一样的道理）"""
    with open(file_path, 'r', newline='') as file:
        reader = csv.DictReader(file)  # 这是一个迭代器对象，把每次读取出来的数据都放到字典里面存起来，下面用一个for循环一次一次的去读取字典里面的数据，确保不会一次性将所有的数据读取到内存中。
        for row in reader: # 如过下面没有生成器，那么这里直接全部数据都遍历一遍，如果有生成器就会卡住，一个一个来，接收到next方法才会读取下一行。
            yield row['username'], row['password']

@pytest.mark.parametrize('username, password', read_csv_file(r'H:\Develop\Python\Selenium_UI_Project\data\data.csv'))
def test_001(drivers, username, password):
    zhufeng = zhuifeng_index_page(drivers)
    zhufeng.input_account = username
    zhufeng.input_password = password
    # zhufeng.log_in_button.click()
    zhufeng.click_log_in_button
    # assert drivers.current_url == 'https://exam.wzzz.fun'


if __name__ == '__main__':
    pytest.main(['--alluredir', './reports', 'vs', 'testcases/zhuifeng_tc/test_ddt_zhuifeng_csv_file3.py'])

    # t1 = threading.Thread(target=test_pytest.main,
    #                    args=(["-v", "-s", "testcases/zhuifeng_tc/test_ddt_zhuifeng_csv_file.py"],))
    # t2 = threading.Thread(target=test_pytest.main,
    #                       args=(["-v", "-s", "testcases/zhuifeng_tc/test_ddt_zhuifeng.py"],))
    # t3 = threading.Thread(target=test_pytest.main,
    #                       args=(["-v", "-s", "testcases/zhuifeng_tc/test_zhuifeng_system.py"],))
    #
    # t1.start()
    # t2.start()
    # t3.start()
    #
    #
    # t1.join()
    # t2.join()
    # t3.join()
