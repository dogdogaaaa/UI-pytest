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
from pywinauto import Desktop
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By

from page.zhuifeng_pages.zhuifeng_index import zhuifeng_index_page
from page.wms_pages.wms_elements import WmsElements
from config.conf import ConfigManager
import time
from common.image_identify import image_identify
from common.file_upload import upload_files


class TestUploadElement:
    # @pytest.fixture(scope='function', autouse=True)
    # def login_logout(self, drivers):
    #     """登录wms网站然后pytest的测试用例执行完后再执行登出操作"""
    #     drivers.get(ConfigManager.WMS_URL)
    #
    #     yield
    #     print("后置")

    # @pytest.mark.test1
    @pytest.mark.parametrize('username, password', [
        ('admin', '123456')
    ])
    def test_001_add_upload_element(self, drivers, username, password):
        """
            在一个def用例里面，如果有一个assert执行失败，那么整个用例都会停下来，所以要将用例原子化一些
        """
        # 访问网址
        drivers.get(ConfigManager.WMS_URL)

        account = drivers.find_elements(By.CLASS_NAME, "el-input__inner")[0]
        account.send_keys(username)
        password1 = drivers.find_elements(By.CLASS_NAME, "el-input__inner")[1]
        password1.send_keys(password)

        time.sleep(3)

        login = drivers.find_elements(By.CLASS_NAME, "el-button")[0]
        assert login.text == "登 录"
        assert login.is_displayed() == True
        login.click()



        churuku = drivers.find_elements(By.CLASS_NAME, "el-submenu__title")[2]
        churuku.click()
        # ruku = drivers.find_element(By.CLASS_NAME, "el-menu-item")
        # ruku.click()
        systemtool = drivers.find_elements(By.CLASS_NAME, "el-submenu__title")[4]
        systemtool.click()
        time.sleep(2)
        ul = drivers.find_element(By.CLASS_NAME, "el-menu--inline")

        # li = ul.find_elements(By.TAG_NAME, "li")[0]
        li = ul.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[8]/li/ul/div[1]/a')
        assert li.is_displayed() == True
        li.click()
        time.sleep(2)
        form_gen = drivers.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[1]/div[1]/div')
        assert form_gen.text == "Form Generator"


        upload = drivers.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/div[1]/div/div/div[4]/div[13]/div')
        upload.click()


        # uploadbutton = drivers.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[2]/div[2]/div[1]/div/div/form/div[1]/div[2]/div/div/div/div/button')
        # uploadbutton.click()
        #
        # app = Desktop()
        # dialog = app['打开']
        # # 根据名字找到弹出窗口
        # dialog["Edit"].type_keys(r'E:\Develop\Python\selenium_projects\xiaobei_selenium_automation\common\img.png')
        # # 在弹出的框中输入相关的值。
        # dialog["Button"].click()
        # time.sleep(3)
        #
        # # 对文件上传的图标断言
        # icon = drivers.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[2]/div[2]/div[1]/div/div/form/div[1]/div[2]/div/div/div/div/button/i')
        # assert icon.is_displayed() == True
        # button_name = drivers.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[2]/div[2]/div[1]/div/div/form/div[1]/div[2]/div/div/div/div/button/span')
        # assert button_name.text == "点击上传"
        #
        # head_upload_name = drivers.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[2]/div[2]/div[1]/div/div/form/div[1]/div[2]/div/label')
        # assert head_upload_name.text == "上传"
        #
        #
        # # 最后删除添加的各个组件
        # delete_icon = drivers.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[2]/div[2]/div[1]/div/div/form/div[1]/div[2]/span[2]')
        # delete_icon.click()
        #
        # # 判断文件上传组件是否删除
        # # try:
        # #     button = drivers.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[2]/div[2]/div[1]/div/div/form/div[1]/div[2]/div')
        # # except NoSuchElementException:
        # #     raise AssertionError(f"组件 {button} 不存在")  # 当一个用例里面出现了抛出异常的情况，那么def函数用例也会停止执行，一旦发现测试用例失败（包括断言失败、异常抛出等），pytest 将立即停止执行其他的测试用例，以减少不必要的运行时间。
        #
        # # 对于input框的操作
        # input_phone_number = drivers.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[2]/div[2]/div[1]/div/div/form/div[1]/div[1]/div/div/div/input')
        # input_phone_number.send_keys("17205290079")
        # input_phone_number.clear()
        # time.sleep(5)
        # right_number = drivers.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[2]/div[2]/div[1]/div/div/form/div[1]/div[1]/div/div/div/span[2]/span/span/span')
        # assert input_phone_number.get_attribute("placeholder") == "请输入手机号"   # 获取input框中的默认提示语
        # # assert right_number.text == "0/11"      # 这里有一个bug，由于电话号码都被clear清空了，后面的数据应该为0，而不是11，这里断言发现了一个bug，然后手动复现也是有这个bug的，然后就提bug了。
        # input_phone_number.send_keys("17205290078")
        # right_number.click()
        #
        # assert right_number.text == "11/11"
        # assert input_phone_number.get_attribute("value") == "17205290078"  # 对刚刚输入input框的str做断言，不能用text，因为是断言非用户输入的文本，后者是断言用户输入的文本，这里也可以在面试中如果被问道查看测试报告中的一些断言报错，就可以说这个。

        # ------------鼠标滑动操作------------
        # action = ActionChains(drivers)
        # # 第一步：在滑块处按住鼠标左键
        # action.click_and_hold(upload)
        # # 第二步：相对鼠标当前位置进行移动
        # action.move_by_offset(300, 300)
        # # 第三步：释放鼠标
        # action.release()
        # # 执行动作
        # action.perform()
        #
        # time.sleep(5)

    def test_002_upload_files(self, drivers):

        uploadbutton = drivers.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[2]/div[2]/div[1]/div/div/form/div[1]/div[2]/div/div/div/div/button')
        uploadbutton.click()

        app = Desktop()
        dialog = app['打开']
        # 根据名字找到弹出窗口
        dialog["Edit"].type_keys(r'E:\Develop\Python\selenium_projects\xiaobei_selenium_automation\common\img.png')
        # 在弹出的框中输入相关的值。
        dialog["Button"].click()
        time.sleep(3)


        # # 对文件上传的图标断言
        # icon = drivers.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[2]/div[2]/div[1]/div/div/form/div[1]/div[2]/div/div/div/div/button/i')
        # assert icon.is_displayed() == True
        # button_name = drivers.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[2]/div[2]/div[1]/div/div/form/div[1]/div[2]/div/div/div/div/button/span')
        # assert button_name.text == "点击上传"
        #
        # head_upload_name = drivers.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[2]/div[2]/div[1]/div/div/form/div[1]/div[2]/div/label')
        # assert head_upload_name.text == "上传"
        #
        #
        # # 最后删除添加的各个组件
        # delete_icon = drivers.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[2]/div[2]/div[1]/div/div/form/div[1]/div[2]/span[2]')
        # delete_icon.click()
        #
        # # 判断文件上传组件是否删除
        # # try:
        # #     button = drivers.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[2]/div[2]/div[1]/div/div/form/div[1]/div[2]/div')
        # # except NoSuchElementException:
        # #     raise AssertionError(f"组件 {button} 不存在")  # 当一个用例里面出现了抛出异常的情况，那么def函数用例也会停止执行，一旦发现测试用例失败（包括断言失败、异常抛出等），pytest 将立即停止执行其他的测试用例，以减少不必要的运行时间。
        #
        # # 对于input框的操作
        # input_phone_number = drivers.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[2]/div[2]/div[1]/div/div/form/div[1]/div[1]/div/div/div/input')
        # input_phone_number.send_keys("17205290079")
        # input_phone_number.clear()
        # time.sleep(5)
        # right_number = drivers.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[2]/div[2]/div[1]/div/div/form/div[1]/div[1]/div/div/div/span[2]/span/span/span')
        # assert input_phone_number.get_attribute("placeholder") == "请输入手机号"   # 获取input框中的默认提示语
        # # assert right_number.text == "0/11"      # 这里有一个bug，由于电话号码都被clear清空了，后面的数据应该为0，而不是11，这里断言发现了一个bug，然后手动复现也是有这个bug的，然后就提bug了。
        # input_phone_number.send_keys("17205290078")
        # right_number.click()
        #
        # assert right_number.text == "11/11"
        # assert input_phone_number.get_attribute("value") == "17205290078"  # 对刚刚输入input框的str做断言，不能用text，因为是断言非用户输入的文本，后者是断言用户输入的文本，这里也可以在面试中如果被问道查看测试报告中的一些断言报错，就可以说这个。

        # ------------鼠标滑动操作------------
        # action = ActionChains(drivers)
        # # 第一步：在滑块处按住鼠标左键
        # action.click_and_hold(upload)
        # # 第二步：相对鼠标当前位置进行移动
        # action.move_by_offset(300, 300)
        # # 第三步：释放鼠标
        # action.release()
        # # 执行动作
        # action.perform()
        #
        # time.sleep(5)








