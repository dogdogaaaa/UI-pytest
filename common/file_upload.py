"""
-------------------------------------------------
   File Name：
   Description :
   Author :   xiaobei
   CreateDate：
   wechat：xiaobei_upup
-------------------------------------------------
"""
import os
import time
from pywinauto import Desktop
from pywinauto.keyboard import send_keys


def upload_files(file_path):
    """
    :param file_path: files path which geometry files in directory
    """

    app = Desktop()
    dialog = app['打开']
    # 根据名字找到弹出窗口
    dialog["Edit"].type_keys(file_path)
    # 在弹出的框中输入相关的值。
    dialog["Button"].click()



# def upload_files(file_path, *args):
#     """
#     :param file_path: files path which geometry files in directory
#     :param args: file name about geometry files
#     """
#     app = Desktop()
#     # select the explorer file popover
#     shon = app["Select Geometry Files"]
#     # accept the one or more files to write into input box
#     for i in args:
#         send_keys('"{}"'.format(i))
#     url_tab = shon["Toolbar3"]
#     url_tab.click()
#     # input url of the geometry files
#     send_keys(file_path)
#     send_keys("{VK_RETURN}")
#     time.sleep(1)
#     shon["打开(O)"].click_input()
