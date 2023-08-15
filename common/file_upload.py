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

def upload_files(file_path, *args):
    """
    :param file_path: files path which geometry files in directory
    :param args: file name about geometry files
    """
    app = Desktop()
    # select the explorer file popover
    shon = app["Select Geometry Files"]
    # accept the one or more files to write into input box
    for i in args:
        send_keys('"{}"'.format(i))
    url_tab = shon["Toolbar3"]
    url_tab.click()
    # input url of the geometry files
    send_keys(file_path)
    send_keys("{VK_RETURN}")
    time.sleep(1)
    shon["打开(O)"].click_input()
